# EduVision_DV: Dashboard User Guide & Interaction Manual

Welcome to the **EduVision_DV** Higher Education Performance Dashboard suite. This interactive system provides institutional leaders, analysts, researchers, and students with deep multidimensional visibility into global university excellence.

The deliverable is packaged as a unified Tableau Workbook (`EduVision_DV.twbx`) and mirrored via an interactive web twin (`dashboard/index.html`).

---

## 1. Global Navigation & Layout Architecture

The suite consists of **four unified dashboards** organized logically from macro institutional performance down to national system benchmarking:

```
[ EduVision DV Master Header ]
--------------------------------------------------------------------------------------
[ Navigation Sidebar ] | [ Top 6 Primary KPI Summary Cards                          ]
- University Overview  |--------------------------------------------------------------
- Research Analytics   | [ Mid Row: Rankings Table | 5-Yr Trend Line | Regional Donut]
- Student Analytics    |--------------------------------------------------------------
- Country Comparison   | [ Bottom: Top 5 Pubs Bar | Intl % Heatmap | Faculty Ratio   ]
```

### Navigation Controls:
* **Sidebar Menu / Header Nav:** Click any view name (**Overview**, **Research Analytics**, **Student Analytics**, or **Country Comparison**) to immediately switch viewports.
* **Top Ribbon Filters:** Quickly adjust reporting parameters (**Year**, **Region**, **Country**, and **Subject Area**).
* **Reset Filters Button:** Located on the sidebar; clears all active filters back to global 2024 defaults with a single click.

---

## 2. Dashboard 1: University Overview

### Visual Layout & Components:
1. **Top 6 KPI Summary Cards:**
   * **Top Global Ranking:** Displays current #1 ranked institution (MIT) with parenthetical designation.
   * **Total Universities:** Total volume of institutions meeting active filter criteria (Global Total: 1,503).
   * **Avg. Overall Score:** Mean score across cohort (2024 Global: 72.6, showing $\Delta +2.4$ vs 2023).
   * **International Students %:** Cohort average international enrollment share (2024 Global: 28.7%, $\Delta +1.8\%$).
   * **Faculty Ratio:** Student-to-faculty density (2024 Global: 1:17.3, $\Delta +0.6$).
   * **Total Publications:** Aggregated scholarship volume (2024 Global: 2.45M, $+6.3\%$).

2. **Top 10 Universities by Global Ranking (Interactive Table):**
   * Displays Rank, Institution Name, Country, and Overall Score bar.
   * **Interaction:** Clicking any row highlights that institution across all other charts on the dashboard.

3. **Top 10 Universities by Overall Score Trend (5-Year Line Chart):**
   * Multi-series line plot tracking score trajectories from 2020 through 2024 for MIT, Cambridge, Oxford, Harvard, Stanford.
   * **Tooltip:** Hovering reveals exact annual score, YoY delta, and rank progression.

4. **Universities by Region (Interactive Donut Chart):**
   * Visualizes regional representation:
     * Europe: $37.6\%$ (565 institutions)
     * North America: $28.3\%$ (425 institutions)
     * Asia: $24.8\%$ (373 institutions)
     * Oceania: $6.1\%$ (92 institutions)
     * South America: $3.2\%$ (48 institutions)
   * **Interaction:** Clicking a donut segment filters the entire dashboard to universities in that region.

5. **Publications by Top 5 Universities (Horizontal Bar Chart):**
   * Displays high-volume publication output for Harvard (208K), Stanford (189K), MIT (186K), Oxford (163K), Cambridge (150K).

6. **International Students % by Region (Heatmap / Choropleth Map):**
   * Color-graded visual depicting regional international student density ranging from $10\%$ to $45\%$.

7. **Faculty to Student Ratio by Region (Comparative Bars):**
   * Highlights regional teaching resource benchmarks: North America (1:21.0), Europe (1:17.8), Asia (1:15.5), Oceania (1:14.5), South America (1:12.8).

---

## 3. Dashboard 2: Research Analytics

Designed for Chief Research Officers and grant committees:
* **Research Impact vs Productivity Quadrant:** Scatter plot mapping Research Productivity Index ($X$) against Research Impact Score ($Y$).
  * *Top-Right Quadrant:* High volume, high citation influence (MIT, Harvard, Oxford).
  * *Top-Left Quadrant:* Specialized high-impact research (Caltech, Princeton).
* **Top 20 Global Research Institutions by Citations:** Lollipop/Bar chart displaying aggregate citation influence.
* **5-Year Growth Velocity:** Dual-axis chart contrasting annual paper production against citation acceleration.

---

## 4. Dashboard 3: Student Analytics

Designed for Enrollment Management and Diversity Officers:
* **International Student Distribution by Country:** Box-plot and strip-chart visual detailing distribution extremes (UK and Australia leading at $>40\%$).
* **Faculty-to-Student Ratio vs Global Ranking Score:** Evaluates whether small class sizes directly associate with higher global prestige.
* **Enrollment Capacity vs International Density:** Bubble treemap where bubble area represents total student body and saturation denotes international share.

---

## 5. Dashboard 4: Country Comparison

Designed for National Policymakers and Higher Education Ministries:
* **Global Education Excellence Map:** Country-level choropleth map shaded by average institutional score.
* **Country Performance Scoreboard:** Comparative scorecard ranking nations by:
  1. Average Institutional Score
  2. Number of Ranked Universities
  3. Top 100 University Count
  4. Average Citations per Paper
* **Regional Radar Benchmark:** Hexagonal radar profile benchmarking continents across all 6 core KPIs.

---

## 6. How to Open in Tableau

1. **Tableau Desktop / Tableau Public:**
   * Open Tableau Desktop or Tableau Public (version 2020.4 or newer).
   * Go to **File $\rightarrow$ Open** and select `EduVision_DV.twbx` (or `dashboard/EduVision_DV.twbx`).
   * The workbook will automatically load the packaged data extract and present the **University Overview** dashboard.
2. **Instant Web Twin Preview:**
   * Double-click `EduVision_Dashboard.html` or open `dashboard/index.html` in Chrome, Edge, Firefox, or Safari.
   * All filters, calculations, charts, and tabs work live in the browser without requiring Tableau installation.
