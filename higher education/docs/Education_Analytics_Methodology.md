# EduVision_DV: Education Analytics Methodology

This document outlines the end-to-end data analytics methodology, statistical pipelines, integration schemas, and normalization formulas utilized in the development of the **EduVision_DV (Higher Education Performance Dashboard)** suite.

---

## 1. Data Foundation & Source Integration

The analytics pipeline integrates empirical indicators from two preeminent global ranking frameworks:
1. **QS World University Rankings (Quacquarelli Symonds):**
   * Emphasizes academic reputation, employer reputation, citations per faculty, faculty/student ratio, international student ratio, and sustainability.
2. **Times Higher Education (THE) World University Rankings:**
   * Emphasizes teaching environment, research environment, research quality (citation impact), industry engagement, and international outlook.

### Panel Architecture:
* **Temporal Horizon:** 5 Academic Years ($2020, 2021, 2022, 2023, 2024$).
* **Institutional Population:** $1,503$ distinct universities across $42$ nations.
* **Total Observation Records:** $7,520$ institution-year observations.
* **Regional Cohort Distribution:**
  * **Europe:** $37.6\%$ ($565$ universities)
  * **North America:** $28.3\%$ ($425$ universities)
  * **Asia:** $24.8\%$ ($373$ universities)
  * **Oceania:** $6.1\%$ ($92$ universities)
  * **South America:** $3.2\%$ ($48$ universities)

---

## 2. Data Cleaning & Transformation Pipeline

### A. Deduplication
Institutional records are verified against composite primary keys `(university_id, year)` and `(university_name_standardized, year)` to ensure zero duplicate entries exist.

### B. Entity & Name Standardization
* Institutional naming discrepancies are resolved using canonical lookup tables (e.g., standardizing "Massachusetts Institute of Technology" to `"MIT (Massachusetts Institute of Technology)"`, "UCL" to `"UCL (University College London)"`).
* Country names are mapped to standardized 3-letter **ISO 3166-1 alpha-3** codes (`USA`, `GBR`, `CHE`, `SGP`, `AUS`, `CAN`, etc.) enabling instant, error-free geographic plotting within Tableau's native geocoding engine.

### C. Missing Value Imputation
* **Requirement:** Overall dataset missingness must remain strictly below $2.0\%$.
* **Methodology:** Imputation is performed using hierarchical regional-year median estimation:
  $$\hat{x}_{i,r,t} = \text{Median}\left(\{ x_{j,r,t} \mid \text{Region}(j) = r, \, \text{Year}(j) = t, \, x_{j,r,t} \text{ observed} \}\right)$$
* **Outcome:** Cleaned dataset achieved **0.0000% missing values** across all $33$ features.

---

## 3. Indicator Normalization & Mathematical Scoring

To synthesize multi-source indicators onto unified comparative scales, indicators are normalized onto bounded continuous intervals $[0, 100]$.

### A. Global Ranking Score Formulation
The composite institutional score is formulated as a multi-criteria weighted linear combination:
$$\text{Global Score} = \sum_{k=1}^{6} w_k \cdot I_k$$

Where:
* $I_1$ (Academic Reputation): $w_1 = 0.30$
* $I_2$ (Research Impact Score): $w_2 = 0.25$
* $I_3$ (Faculty-to-Student Ratio Score): $w_3 = 0.15$
* $I_4$ (Employer Reputation): $w_4 = 0.15$
* $I_5$ (International Outlook): $w_5 = 0.10$
* $I_6$ (Sustainability Score): $w_6 = 0.05$

### B. Research Productivity Index Formulation
Publication counts are scaled by academic staff size and calibrated against the 95th percentile benchmark ($P_{95} = 35.0$):
$$\text{Productivity Index} = \text{clip}\left(\left(\frac{\text{Publications} / \text{Academic Staff}}{P_{95}}\right) \times 85.0, \, 0.0, \, 100.0\right)$$

### C. Research Impact Score Formulation
Citations per publication are combined with citations per faculty member:
$$\text{Impact Score} = \min\left(100.0, \, \left(\frac{\text{Citations}}{\text{Publications}}\right) \times 18.5 + \left(\text{Citations per Faculty}\right) \times 0.25\right)$$

---

## 4. Tableau Workbook Architecture & Optimization

1. **Denormalized Flat Table Schema:**
   The output `university_final_dataset.xlsx` and `university_final_dataset.csv` are formatted in a denormalized single-table star schema. This eliminates complex joins inside Tableau, resulting in sub-second query rendering even when switching heavy global filters.
2. **Pre-Engineered Display Dimensions:**
   Measures such as `student_faculty_ratio` are pre-formatted alongside clean categorical bins (`rank_tier`, `score_bracket`, `faculty_ratio_display`) so Tableau displays concise human-readable card values without requiring expensive runtime string concatenations.
3. **Packaging Strategy:**
   Packaged as `.twbx` containing embedded CSV and Excel files, guaranteeing 100% portability when transferred across client operating systems, Tableau Server, or Tableau Public.
