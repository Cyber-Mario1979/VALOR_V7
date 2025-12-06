# 13_Valor_Document_Logic

## 1. Numbering and Version Control
- Document ID format DocType-Seq e.g., URS-001
- Optional linkage DocType-WPID-TID e.g., URS-WP003-T002 for traceability
- Versioning Draft 0.1, Approved 1.0, minor increments 1.1, major 2.0
- Status Draft, Under Review, Approved

## 2. Document Control Fields
- Document Title
- System or Equipment
- Location
- Document Number
- Version
- Date dd-mm-yyyy
- Status
- Prepared By and Department
- Reviewed By and Department
- Approved By and Department
- Validation Approach Prospective Concurrent Retrospective
- GAMP Category if applicable

## 3. Generation Logic
- **VMP Extract:** lifecycle strategy, risk, and responsibilities using T1 template
- **URS:** questionnaire sections for Eng QA QC Production SHE Automation; generate URS from responses or skeleton if skipped; assign URS reference numbers
- **Risk Assessment FMEA:** derive from URS functions, S O D ratings and RPN, mitigation, and residual risk
- **RTM:** map URS to DQ IQ OQ PQ and RA IDs
- **DQ IQ OQ PQ:** standardized structures and checklists or test scripts with acceptance criteria
- **VSR:** consolidate lifecycle outcomes, deviations and CAPAs, residual risk, and release recommendation

## 4. User Uploads
- VMP and CQV Questionnaire templates issued blank in Canvas
- Other templates may be auto-populated unless user requests blanks
- Extract key data from uploaded vendor documents if provided

## 5. Linking and Traceability
- Standalone in M2 or linked directly to WP tasks
- Maintain URS numbering across downstream documents
- RA failure modes have unique IDs e.g., RA-FM-001
- Revision history entries on every update

## 6. Quality and Regulatory Alignment
- Align with Annex 15, ASTM E2500, GAMP 5, ICH Q9
- Use Annex 1 context for sterile and HVAC where applicable

## 7. Export Logic
 - Use the existing work‑package export template (`09_Valor_Export_Template.csv`)
- Columns WP ID, WP Title, Owner, Status, Start Date, Finish Date, Planned Duration d, Elapsed d, Remaining d, Lateness d, Percent Time Elapsed
- Dates dd-mm-yyyy and timezone Africa Cairo
---