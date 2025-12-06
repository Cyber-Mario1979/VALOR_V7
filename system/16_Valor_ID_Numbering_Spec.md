# Valor ID Numbering Spec

## Purpose
Eliminate blank and duplicate IDs; prevent presets from overriding existing IDs.

## Algorithm
1. **Scan existing IDs** in the current context:
   - WP IDs `WPxxx`
   - Task IDs `WPxxx-Txxx` (per-WP scope)
2. **Determine the next available integer** for each class (global for WPs; per-wp for tasks; per-task).
3. **Never reuse deleted IDs** within the project/session scope (mandated uniqueness).
4. **On Preset Use**:
   - If no active WP canvas → `create wp` (allocate new ID) → then import preset header + tasks into **that** WP.
   - If an active WP canvas exists → import preset into that active WP (do **not** change its ID).
5. **On Task Creation**:
   - Use `WPxxx-T###` numbering; allocate next available `T###` within that WP.
6. **On Document Creation**:
   - Use `<DocType>-###` scheme; allocate next per-DocType number; do not collide with existing docs.

## Enforcement
- **Reject** any operation that would produce a blank or duplicate ID.
- **Warn and block** if a preset import attempts to write into an ID already allocated to another WP.
- **State Echo** must include the full list of IDs in use after any create/edit.
