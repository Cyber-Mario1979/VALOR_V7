"""VALOR Manifest Generator

Regenerates `manifest.yaml` for the current pack folder.

What it does:
- Walks all files in the pack root (recursively).
- Computes SHA-256 and byte size for each file.
- Writes `manifest.yaml` in a deterministic order.

Usage:
  python generate_manifest.py

Notes:
- Run this script from the pack root (the folder containing the pack files).
- Requires PyYAML: `python -m pip install pyyaml`
"""

import hashlib
from datetime import datetime, timezone
from pathlib import Path
import sys

try:
    import yaml  # type: ignore
except ImportError:
    print("ERROR: PyYAML is not installed. Run: python -m pip install pyyaml")
    sys.exit(2)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    root = Path(".").resolve()
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    entries = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()

        # The manifest is the root of truth; we do not hash it inside itself.
        if rel == "manifest.yaml":
            continue

        data = p.read_bytes()
        entries.append({
            "path": rel,
            "sha256": sha256_bytes(data),
            "bytes": len(data),
        })

    manifest = {
        "manifest_version": "v1.0.1",
        "pack": {
            "name": "Valor_Architecture_Pack",
            "pack_version": "v1.0.1",
            "created_at_utc": created_at,
            "hash_algorithm": "sha256",
            "root": ".",
        },
        "files": sorted(entries, key=lambda x: x["path"]),
    }

    manifest_path = root / "manifest.yaml"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print("manifest.yaml regenerated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
