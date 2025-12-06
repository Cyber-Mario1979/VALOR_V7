# 15_Valor_Document_KB

> File Purpose: Definitive source text for all controlled document templates for Valor.  Preserves anchors and table structures for reliable Canvas rendering and traceability.

## Template Index
- T0: Project Quality Plan (PQP) — Anchor: source-t0-PQP-template-v1-0-0-md
- T1: Validation Master Plan (VMP) Extract — Anchor: source-t1-VMP-template-v1-0-0-md
- T2: CQV Department Questionnaires — Anchor: source-t2-cqv-department-questionnaires-v1-0-0-md
- T3: Risk Assessment (FMEA) — Anchor: source-t3-risk-assessment-template-v1-0-0-md
- T4: User Requirements Specification (URS) — Anchor: source-t4-urs-template-v1-0-0-md
- T5: Requirements Traceability Matrix (RTM) — Anchor: source-t5-rtm-template-md
- T6: Design Qualification (DQ) — Anchor: source-t6-dq-template-v1-0-0-md
- T7: Installation Qualification (IQ) Protocol — Anchor: source-t7-iq-protocol-template-v1-0-0-md
- T8: Operational Qualification (OQ) Protocol — Anchor: source-t8-oq-protocol-template-v1-0-0-md
- T9: Performance Qualification (PQ) Protocol — Anchor: source-t9-pq-protocol-template-v1-0-0-md
- T10: Validation Summary Report (VSR) — Anchor: source-t10-vsr-template-v1-0-0-md
    <!-- T11–T15 removed: repository/work package/task/report/backup schemas deprecated in Valor -->
---
<a id="source-t0-PQP-template-v1-0-0-md"></a>
# Source: T0_PQP_Template_V1_0_0.md

## Template Metadata
- ID: T0
- Title: Project Quality Plan (PQP)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Project Quality Plan (PQP)

## CQV-QA

## 1. Purpose & Scope
Define the quality governance for the project, including boundaries (GxP scope) and interfaces with site/corporate QMS. This plan governs quality practices for all project activities and suppliers. Operational SOPs are referenced, not duplicated.

## 2. Applicable QMS & References
List controlling quality system documents and standards (by title/ID). Examples: Site/Corporate Quality Manual, Document Control SOP, Deviation/CAPA SOP, Training SOP, Change Control SOP, Supplier Management SOP. Include external normative references as applicable.

## 3. Definitions & Abbreviations
⦁ QMS: Quality Management System — the policies, processes, and procedures that govern quality (e.g., document control, training, deviations/CAPA, change control, audits).  
⦁ CQV: Commissioning, Qualification, and Validation — a lifecycle ensuring facilities/equipment/systems are fit for intended use using a risk-based approach.  
⦁ URS: User Requirements Specification — testable, uniquely-identified user needs that define “what the system must do.”  
⦁ RTM: Requirements Traceability Matrix — maps each URS requirement to design elements and to verification in DQ/IQ/OQ/PQ.  
⦁ DQ/IQ/OQ/PQ: Qualification phases:  
⦁ DQ (Design Qualification): Proposed design meets URS/GxP.  
⦁ IQ (Installation Qualification): Installed per approved design/manufacturer specs.  
⦁ OQ (Operational Qualification): Functions operate as intended across defined ranges.  
⦁ PQ (Performance Qualification): Performs effectively and reproducibly under intended (routine) conditions.  
⦁ VSR: Validation Summary Report — consolidates results from DQ/IQ/OQ/PQ, deviations/CAPA, and acceptance decisions to support QA release.  
⦁ CAPA: Corrective and Preventive Action — system to fix root causes of nonconformities and prevent recurrence/occurrence.  
⦁ RPN: Risk Priority Number — severity × occurrence × detection (FMEA) used to prioritize risks and drive mitigations.  
⦁ CQA: Critical Quality Attribute — product/quality attribute that must be within limits to ensure safety, identity, strength, purity, and quality.  
⦁ CPP: Critical Process Parameter — a process variable whose variability impacts a CQA; requires control/monitoring to maintain product quality.

## 4. Roles & Responsibilities (RACI)
High-level RACI for Quality, CQV, Engineering/Automation, Production, QC, IT/CSV, Procurement, and Suppliers.

