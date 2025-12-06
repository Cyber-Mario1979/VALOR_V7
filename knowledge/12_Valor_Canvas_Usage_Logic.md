# 12_Valor_Canvas_Usage_Logic

## 1. Open or Reopen Rules
- **Create** WP/Task/Document/Report → open `document type canvas` with editable true.
- **Edit** WP/Task/Document/Report → reopen `document type canvas` with editable true.
- Never render primary objects in chat; Canvas is the single source of truth.

## 2. Canvas Watchdog Auto-Recover
- **Trigger:** After any create or edit, or if the last reply included a primary object in chat.
- **Action:** use canvas → re-hydrate the active object → reply “Moved to Canvas. Continue.”

## 3. Session Warm-Up
Run `use canvas` at the start of a session before executing any command.  There is no additional mode required beyond M1/M2; documents and reports are handled within work‑package mode (M2).

## 4. No Duplicate States
- If content appears in chat, migrate to Canvas immediately and confirm “Moved to Canvas. Continue.”
- Do not keep parallel versions of the same object.

## 5. Canvas Object Model
- **Work Package:** ID WPxxx, Title, Scope, Objective, Governance, System or Equipment optional, Location optional, Standards optional, Risks optional, Status.
- **Task:** ID WPxxx-Tyyy, Description, Owner, Start Date, Finish Date, Status, Predecessor optional, Acceptance Criteria optional.
- **Document:** DocID, DocType, ModeOfCreation M2, LinkedTo None or WPxxx-Tyyy, Status, Version.
- **Report:** Context Session, Summary, Date, Version.
- **Defaults:** Missing fields “No Entry”; Status “Opened”.

---
