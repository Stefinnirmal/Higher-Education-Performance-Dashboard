# EduVision_DV: Data Dictionary & Column Specifications

This data dictionary documents the complete schema for `data/university_final_dataset.xlsx` and `data/university_final_dataset.csv`.

---

## Column Specifications

| # | Column Name | Data Type | Domain / Range | Description | Example |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | `university_id` | String | `UNIV_000000`–`999999` | Unique institutional identification code | `UNIV_482910` |
| **2** | `university_name` | String | Text | Original raw university institution name | `University of Cambridge` |
| **3** | `university_name_standardized` | String | Text | Cleaned, standardized institution title | `University of Cambridge` |
| **4** | `country` | String | Text | Original country string | `United Kingdom` |
| **5** | `country_clean` | String | Text | Standardized country name | `UK` |
| **6** | `country_iso_code` | String | 3-char ISO-3166 | ISO-3 country code for Tableau geocoding | `GBR` |
| **7** | `region` | Categorical | 5 Regions | Geographic continent / world region | `Europe` |
| **8** | `year` | Integer | `2020` – `2024` | Academic reporting year | `2024` |
| **9** | `subject_area` | Categorical | 5 Domains | Primary academic discipline cluster | `Engineering & Technology` |
| **10** | `total_students` | Integer | $8,000$ – $50,000$ | Total enrolled student body | `24,500` |
| **11** | `international_students` | Integer | $500$ – $25,000$ | Number of international students | `9,432` |
| **12** | `academic_staff` | Integer | $500$ – $8,000$ | Full-time academic faculty and research staff | `5,444` |
| **13** | `student_faculty_ratio` | Float | $1.0$ – $60.0$ | Number of students per academic staff member | `4.5` |
| **14** | `faculty_to_student_ratio` | Float | $0.01$ – $0.50$ | Inverted ratio (faculty staff per student) | `0.2222` |
| **15** | `faculty_ratio_display` | String | `'1:X.X'` | Formatted string for Tableau cards | `'1 : 4.5'` |
| **16** | `international_student_pct` | Float | $0.0\%$ – $100.0\%$ | International students as percentage of total | `38.5%` |
| **17** | `publications_count` | Integer | $400$ – $250,000$ | Volume of peer-reviewed research publications | `150,812` |
| **18** | `citations_count` | Integer | $2,000$ – $1,200,000$ | Total scholarly citations received | `710,000` |
| **19** | `citations_per_publication` | Float | $1.0$ – $15.0$ | Average citations per research article | `4.71` |
| **20** | `citations_per_faculty` | Float | $10.0$ – $100.0$ | Citations per faculty member score | `85.4` |
| **21** | `academic_reputation_score` | Float | $0.0$ – $100.0$ | Peer academic survey standing score | `99.8` |
| **22** | `employer_reputation_score` | Float | $0.0$ – $100.0$ | Employer survey and graduate employability | `99.2` |
| **23** | `faculty_student_score` | Float | $0.0$ – $100.0$ | Normalized teaching capacity score | `88.5` |
| **24** | `research_impact_score` | Float | $0.0$ – $100.0$ | Citation velocity and qualitative impact | `95.3` |
| **25** | `research_productivity_index`| Float | $0.0$ – $100.0$ | Publication output per faculty index | `82.4` |
| **26** | `global_ranking_score` | Float | $0.0$ – $100.0$ | Composite overall institutional score | `98.7` |
| **27** | `rank` | Integer | $1$ – $1,503$ | Global rank within specific academic year | `2` |
| **28** | `rank_tier` | Categorical | 6 Tiers | Tier bracket (Top 10, Top 11-50, etc.) | `Top 10` |
| **29** | `score_bracket` | Categorical | 5 Brackets | Score grouping for drill-downs | `90-100 (World Class)` |
| **30** | `score_yoy_change` | Float | $\pm 10.0$ | Year-over-year overall score difference | `+0.8` |
| **31** | `intl_pct_yoy_change` | Float | $\pm 5.0\%$ | YoY change in international student share | `+0.5%` |
| **32** | `sfr_yoy_change` | Float | $\pm 2.0$ | YoY change in student-faculty ratio | `-0.1` |
| **33** | `pubs_yoy_pct_change` | Float | $\pm 25.0\%$ | YoY percentage growth in publication volume | `+5.8%` |
| **34** | `sustainability_score` | Float | $0.0$ – $100.0$ | Social and environmental impact score | `94.2` |
| **35** | `employment_outcomes_score` | Float | $0.0$ – $100.0$ | Graduate employment success score | `96.0` |
| **36** | `the_teaching_score` | Float | $0.0$ – $100.0$ | Times Higher Education teaching score | `94.0` |
| **37** | `the_research_environment` | Float | $0.0$ – $100.0$ | Research income and peer prestige | `98.0` |
| **38** | `the_research_quality` | Float | $0.0$ – $100.0$ | Citation density and field-weighted impact | `95.0` |
| **39** | `the_industry_score` | Float | $0.0$ – $100.0$ | Industry income and patent citations | `88.0` |
| **40** | `the_international_outlook` | Float | $0.0$ – $100.0$ | Staff, student, and co-authorship diversity | `95.5` |
| **41** | `source_qs` | String | Constant | Identifier for QS dataset lineage | `QS World University Rankings` |
| **42** | `source_the` | String | Constant | Identifier for THE dataset lineage | `Times Higher Education Rankings` |