| Activity | Quality | CQV | Eng/Auto | Production | QC | IT/CSV | Procurement | Supplier |
|---|---|---|---|---|---|---|---|
| Approve QP | A | C | C | C | C | C | C | I |
| Manage Document Control | R | C | C | C | C | C | C | I |
| Manage Deviations/CAPA | A | C | C | C | C | C | I | I |
| Approve Change Control | A | C | C | C | C | C | C | I |
| Audit/Supplier Oversight | A | C | C | I | I | I | C | R |

## 5. Document Control
- Document ID conventions and naming.  
- Versioning and approval workflow.  
- Storage locations and retention periods.  
- Controlled templates and use of watermarks for drafts.

## 6. Training & Competency
- Training requirements, curricula, role matrices.  
- Training completion prior to participation in GxP activities.  
- Maintaining training records; re‑training triggers.

## 7. Deviation / Nonconformance & CAPA
- How to log, classify, investigate, and close deviations.  
- CAPA linkage, effectiveness checks, and escalation.  
- Interfaces with qualification deviations (recorded in protocols).

## 8. Change Control
- When change control is required.  
- Impact assessment steps (product quality, patient safety, data integrity).  
- Approval matrix and implementation verification.

## 9. Risk Management
- Methodology (e.g., FMEA or equivalent).  
- Severity/Occurrence/Detection scales, RPN thresholds, and how risk informs testing depth and sampling.  
- Interfaces to CQV risk activities (ties into RA and protocol strategy).

## 10. Supplier & GxP Oversight
- Supplier qualification/approval.  
- Quality agreements and performance monitoring.  
- Audits, observations, follow‑up and closure.

## 11. Data Integrity & Computerized Systems
- ALCOA+ expectations, audit trails, time sync, backups.  
- CSV considerations and system categorization (reference relevant SOPs).

## 12. Health, Safety & Environment (HSE) Interface
- Interface points with HSE policies and permits where applicable.

## 13. CQV Interface (Relationship to VMP)
- This PQP governs the Validation Master Plan (VMP).  
- The CQV lifecycle is: URS → RA → RTM → DQ → IQ → OQ → PQ → VSR.  
- The VMP must reference this QP ID and comply with QP‑defined rules.

## 14. Quality Metrics & Management Review
- KPIs (e.g., deviation closure time, training compliance, audit findings).  
- Review cadence, attendees, inputs/outputs, and action tracking.

## 15. Records & Archival
- What records are generated under this QP.  
- Where records are stored under document control.  
- Retention and retrieval processes.

## 16. Appendices (Optional)
- A: SOP Map (IDs → processes)  
- B: Forms/Templates index (IDs)  
- C: Abbreviations

## 17. Document History
| Rev | Date | Summary of Changes | Author |
|---|---|---|---|
| 0.1 | [dd-mmm-yyyy] | Initial draft | Quality |

## 18. Approval Signatures
| Name | Title | Department | Date | Signature |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |

---

<a id="source-t1-VMP-template-v1-0-0-md"></a>
# Source: T1_VMP_Template_V1_0_0.md

## Template Metadata
- ID: T1
- Title: Validation Master Plan (VMP) Extract
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Validation Master Plan (VMP) Extract Template

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Validation Master Plan Extract (VMP Extract) |
| System/Equipment | No Entry |
| Location | No Entry |
| Document Number | VMP-EXT-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | Commissioning & Qualification (CQV) |
| Reviewed By | Quality Assurance (QA) |
| Approved By | Head of Quality / Site Manager |
| Validation Approach | Lifecycle, risk‑based |

## 1. Purpose and Scope
### 1.1 Purpose
Describe validation strategy, lifecycle approach, and documentation requirements aligned to corporate policies and regulatory guidelines.

### 1.2 Scope
Applies to the subject system/equipment at the specified facility. Outlines planned validation activities from URS through PQ; defines responsibilities; references applicable standards and procedures.

## 2. Validation Strategy
### 2.1 Lifecycle Approach
Adopt lifecycle methodology consistent with ASTM E2500 and EU GMP Annex 15: URS, DQ, IQ, OQ, PQ.

### 2.2 Risk Management
Employ risk‑based thinking throughout lifecycle. Conduct RA (e.g., FMEA) to identify failure modes, rate S/O/D, calculate RPN, define mitigation actions, and drive testing focus.

### 2.3 Documentation and Deliverables
Use standardized templates for URS, DQ, IQ, OQ, PQ, RA, RTM, VSR. Deviations are managed via site deviation/CAPA system.

