# EduVision_DV: Quality Assurance Checklist
**Project:** EduVision_DV (Higher Education Performance Dashboard)  
**Deliverable:** Module 7 - Quality Assurance Checklist  

| # | Item / Check | Category | Status | Notes |
| :---: | :--- | :--- | :---: | :--- |
| **1** | Raw dataset downloaded/simulated for QS and THE | Data Collection | [X] PASS | 7,520 records across 1,503 institutions (2020-2024) |
| **2** | Dataset completeness above 95% | Data Collection | [X] PASS | Initial completeness: 99.95% |
| **3** | Institutional and country duplicate elimination | Data Cleaning | [X] PASS | 0 duplicates in cleaned dataset |
| **4** | Institutional name standardization | Data Cleaning | [X] PASS | Standardized naming with acronym parentheticals |
| **5** | Country name and ISO-3 geocoding standardization | Data Cleaning | [X] PASS | Clean country names + ISO-3 codes for Tableau geocoding |
| **6** | Missing value imputation | Data Cleaning | [X] PASS | Final missing rate: 0.0000% (<2% requirement) |
| **7** | Metric normalization to [0, 100] scale | Data Cleaning | [X] PASS | All scores bounded and rounded to 1 decimal place |
| **8** | Global Ranking Score engineered | KPI Engineering | [X] PASS | Calibrated composite index; MIT #1 with 100.0 |
| **9** | Research Impact Score engineered | KPI Engineering | [X] PASS | Citation density metric; range [10.0, 100.0] |
| **10** | Faculty-to-Student Ratio engineered | KPI Engineering | [X] PASS | Display format '1:X.X'; global median 1:17.3 |
| **11** | International Student % engineered | KPI Engineering | [X] PASS | Diversity index; global mean ~28% |
| **12** | Academic Reputation Score engineered | KPI Engineering | [X] PASS | Global survey score calibrated |
| **13** | Research Productivity Index engineered | KPI Engineering | [X] PASS | Publications per faculty normalized 0-100 |
| **14** | University final dataset exported in Excel (.xlsx) | Deliverables | [X] PASS | Located at `data/university_final_dataset.xlsx` |
| **15** | Dashboard storyboard generated in PDF | Planning | [X] PASS | Located at `docs/dashboard_storyboard.pdf` |
| **16** | Prototype workbook generated (.twbx) | Development | [X] PASS | Located at `dashboard/eduvision_prototype.twbx` |
| **17** | Milestone 3 V1 dashboard workbook (.twbx) | Development | [X] PASS | Located at `dashboard/eduvision_dashboard_v1.twbx` |
| **18** | Final unified workbook generated (.twbx) | Integration | [X] PASS | Located at `dashboard/EduVision_DV.twbx` and root |
| **19** | University Overview dashboard complete | Dashboard | [X] PASS | Matches Page 10 wireframe and visual layout |
| **20** | Research Analytics dashboard complete | Dashboard | [X] PASS | Scatter quadrants, top citations, growth velocity |
| **21** | Student Analytics dashboard complete | Dashboard | [X] PASS | International student distribution, SFR correlations |
| **22** | Country Comparison dashboard complete | Dashboard | [X] PASS | Global choropleth map, scoreboard, macro radar |
| **23** | Interactive web dashboard twin generated | Visualization | [X] PASS | Located at `dashboard/index.html` & root |
| **24** | Comprehensive project documentation created | Documentation | [X] PASS | All methodology, dictionary, and guides complete |
| **25** | Git repository initialized with clean commits | Delivery | [X] PASS | Repository ready for deployment |
