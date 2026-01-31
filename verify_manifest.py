"""VALOR Pack Integrity Verifier

Validates that the current pack folder matches `manifest.yaml`.

Usage:
  python verify_manifest.py

Exit codes:
  0 = PASS
  1 = FAIL (missing/mismatched/extra files)
  2 = ERROR (manifest missing or invalid)

Notes:
- Run this script from the pack root (the folder containing `manifest.yaml`).
- Requires PyYAML: `python -m pip install pyyaml`
"""

import hashlib
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERROR: PyYAML is not installed. Run: python -m pip install pyyaml")
    sys.exit(2)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(".").resolve()
    manifest_path = root / "manifest.yaml"
    if not manifest_path.exists():
        print(f"ERROR: manifest.yaml not found in pack root: {root}")
        return 2

    try:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: Failed to parse manifest.yaml: {e}")
        return 2

    files = manifest.get("files", [])
    if not isinstance(files, list) or not files:
        print("ERROR: manifest.yaml has no valid `files:` list.")
        return 2

    missing = []
    mismatched = []
    ok_count = 0

    for entry in files:
        rel = entry.get("path")
        expected = entry.get("sha256")
        if not rel or not expected:
            print("ERROR: manifest entry missing `path` or `sha256`.")
            return 2

        p = root / rel
        if not p.exists():
            missing.append(rel)
            continue

        actual = sha256_file(p)
        if actual.lower() != str(expected).lower():
            mismatched.append((rel, expected, actual))
        else:
            ok_count += 1

        manifest_paths = set(e.get("path") for e in files if e.get("path"))
    IGNORE_DIRS = {".venv", "venv", "__pycache__", ".vscode", ".git"}

    actual_paths = set()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel_path = p.relative_to(root)
        if rel_path.parts and rel_path.parts[0] in IGNORE_DIRS:
            continue
        actual_paths.add(str(rel_path).replace("\\", "/"))

    # The manifest is the root of truth; do not treat it as an "extra" file.
    actual_paths.discard("manifest.yaml")
    extras = sorted(actual_paths - manifest_paths)

    if missing or mismatched or extras:
        print("FAIL")
        if missing:
            print("\nMissing files:")
            for m in missing:
                print(" -", m)
        if mismatched:
            print("\nHash mismatches:")
            for rel, exp, act in mismatched:
                print(f" - {rel}\n   expected: {exp}\n   actual:   {act}")
        if extras:
            print("\nExtra files (present but not in manifest):")
            for e in extras:
                print(" -", e)
        return 1

    print(f"PASS: {ok_count} files verified and match manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
