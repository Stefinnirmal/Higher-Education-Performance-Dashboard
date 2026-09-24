# EduVision_DV: Key Performance Indicators (KPI) Definitions

This document details the mathematical formulations, data inputs, interpretations, and benchmarking thresholds for all performance metrics used across the **EduVision_DV** higher education dashboard suite.

---

## 1. Primary Core KPIs

### 1. Global Ranking Score (Composite Score)
* **Definition:** A normalized composite index measuring comprehensive institutional performance across academic quality, research impact, teaching capacity, employability, and sustainability.
* **Scale:** $0.0$ to $100.0$ (Higher is better).
* **Mathematical Formula:**
  $$\text{Global Ranking Score} = 0.30 \cdot S_{\text{acad}} + 0.25 \cdot S_{\text{impact}} + 0.15 \cdot S_{\text{faculty\_student}} + 0.15 \cdot S_{\text{employer}} + 0.10 \cdot S_{\text{intl\_outlook}} + 0.05 \cdot S_{\text{sustainability}}$$
  Where:
  - $S_{\text{acad}}$: Academic Reputation Score
  - $S_{\text{impact}}$: Research Impact Score
  - $S_{\text{faculty\_student}}$: Faculty-Student Ratio Score
  - $S_{\text{employer}}$: Employer Reputation Score
  - $S_{\text{intl\_outlook}}$: International Outlook Score
  - $S_{\text{sustainability}}$: Sustainability Score
* **Benchmark Tiers:**
  - **Tier 1 (World Class):** $\ge 90.0$ (e.g., MIT, Cambridge, Oxford, Harvard, Stanford)
  - **Tier 2 (High Excellence):** $80.0 - 89.9$
  - **Tier 3 (Very Competitive):** $70.0 - 79.9$
  - **Tier 4 (Competitive):** $60.0 - 69.9$
  - **Tier 5 (Developing):** $< 60.0$

---

### 2. Research Impact Score
* **Definition:** Evaluates the qualitative influence and citation velocity of an institution's scholarship per publication and per faculty member.
* **Scale:** $0.0$ to $100.0$.
* **Mathematical Formula:**
  $$\text{Research Impact Score} = \min\left(100.0, \, \left(\frac{\text{Citations}}{\text{Publications}}\right) \times 18.5 + \left(\text{Citations per Faculty}\right) \times 0.25\right)$$
* **Interpretation:** Mitigates sheer publication volume bias by rewarding institutional research that is cited heavily by global peers.

---

### 3. Faculty-to-Student Ratio (and Student-to-Faculty Ratio)
* **Definition:** Quantifies teaching resources and instructional mentorship bandwidth available per student.
* **Formulations:**
  - **Student-to-Faculty Ratio (Numeric):**
    $$\text{SFR} = \frac{\text{Total Students}}{\text{Academic Faculty Staff}}$$
  - **Faculty-to-Student Ratio (Ratio):**
    $$\text{FSR} = \frac{\text{Academic Faculty Staff}}{\text{Total Students}}$$
  - **Display String:** `"1 : " + str(round(SFR, 1))` (e.g., `1:17.3`).
* **Benchmarking Context:**
  - **World Elite (< 1:8):** Highly personalized tutorial/laboratory mentorship.
  - **Global Average (~ 1:17.3):** Balanced public research university ratio.
  - **High Enrollment (> 1:24):** Large lecture-hall structured environments.

---

### 4. International Student Percentage
* **Definition:** Measures campus cultural and geographic diversity as the proportion of matriculated international students relative to total student enrollment.
* **Scale:** $0.0\%$ to $100.0\%$.
* **Mathematical Formula:**
  $$\text{International Student \%} = \left(\frac{\text{International Students}}{\text{Total Students}}\right) \times 100$$
* **Benchmarking Context:**
  - **Global Cohort Average (2024):** $28.7\%$
  - **Oceania Average:** $\sim 39.5\%$ (high international recruitment)
  - **Europe Average:** $\sim 33.2\%$ (Erasmus and EU mobility)
  - **North America Average:** $\sim 27.5\%$
  - **Asia Average:** $\sim 18.5\%$

---

### 5. Academic Reputation Score
* **Definition:** Standardized peer-review rating evaluating global scholarly esteem, research prestige, and institutional pedigree based on responses from surveyed academics globally.
* **Scale:** $0.0$ to $100.0$.
* **Source Foundation:** Calibrated using QS World University Rankings Academic Survey and Times Higher Education Academic Reputation indicators.

---

### 6. Research Productivity Index
* **Definition:** Standardized metric assessing the research output volume generated per faculty member, normalized against 95th percentile global benchmarks.
* **Scale:** $0.0$ to $100.0$.
* **Mathematical Formula:**
  $$\text{Research Productivity Index} = \min\left(100.0, \, \left(\frac{\text{Publications Count} / \text{Academic Staff}}{P_{95}}\right) \times 85.0\right)$$
  Where $P_{95} = 35.0$ papers per faculty member over the 5-year observation window.

---

## 2. Year-over-Year (YoY) Differential Metrics

1. **Overall Score YoY Change ($\Delta$ Score):**
   $$\Delta \text{Score}_{t} = \text{Score}_{t} - \text{Score}_{t-1}$$
   *(Global 2024 Benchmark: $\Delta = +2.4$ vs 2023)*
2. **International Student \% YoY Change ($\Delta$ Intl \%):**
   $$\Delta \text{Intl\%}_{t} = \text{Intl\%}_{t} - \text{Intl\%}_{t-1}$$
   *(Global 2024 Benchmark: $\Delta = +1.8\%$ vs 2023)*
3. **Faculty Ratio YoY Change ($\Delta$ SFR):**
   $$\Delta \text{SFR}_{t} = \text{SFR}_{t} - \text{SFR}_{t-1}$$
   *(Global 2024 Benchmark: $\Delta = +0.6$ vs 2023)*
4. **Publications YoY Growth Rate ($\% \Delta$ Pubs):**
   $$\% \Delta \text{Pubs}_{t} = \left(\frac{\text{Pubs}_{t} - \text{Pubs}_{t-1}}{\text{Pubs}_{t-1}}\right) \times 100$$
   *(Global 2024 Benchmark: $+6.3\%$ vs 2023)*
