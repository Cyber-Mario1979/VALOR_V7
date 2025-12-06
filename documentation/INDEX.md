# Repository Index

This index summarizes the main components of the integrated Valor package and where to find them.  The core assistant logic is split into four top‑level folders – `instructions/`, `system/`, `knowledge/` and `templates/` – while supporting documentation and configuration files live alongside them.

## documentation/
Contains meta‑level documentation:

- `CHANGELOG.md` – Revision history from previous repository versions
- `CONTRIBUTING.md` – Guidelines for contributions
- `INDEX.md` – This index file

## Root files
Contains repository‑level documents:

- `README.md` – Overview of the integrated pack
- `LICENSE` – Licensing information

## instructions/, system/, knowledge/ and templates/
Contains all numbered Markdown and CSV files that drive the Valor assistant, including:

- `00_Valor_Instructions.md` – Entry point instructions
- `01_Valor_System_Role_Definition.md` – Defines the system role
- `02_Valor_Rules.md` – Core ruleset
- `03_Valor_State_Machine.md` – Mode transition logic
- `04_Valor_Tone.md` – Tone guidelines
- `05_Valor_Commands_Logic.md` – Command handling logic
- `06_Valor_R_S_Logic.md` – References and standards logic
- `07_Valor_R_S_List.md` – References and standards list
- `08_Valor_Security_Logic.md` – Security safeguards
- `09_Valor_Export_Template.csv` – Export template for WP data
- `10_Valor_WP_Library.md` – Work Package library
- `11_Valor_Few_Shot.md` – Few‑shot example
- `12_Valor_Canvas_Usage_Logic.md` – Canvas usage logic
- `13_Valor_Document_Logic.md` – Document generation logic
- `14_Valor_Document_Index.md` – Index of controlled document templates
- `15_Valor_Document_KB.md` – Knowledge base for controlled templates (T0–T10)
- `16_Valor_ID_Numbering_Spec.md` – WPs ID and Tasks ID numbering specs

## data/
Contains configuration files used for integration with systems that consume YAML:

- `valor_config.yaml` – Runtime configuration and list of knowledge files
- `valor_metadata.yaml` – Metadata about the assistant (identifier, title, version, tags)

## evals/

- `EVALS.md` – Evaluation scenarios used to verify mode transitions, command processing, security enforcement, work‑package lifecycle and export generation