## 3. Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| Project Manager | Timelines, resources, deliverables aligned with VMP extract |
| System/Process Owner | User and process requirements |
| CQV | Protocols, traceability, risk assessments |
| QA | Reviews/approves validation documents; ensures compliance |
| Engineering/Automation | Design/installation; support IQ/OQ execution |
| Production/Operations | PQ runs |
| QC | Analytical testing supporting PQ |

## 4. References
- Site Validation Master Plan (VMP)
- EU GMP Annex 15
- ASTM E2500
- ICH Q8/Q9/Q10
- Company SOPs

## 5. Document History
| Rev | Date | Summary of Changes | Author |
| --- | --- | --- | --- |
| 0.1 | dd-mm-yyyy | Initial draft issued | CQV |

## 6. Approval Signatures
| Name | Title | Department | Date | Signature |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

---

<a id="source-t2-cqv-department-questionnaires-v1-0-0-md"></a>
# Source: T2_CQV_Department_Questionnaires_V1_0_0.md

## Template Metadata
- ID: T2
- Title: CQV Department Questionnaires
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# CQV Department Questionnaires

## CQV-Engineering
| Field | Response | Requester | Date |
|:------------------------------------------------------------------|:-----------|:------------|:-------|
| Equipment/System Name & ID | | | |
| Manufacturer & Model | | | |
| Location / Line / Area | | | |
| Utilities Required (Power, Water, HVAC, etc.) | | | |
| Critical Process Parameters (CPPs) | | | |
| Critical Quality Attributes (CQAs) | | | |
| Capacity and Throughput Requirements | | | |
| Automation / Control System Type | | | |
| Calibration Requirements (Instruments & Frequency) | | | |
| Planned Validation Approach (# of PQ batches, FAT/SAT refs) | | | |
| Vendor Documentation References (Manuals, Drawings, Certificates) | | | |

## QA
| Field | Response | Requester | Date |
|:---------------------------------------------------------------|:-----------|:------------|:-------|
| Applicable Regulations (Annex 15, ICH Q9, ASTM E2500, etc.) | | | |
| Required Documentation Under Document Control | | | |
| Acceptance Criteria for Deviations | | | |
| Change Control Triggers | | | |
| Document Approval Matrix (Signatories) | | | |
| Archival Requirements (Duration, Location, GDP Rules) | | | |
| Risk Assessment Scoring System (Severity/Occurrence/Detection) | | | |
| Release Criteria for Validation Summary Report | | | |

## QC
| Field | Response | Requester | Date |
|:--------------------------------------------------------------------------|:-----------|:------------|:-------|
| Analytical Methods to be Validated (Assay, Impurities, Dissolution, etc.) | | | |
| Method Validation Status (Validated? ICH-compliant?) | | | |
| Swab/Rinse Test Methods for Cleaning Validation | | | |
| Acceptance Criteria for Cleaning Validation | | | |
| Sampling Plan for PQ (In-process Controls, QC Testing) | | | |
| Stability Study Requirements (Pull Points, Parameters, Chambers) | | | |
| OOS/OOT Handling Procedure | | | |

## Production
| Field | Response | Requester | Date |
|:----------------------------------------------------------------|:-----------|:------------|:-------|
| Equipment Operating Procedures (Start-up, Operation, Shut-down) | | | |
| Cleaning Procedures (Frequency, Agents, Methods) | | | |
| Maintenance Procedures (PM Schedule, Responsible Function) | | | |
| Operator Training Requirements | | | |
| Batch Sizes and Expected Throughput | | | |
| Materials Used (Product Contact Parts, Consumables, Packaging) | | | |
| Hold Times (Dirty Hold, Clean Hold) | | | |
| Documentation Practices (Logbooks, Electronic Batch Records) | | | |

## SHE
| Field | Response | Requester | Date |
|:---------------------------------------------------|:-----------|:------------|:-------|
| Applicable SHE Regulations (Local & International) | | | |
| Required SHE Documentation Under Document Control | | | |
| Acceptance Criteria for SHE Incidents / Deviations | | | |
| SHE Change Control Triggers | | | |
| SHE Approval Matrix (Signatories) | | | |
| SHE Training Requirements | | | |
| Risk Assessments (HIRA, JSA) | | | |
| Emergency Preparedness & Response | | | |
| Waste Management & Environmental Controls | | | |
| SHE Audits & Continuous Improvement | | | |

## Automation
| Field | Response | Requester | Date |
|:----------------------------------------------------------------------|:-----------|:------------|:-------|
| Applicable Automation Standards (GAMP 5, ISA-88, ISA-95, IEC 62443) | | | |
| Control System Architecture (DCS/PLC/SCADA breakdown) | | | |
| Automation URS Summary (user requirements specific to control) | | | |
| Functional & Design Specifications (FRS/DS) expectations | | | |
| Hardware Platform & I/O Count (PLC model, racks, expansion) | | | |
| Software Standards (naming conventions, libraries, versioning) | | | |
| Alarm Philosophy & Management (ISA-18.2 compliance) | | | |
| Data Integrity & Time Synchronization (ALCOA+, NTP, audit trails) | | | |
| Interfaces & Integration Points (MES, LIMS, ERP, historians) | | | |
| Cybersecurity Controls (accounts, hardening, patching, remote access) | | | |
| Access Control & User Management (roles, privileges, e-signatures) | | | |
| HMI/SCADA Design Guidelines (graphics, navigation, colors) | | | |
| Historian/Data Retention & Reporting (tags, compression, retention) | | | |
| Backup/Restore & Disaster Recovery (frequency, validation, offsite) | | | |
| Training & Competency (operators, maintenance, engineers) | | | |

---

<a id="source-t3-risk-assessment-template-v1-0-0-md"></a>
# Source: T3_Risk_Assessment_Template_V1_0_0.md

## Template Metadata
- ID: T3
- Title: Risk Assessment (FMEA)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Risk Assessment (FMEA)

**Project/Equipment:** [Insert]  
**Area/Line:** [Insert]  
**Document No.:** RA-XXX  
**Prepared by:** [CQV/Engineering]  
**Reviewed by:** [QA]  
**Approved by:** [Head QA/Production]  

## 1. Purpose
Identify and assess risks (failure modes) to GMP compliance and product quality.

## 2. Scope
Covers risks associated with design, installation, operation, and performance.

## 3. References
- ICH Q9 (Quality Risk Management)
- EU GMP Annex 15
- ISPE Risk-Based Guide

## 4. Risk Assessment Table
| Step/URS Ref | Requirement / Function | Failure Mode | Potential Effect | S (1-5) | O (1-5) | D (1-5) | RPN | Mitigation |
|--------------|------------------------|--------------|-----------------|---------|---------|---------|-----|------------|
| URS-001 | SS316L product contact | Material not compliant | Contamination risk | 5 | 2 | 2 | 20 | Vendor certificate + IQ check |
| URS-002 | Alarm recording | Alarm not timestamped | Data integrity failure | 4 | 3 | 3 | 36 | OQ test of audit trail |
| URS-003 | Capacity ≥ 100 kg | Insufficient throughput | Production delays | 3 | 2 | 3 | 18 | PQ execution with full batch |

## 5. Approval
Prepared by: ____ Date: ____  
Reviewed by: ____ Date: ____  
Approved by: ____ Date: ____  

---

<a id="source-t4-urs-template-v1-0-0-md"></a>
# Source: T4_URS_Template_V1_0_0.md

## Template Metadata
- ID: T4
- Title: User Requirements Specification (URS)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# User Requirements Specification (URS) Template

## Document Control
- Document Title: User Requirements Specification (URS)
- System/Equipment: [Insert name]
- Location: [Insert site/facility]
- Document Number: [Insert number]
- Version: [Insert version]
- Date: [Insert date]
- Status: [Draft/Approved]
- Prepared By: [Name / Department]
- Reviewed By: [Name / Department]
- Approved By: [Name / Department]
- Validation Approach: [Prospective / Concurrent / Retrospective]
- GAMP Category (if applicable): [Category 1–5]

## 1. Purpose and Scope
### 1.1 Purpose
Define the purpose of the system/equipment, including intended use and regulatory/business drivers.

### 1.2 Scope
- In Scope: [Main system functions, subsystems]
- Out of Scope: [Anything explicitly excluded]

## 2. Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| System Owner | Owns content & approvals |
| Process Owner | Confirms process fit |
| Automation/CSV | Ensures compliance with computerized systems |
| EHS/SHE | Confirms safety & sustainability inputs |
| Quality | Ensures compliance with GMP/QA |
| Project Manager | Oversees alignment with project goals |

## 3. System Description
- Overview: [Brief description of the system]
- Interfaces: [Upstream/Downstream systems]
- Main Functions: [High-level functional description]

## 4. Definitions & Abbreviations
List key terms, e.g.: CQA, CPP, DQ/IQ/OQ/PQ, etc.

## 5. Requirement Classification
- M = Mandatory
- B = Beneficial
- N = Nice-to-have

## 6. User Requirements — Functional
| URS Ref | Requirement | Priority (M/B/N) | Verification (DQ/IQ/OQ/PQ) |
|---------|-------------|------------------|-----------------------------|
| 6.1 | [System shall perform its core function reliably] | | |
| 6.2 | [System capacity/throughput requirements] | | |
| 6.3 | [Integration with related systems] | | |

## 7. User Requirements — Design & Materials
| URS Ref | Requirement | Priority | Verification |
|---------|-------------|----------|--------------|
| 7.1 | [Materials compatible with intended use] | | |
| 7.2 | [Surfaces smooth and cleanable] | | |
| 7.3 | [Non-reactive and non-shedding materials] | | |

## 8. User Requirements — Facility & Environment
| URS Ref | Requirement | Priority | Verification |
|---------|-------------|----------|--------------|
| 8.1 | [Operating temperature range] | | |
| 8.2 | [Relative humidity range] | | |
| 8.3 | [Cleanroom classification/environmental conditions] | | |

## 9. User Requirements — Utilities
| URS Ref | Utility | Requirement |
|---------|---------|-------------|
| 9.1 | Electrical | [Voltage, frequency, phases] |
| 9.2 | Air/Water | [Compressed air, cooling, vacuum] |
| 9.3 | Other | [List as needed] |

## 10. User Requirements — Computerized Systems
| URS Ref | Requirement |
|---------|-------------|
| 10.1 | [Compliance with 21 CFR Part 11, Annex 11] |
| 10.2 | [Audit trails, security, backup] |
| 10.3 | [User management and access controls] |

## 11. User Requirements — Safety, Health & Environment
| URS Ref | Requirement |
|---------|-------------|
| 11.1 | [Operator safety] |
| 11.2 | [Emergency stops and safety interlocks] |
| 11.3 | [Noise/vibration limits] |
| 11.4 | [Environmental impact] |

## 12. User Requirements — Maintenance & Support
| URS Ref | Requirement |
|---------|-------------|
| 12.1 | [Ease of maintenance and access] |
| 12.2 | [Spare parts availability] |
| 12.3 | [Training and manuals] |
| 12.4 | [Warranty and service agreements] |

## 13. Documentation Deliverables
- GA Drawings, Technical Datasheets, Manuals, Qualification Protocols, Certificates.

## 14. References
- ISPE Baseline Guide Vol.5, GAMP 5, ICH Q8/Q9/Q10, EU GMP Annex 15, ASTM E2500, local regulatory (e.g., EDA).

## 15. Traceability
- Define trace through design and testing. Reference RTM.

## 16. Risk Assessment
- Summary of initial RA, identification of critical requirements.

## 17. Acceptance Criteria
- Define general acceptance criteria for fit-for-use.

## 18. Document History
| Rev | Date | Summary of Changes | Author |
|-----|------|--------------------|--------|
| 0.1 | [dd-mmm-yyyy] | Draft issued | [Name/Role] |

## 19. Approval Signatures
| Name | Title | Department | Date | Signature |
|------|-------|------------|------|------------|
| | | | | |
| | | | | |
| | | | | |

---

<a id="source-t5-rtm-template-md"></a>
# Source: T5_RTM_Template.md

## Template Metadata
- ID: T5
- Title: Requirements Traceability Matrix (RTM)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# CQV Traceability Matrix Template
Ensures traceability of URS requirements through validation lifecycle (DQ, IQ, OQ, PQ, VSR).

| URS_ID | Requirement Description | Risk Assessment Ref | DQ Verification (Design Review) | IQ Verification (Installation) | OQ Verification (Operation) | PQ Verification (Performance) | VSR Reference | Release Decision |
|---------|-------------------------------|---------------------|---------------------------------|-------------------------------|-----------------------------|-------------------------------|----------------|-----------------|
| URS-XXX | [Enter requirement] | RA-XXX | [DQ method] | [IQ method] | [OQ method] | [PQ method] | [VSR] | Accepted/Rejected |
| URS-XXX | [Enter requirement] | RA-XXX | [DQ method] | [IQ method] | [OQ method] | [PQ method] | [VSR] | Accepted/Rejected |

---

<a id="source-t6-dq-template-v1-0-0-md"></a>
# Source: T6_DQ_Template_V1_0_0.md

## Template Metadata
- ID: T6
- Title: Design Qualification (DQ)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Design Qualification (DQ) Template

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Design Qualification (DQ) |
| System/Equipment | No Entry |
| Location | No Entry |
| Document Number | DQ-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | Engineering / CQV |
| Reviewed By | Quality Assurance |
| Approved By | Department Head |
| Validation Approach | Prospective |
| GAMP Category | Category 3 |

## Purpose and Scope
Verify proposed design meets URS and standards; review documentation, drawings, specs, and supplier responses.

## Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| System Owner | Ensures design meets business/process needs |
| Engineering | Collates design documentation and vendor responses |
| CQV | Reviews design for GMP and URS |
| Quality Assurance | Approves DQ and monitors quality standards |
| Supplier | Provides detailed design documentation and responses |

## Design Compliance Matrix
| URS ID | Requirement | Design Response | Compliance (Y/N) | Evidence/Comments |
| --- | --- | --- | --- | --- |
| URS-001 | [Describe requirement] | [Design solution] |  |  |
| URS-002 | [Describe requirement] | [Design solution] |  |  |

## Deviations & Resolutions
Document deviations and actions taken.

## References
- Approved URS
- EU GMP Annex 15
- ASTM E2500
- Company design guidelines

## Approval
Prepared by: ___ Date: ___  
Reviewed by: ___ Date: ___  
Approved by: ___ Date: ___

---

<a id="source-t7-iq-protocol-template-v1-0-0-md"></a>
# Source: T7_IQ_Protocol_Template_V1_0_0.md

## Template Metadata
- ID: T7
- Title: Installation Qualification (IQ) Protocol
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Installation Qualification (IQ) Protocol

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Installation Qualification (IQ) Protocol |
| System/Equipment | No Entry |
| Location / Line | No Entry |
| Document Number | IQP-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | CQV / Engineering |
| Reviewed By | Quality Assurance |
| Approved By | Department Head |
| Validation Approach | Prospective |

## Purpose and Scope
Verify installation per design/manufacturer recommendations/regulatory requirements. OQ covers operational testing.

## Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| CQV Engineer | Executes installation checks |
| Quality | Reviews IQ results |
| Engineering/Maintenance | Ensures compliant utilities/services |
| Supplier | Provides guidelines and certificates |

## References
- URS, DQ
- EU GMP Annex 15
- ASTM E2500

## Installation Checklist
| Item | Requirement | Verification Method | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Utilities | Connected per approved P&ID | Visual inspection |  |  |
| Materials of Construction | Compliant (e.g., SS316L) | Certificate review |  |  |
| Calibration Certificates | Instruments in date | Certificate review |  |  |
| Documentation | Manuals/drawings/spare parts list | Document review |  |  |

## Deviations
Describe non-conformances and corrective actions.

## Approval
Prepared by: ___ Date: ___  
Reviewed by: ___ Date: ___  
Approved by: ___ Date: ___

---

<a id="source-t8-oq-protocol-template-v1-0-0-md"></a>
# Source: T8_OQ_Protocol_Template_V1_0_0.md

## Template Metadata
- ID: T8
- Title: Operational Qualification (OQ) Protocol
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Operational Qualification (OQ) Protocol

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Operational Qualification (OQ) Protocol |
| System/Equipment | No Entry |
| Location / Line | No Entry |
| Document Number | OQP-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | CQV / Engineering |
| Reviewed By | Quality Assurance |
| Approved By | Department Head |
| Validation Approach | Prospective |

## Purpose and Scope
Verify operational performance across ranges; confirm critical functions, alarms, interlocks; ensure data integrity.

## Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| CQV Engineer | Executes OQ scripts and records results |
| Process Owner | Reviews parameters and accepts outcomes |
| Quality | Ensures compliance; approves deviations |
| Automation/CSV | Supports software testing and DI verification |

## References
- URS, DQ, IQ
- EU GMP Annex 15
- ASTM E2500

## Test Matrix
| Test ID | Objective | Method | Acceptance Criteria | Records |
| --- | --- | --- | --- | --- |
| OQ-001 | Verify alarm activation | Force alarm; monitor response | Alarm logs with correct timestamp | Event log capture |
| OQ-002 | Verify temperature control | Operate at setpoints across range | Maintain within ±2 °C of setpoint | Recorder printout |
| OQ-003 | Verify safety interlock | Attempt unsafe start | Prevented; warning displayed | Checklist |

## Deviations
Record deviations, impact, corrective actions.

## Approval
Prepared by: ___ Date: ___  
Reviewed by: ___ Date: ___  
Approved by: ___ Date: ___

---

<a id="source-t9-pq-protocol-template-v1-0-0-md"></a>
# Source: T9_PQ_Protocol_Template_V1_0_0.md

## Template Metadata
- ID: T9
- Title: Performance Qualification (PQ) Protocol
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Performance Qualification (PQ) Protocol

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Performance Qualification (PQ) Protocol |
| System/Equipment | No Entry |
| Location / Line | No Entry |
| Document Number | PQP-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | CQV |
| Reviewed By | QA / Production |
| Approved By | Department Head |
| Validation Approach | Prospective |

## Purpose and Scope
Demonstrate consistent performance under routine conditions; assess throughput, product quality, reproducibility.

## Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| CQV | Plans and executes PQ runs |
| Production | Operates equipment per batch records |
| QC | Conducts analytical testing |
| QA | Reviews PQ documentation; approves status |

## References
- URS, DQ, IQ, OQ
- Process validation master plan
- EU GMP Annex 15; ICH Q8/Q9/Q10

## Test Matrix
| Test ID | Objective | Method | Acceptance Criteria | Records |
| --- | --- | --- | --- | --- |
| PQ-001 | Verify throughput | Full-scale batch | ≥ target throughput within tolerance | Batch record |
| PQ-002 | Verify product quality | In-process and final QC | All within specifications | QC certificates |
| PQ-003 | Verify reproducibility | Three consecutive runs | No critical deviations; consistent results | VSR summary |

## Deviations
List deviations, impact, corrective actions.

## Approval
Prepared by: ___ Date: ___  
Reviewed by: ___ Date: ___  
Approved by: ___ Date: ___

---

<a id="source-t10-vsr-template-v1-0-0-md"></a>
# Source: T10_VSR_Template_V1_0_0.md

## Template Metadata
- ID: T10
- Title: Validation Summary Report (VSR)
- Version: V1.0.0
- Revision Date: dd-mm-yyyy

# Validation Summary Report (VSR) Template

## Document Control
| Item | Details |
| --- | --- |
| Document Title | Validation Summary Report (VSR) |
| System/Equipment | No Entry |
| Location | No Entry |
| Document Number | VSR-TBD |
| Version | 0.1 (Draft) |
| Date | dd-mm-yyyy |
| Status | Draft |
| Prepared By | Commissioning & Qualification (CQV) |
| Reviewed By | Quality Assurance (QA) |
| Approved By | Department Head / QA Manager |
| Validation Approach | Lifecycle, risk‑based |
| GAMP Category | Category 3–5 (as applicable) |

## 1. Purpose and Scope
Summarize URS, DQ, IQ, OQ, PQ outcomes; assess compliance, deviations/CAPAs, residual risks; support release decision.

## 2. Roles & Responsibilities
| Role | Responsibility |
| --- | --- |
| System/Process Owner | Confirms system meets requirements; authorizes release |
| CQV | Prepares VSR; collates data; assesses compliance |
| QA | Reviews/approves VSR; verifies deviations/CAPAs closure |
| Engineering/Automation | Provides design/install data; evaluates technical issues |
| Production/Operations | Executes PQ runs; verifies user acceptance |
| QC | Provides analytical data supporting PQ |

## 3. Validation Lifecycle Summary
- URS Compliance
- Design Qualification
- Installation Qualification
- Operational Qualification
- Performance Qualification

## 4. Risk Assessment and Mitigation
Summarize RA (e.g., FMEA), significant risks, RPN, mitigations, residual risk acceptance.

## 5. Deviations and Corrective Actions
List deviations across URS/DQ/IQ/OQ/PQ; root cause, impact, CAPA; closure status.

## 6. Conclusion and Recommendation
Overall evaluation of validation status; recommend qualified release or conditions.

## 7. References, Document History, Approval Signatures
List referenced documents; revision table; signatures.

---

<!-- Removed deprecated schema templates T11–T15. -->
