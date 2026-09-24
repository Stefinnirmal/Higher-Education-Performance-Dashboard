"""
EduVision_DV - Higher Education Performance Analytics
Build Interactive Web-Based Dashboard Mirror & Demonstration App
File: scripts/build_interactive_dashboard_html.py

Description:
Creates `dashboard/index.html` (and project root `EduVision_Dashboard.html`),
providing an interactive, pixel-perfect digital twin of the EduVision DV dashboard
depicted on Page 10 of the project specification.
Embeds data directly, supports live filtering (Year, Region, Country, Subject Area),
navigation tabs (Overview, Research Analytics, Student Analytics, Country Comparison),
and interactive Chart.js visualizations.
"""

import os
import json
import shutil
import pandas as pd

def build_dashboard_html():
    csv_path = os.path.join("data", "university_final_dataset.csv")
    df = pd.read_csv(csv_path)
    
    # Extract dataset subset for fast client-side filtering
    records = df[[
        "rank", "university_name_standardized", "country_clean", "region", "year",
        "subject_area", "global_ranking_score", "academic_reputation_score",
        "research_impact_score", "student_faculty_ratio", "international_student_pct",
        "publications_count", "citations_count", "faculty_ratio_display"
    ]].to_dict(orient="records")
    
    data_json = json.dumps(records)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduVision DV | Higher Education Performance Dashboard</title>
    <!-- Chart.js and FontAwesome -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        :root {{
            --bg-base: #0c0517;
            --bg-sidebar: #130924;
            --bg-card: #1c0e35;
            --bg-card-hover: #26134b;
            --accent-purple: #845ec2;
            --accent-teal: #00c9a7;
            --accent-pink: #d65db1;
            --accent-orange: #ff9671;
            --accent-gold: #ffc75f;
            --accent-blue: #2c73d2;
            --text-main: #f1f1f5;
            --text-muted: #9e93b8;
            --border-color: #2b184d;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        /* TOP NAVIGATION HEADER */
        .top-navbar {{
            background: linear-gradient(90deg, #170b2e 0%, #110724 100%);
            border-bottom: 1px solid var(--border-color);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .brand-container {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-icon {{
            background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
            width: 38px;
            height: 38px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: #fff;
            box-shadow: 0 4px 12px rgba(132, 94, 194, 0.4);
        }}

        .brand-text h1 {{
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .brand-text h1 span {{
            font-size: 0.8rem;
            background: rgba(132, 94, 194, 0.2);
            color: #d1b8ff;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 500;
        }}

        .brand-text p {{
            font-size: 0.72rem;
            color: var(--text-muted);
        }}

        .top-controls {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .header-filter {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .header-filter label {{
            font-size: 0.68rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
        }}

        .header-filter select {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            cursor: pointer;
            outline: none;
        }}

        .header-filter select:focus {{
            border-color: var(--accent-purple);
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-left: 20px;
            border-left: 1px solid var(--border-color);
            padding-left: 20px;
        }}

        .nav-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 0.85rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 10px;
            border-radius: 6px;
            transition: all 0.2s;
        }}

        .nav-btn:hover, .nav-btn.active {{
            color: #fff;
            background: rgba(255, 255, 255, 0.08);
        }}

        /* APP LAYOUT */
        .app-body {{
            display: flex;
            flex: 1;
        }}

        /* LEFT SIDEBAR */
        .sidebar {{
            width: 240px;
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            padding: 20px 16px;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}

        .sidebar-section-title {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 10px;
            font-weight: 600;
        }}

        .sidebar-menu {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .menu-item {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 14px;
            border-radius: 8px;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 0.88rem;
            font-weight: 500;
            transition: all 0.2s;
        }}

        .menu-item:hover {{
            background-color: rgba(255, 255, 255, 0.05);
            color: #fff;
        }}

        .menu-item.active {{
            background: linear-gradient(90deg, rgba(132, 94, 194, 0.25) 0%, rgba(132, 94, 194, 0.08) 100%);
            color: #fff;
            border-left: 3px solid var(--accent-purple);
        }}

        .sidebar-filters {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .filter-group {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .filter-group label {{
            font-size: 0.75rem;
            color: var(--text-muted);
        }}

        .filter-group select {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 8px 10px;
            border-radius: 6px;
            font-size: 0.82rem;
            outline: none;
            width: 100%;
        }}

        .reset-btn {{
            margin-top: 10px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 8px;
            border-radius: 6px;
            font-size: 0.82rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.2s;
        }}

        .reset-btn:hover {{
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
        }}

        /* MAIN CONTENT AREA */
        .main-content {{
            flex: 1;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            overflow-y: auto;
        }}

        /* KPI SUMMARY CARDS */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 14px;
        }}

        .kpi-card {{
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 14px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: relative;
            overflow: hidden;
        }}

        .kpi-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
        }}

        .kpi-card.c-purple::before {{ background: var(--accent-purple); }}
        .kpi-card.c-blue::before {{ background: var(--accent-blue); }}
        .kpi-card.c-teal::before {{ background: var(--accent-teal); }}
        .kpi-card.c-orange::before {{ background: var(--accent-orange); }}
        .kpi-card.c-pink::before {{ background: var(--accent-pink); }}
        .kpi-card.c-gold::before {{ background: var(--accent-gold); }}

        .kpi-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .kpi-title {{
            font-size: 0.72rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
        }}

        .kpi-icon {{
            font-size: 0.95rem;
            opacity: 0.85;
        }}

        .kpi-value {{
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
            line-height: 1.1;
        }}

        .kpi-subtext {{
            font-size: 0.72rem;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .badge-delta {{
            font-size: 0.7rem;
            font-weight: 600;
            color: var(--accent-teal);
            display: inline-flex;
            align-items: center;
            gap: 2px;
        }}

        /* CHART GRID LAYOUTS */
        .chart-row {{
            display: grid;
            gap: 16px;
        }}

        .row-3-cols {{
            grid-template-columns: 1.35fr 1.15fr 0.95fr;
        }}

        .row-bottom {{
            grid-template-columns: 1.1fr 1.1fr 0.8fr;
        }}

        .chart-card {{
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            min-height: 290px;
        }}

        .chart-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .chart-title {{
            font-size: 0.88rem;
            font-weight: 600;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .chart-badge {{
            font-size: 0.68rem;
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-muted);
            padding: 2px 6px;
            border-radius: 4px;
        }}

        .chart-body {{
            flex: 1;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* TOP 10 RANKINGS TABLE */
        .rank-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.78rem;
        }}

        .rank-table th {{
            text-align: left;
            padding: 6px 8px;
            color: var(--text-muted);
            font-size: 0.68rem;
            text-transform: uppercase;
            border-bottom: 1px solid var(--border-color);
        }}

        .rank-table td {{
            padding: 6px 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            vertical-align: middle;
        }}

        .rank-table tr:hover td {{
            background-color: rgba(255, 255, 255, 0.03);
        }}

        .rank-badge {{
            width: 20px;
            height: 20px;
            border-radius: 4px;
            background: rgba(132, 94, 194, 0.2);
            color: var(--accent-purple);
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.72rem;
        }}

        .score-bar-container {{
            width: 65px;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
            display: inline-block;
            vertical-align: middle;
            margin-right: 6px;
        }}

        .score-bar {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-teal), var(--accent-blue));
            border-radius: 3px;
        }}

        /* FOOTER */
        .footer-banner {{
            border-top: 1px solid var(--border-color);
            padding: 12px 24px;
            font-size: 0.72rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bg-sidebar);
        }}

        /* TAB PANES */
        .tab-pane {{
            display: none;
            flex-direction: column;
            gap: 20px;
        }}

        .tab-pane.active {{
            display: flex;
        }}
    </style>
</head>
<body>

    <!-- TOP NAVBAR -->
    <header class="top-navbar">
        <div class="brand-container">
            <div class="brand-icon">
                <i class="fa-solid fa-graduation-cap"></i>
            </div>
            <div class="brand-text">
                <h1>EduVision DV <span>Tableau Suite</span></h1>
                <p>Higher Education Performance Dashboard • QS &amp; Times Higher Education Analytics</p>
            </div>
        </div>

        <div class="top-controls">
            <div class="header-filter">
                <label>Year</label>
                <select id="topYearFilter" onchange="onFilterChange('year', this.value)">
                    <option value="2024" selected>2024</option>
                    <option value="2023">2023</option>
                    <option value="2022">2022</option>
                    <option value="2021">2021</option>
                    <option value="2020">2020</option>
                </select>
            </div>
            <div class="header-filter">
                <label>Region</label>
                <select id="topRegionFilter" onchange="onFilterChange('region', this.value)">
                    <option value="All" selected>(All)</option>
                    <option value="Europe">Europe</option>
                    <option value="North America">North America</option>
                    <option value="Asia">Asia</option>
                    <option value="Oceania">Oceania</option>
                    <option value="South America">South America</option>
                </select>
            </div>
            <div class="header-filter">
                <label>Country</label>
                <select id="topCountryFilter" onchange="onFilterChange('country', this.value)">
                    <option value="All" selected>(All)</option>
                    <option value="USA">USA</option>
                    <option value="UK">UK</option>
                    <option value="Switzerland">Switzerland</option>
                    <option value="Singapore">Singapore</option>
                    <option value="Australia">Australia</option>
                    <option value="Canada">Canada</option>
                    <option value="China">China</option>
                    <option value="Japan">Japan</option>
                </select>
            </div>
            <div class="header-filter">
                <label>Subject Area</label>
                <select id="topSubjectFilter" onchange="onFilterChange('subject', this.value)">
                    <option value="All" selected>(All)</option>
                    <option value="Engineering & Technology">Engineering &amp; Technology</option>
                    <option value="Natural Sciences">Natural Sciences</option>
                    <option value="Life Sciences & Medicine">Life Sciences &amp; Medicine</option>
                    <option value="Arts & Humanities">Arts &amp; Humanities</option>
                    <option value="Social Sciences & Management">Social Sciences</option>
                </select>
            </div>

            <nav class="nav-links">
                <button class="nav-btn active" onclick="switchTab('overview')"><i class="fa-solid fa-house"></i> Home</button>
                <button class="nav-btn" onclick="switchTab('overview')"><i class="fa-solid fa-table-columns"></i> Dashboard</button>
                <button class="nav-btn" onclick="alert('EduVision_DV: Comprehensive Higher Education Performance Dashboard. Packaged in EduVision_DV.twbx.')"><i class="fa-solid fa-circle-info"></i> About</button>
            </nav>
        </div>
    </header>

    <div class="app-body">
        <!-- SIDEBAR -->
        <aside class="sidebar">
            <div>
                <div class="sidebar-section-title">Navigation Views</div>
                <ul class="sidebar-menu">
                    <li class="menu-item active" id="menu-overview" onclick="switchTab('overview')">
                        <i class="fa-solid fa-chart-pie" style="color: var(--accent-purple);"></i> Overview
                    </li>
                    <li class="menu-item" id="menu-research" onclick="switchTab('research')">
                        <i class="fa-solid fa-flask" style="color: var(--accent-teal);"></i> Research Analytics
                    </li>
                    <li class="menu-item" id="menu-student" onclick="switchTab('student')">
                        <i class="fa-solid fa-users" style="color: var(--accent-orange);"></i> Student Analytics
                    </li>
                    <li class="menu-item" id="menu-country" onclick="switchTab('country')">
                        <i class="fa-solid fa-earth-americas" style="color: var(--accent-blue);"></i> Country Comparison
                    </li>
                </ul>
            </div>

            <div class="sidebar-filters">
                <div class="sidebar-section-title">Interactive Filters</div>
                <div class="filter-group">
                    <label>Year</label>
                    <select id="sideYear" onchange="syncFilters('year', this.value)">
                        <option value="2024" selected>2024</option>
                        <option value="2023">2023</option>
                        <option value="2022">2022</option>
                        <option value="2021">2021</option>
                        <option value="2020">2020</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Region</label>
                    <select id="sideRegion" onchange="syncFilters('region', this.value)">
                        <option value="All" selected>(All)</option>
                        <option value="Europe">Europe</option>
                        <option value="North America">North America</option>
                        <option value="Asia">Asia</option>
                        <option value="Oceania">Oceania</option>
                        <option value="South America">South America</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Country</label>
                    <select id="sideCountry" onchange="syncFilters('country', this.value)">
                        <option value="All" selected>(All)</option>
                        <option value="USA">USA</option>
                        <option value="UK">UK</option>
                        <option value="Switzerland">Switzerland</option>
                        <option value="Singapore">Singapore</option>
                        <option value="Australia">Australia</option>
                        <option value="Canada">Canada</option>
                        <option value="China">China</option>
                        <option value="Japan">Japan</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Subject Area</label>
                    <select id="sideSubject" onchange="syncFilters('subject', this.value)">
                        <option value="All" selected>(All)</option>
                        <option value="Engineering & Technology">Engineering &amp; Technology</option>
                        <option value="Natural Sciences">Natural Sciences</option>
                        <option value="Life Sciences & Medicine">Life Sciences &amp; Medicine</option>
                        <option value="Arts & Humanities">Arts &amp; Humanities</option>
                        <option value="Social Sciences & Management">Social Sciences</option>
                    </select>
                </div>

                <button class="reset-btn" onclick="resetAllFilters()">
                    <i class="fa-solid fa-arrows-rotate"></i> Reset Filters
                </button>
            </div>
        </aside>

        <!-- MAIN VIEWPORTS -->
        <main class="main-content">

            <!-- TAB 1: UNIVERSITY OVERVIEW -->
            <div id="tab-overview" class="tab-pane active">
                
                <!-- 6 PRIMARY KPI CARDS -->
                <div class="kpi-grid">
                    <div class="kpi-card c-purple">
                        <div class="kpi-header">
                            <span class="kpi-title">Top Global Ranking</span>
                            <i class="fa-solid fa-trophy kpi-icon" style="color: var(--accent-purple);"></i>
                        </div>
                        <div class="kpi-value" id="kpiTopRank">#1 MIT</div>
                        <div class="kpi-subtext" id="kpiTopSub">Massachusetts Institute of Technology</div>
                    </div>

                    <div class="kpi-card c-blue">
                        <div class="kpi-header">
                            <span class="kpi-title">Total Universities</span>
                            <i class="fa-solid fa-building-columns kpi-icon" style="color: var(--accent-blue);"></i>
                        </div>
                        <div class="kpi-value" id="kpiTotalUnis">1,503</div>
                        <div class="kpi-subtext">Ranked Institutions Worldwide</div>
                    </div>

                    <div class="kpi-card c-teal">
                        <div class="kpi-header">
                            <span class="kpi-title">Avg. Overall Score</span>
                            <i class="fa-solid fa-chart-line kpi-icon" style="color: var(--accent-teal);"></i>
                        </div>
                        <div class="kpi-value" id="kpiAvgScore">72.6</div>
                        <div class="kpi-subtext"><span class="badge-delta">▲ 2.4</span> vs 2023</div>
                    </div>

                    <div class="kpi-card c-orange">
                        <div class="kpi-header">
                            <span class="kpi-title">International Students %</span>
                            <i class="fa-solid fa-globe kpi-icon" style="color: var(--accent-orange);"></i>
                        </div>
                        <div class="kpi-value" id="kpiIntlPct">28.7%</div>
                        <div class="kpi-subtext"><span class="badge-delta">▲ 1.8%</span> vs 2023</div>
                    </div>

                    <div class="kpi-card c-pink">
                        <div class="kpi-header">
                            <span class="kpi-title">Faculty Ratio</span>
                            <i class="fa-solid fa-user-group kpi-icon" style="color: var(--accent-pink);"></i>
                        </div>
                        <div class="kpi-value" id="kpiFacultyRatio">1 : 17.3</div>
                        <div class="kpi-subtext"><span class="badge-delta">▲ 0.6</span> vs 2023</div>
                    </div>

                    <div class="kpi-card c-gold">
                        <div class="kpi-header">
                            <span class="kpi-title">Total Publications</span>
                            <i class="fa-solid fa-book-open kpi-icon" style="color: var(--accent-gold);"></i>
                        </div>
                        <div class="kpi-value" id="kpiTotalPubs">2.45M</div>
                        <div class="kpi-subtext"><span class="badge-delta">▲ 6.3%</span> vs 2023</div>
                    </div>
                </div>

                <!-- MIDDLE VISUALIZATIONS ROW -->
                <div class="chart-row row-3-cols">
                    <!-- Top 10 Table -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-list-ol" style="color: var(--accent-purple);"></i> Top 10 Universities by Global Ranking</span>
                            <span class="chart-badge" id="tableFilterTag">2024 Global</span>
                        </div>
                        <div class="chart-body" style="align-items: flex-start; overflow-y: auto;">
                            <table class="rank-table" id="topRankTable">
                                <thead>
                                    <tr>
                                        <th>Rank</th>
                                        <th>University</th>
                                        <th>Country</th>
                                        <th>Score</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- Populated dynamically -->
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- 5-Year Trend Line -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-arrow-trend-up" style="color: var(--accent-teal);"></i> Top 10 Universities by Overall Score Trend</span>
                            <span class="chart-badge">2020 - 2024</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="trendChart"></canvas>
                        </div>
                    </div>

                    <!-- Regional Donut Chart -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-chart-pie" style="color: var(--accent-gold);"></i> Universities by Region</span>
                            <span class="chart-badge" id="totalUnisTag">1,503 Total</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="regionDonutChart"></canvas>
                        </div>
                    </div>
                </div>

                <!-- BOTTOM VISUALIZATIONS ROW -->
                <div class="chart-row row-bottom">
                    <!-- Top 5 Publications Bar Chart -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-chart-column" style="color: var(--accent-blue);"></i> Publications by Top 5 Universities</span>
                            <span class="chart-badge">Volume</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="pubsBarChart"></canvas>
                        </div>
                    </div>

                    <!-- International Students % by Region Map / Bars -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-earth-americas" style="color: var(--accent-orange);"></i> International Students % by Region</span>
                            <span class="chart-badge">Regional Benchmarks</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="intlRegionChart"></canvas>
                        </div>
                    </div>

                    <!-- Faculty to Student Ratio by Region -->
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-users-rectangle" style="color: var(--accent-pink);"></i> Faculty to Student Ratio by Region</span>
                            <span class="chart-badge">Student/Faculty</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="sfrRegionChart"></canvas>
                        </div>
                    </div>
                </div>

            </div>

            <!-- TAB 2: RESEARCH ANALYTICS -->
            <div id="tab-research" class="tab-pane">
                <div class="chart-row" style="grid-template-columns: 1fr 1fr;">
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-atom" style="color: var(--accent-teal);"></i> Research Impact Score vs Productivity Index</span>
                            <span class="chart-badge">Quadrant Analysis</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="researchScatterChart"></canvas>
                        </div>
                    </div>
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-award" style="color: var(--accent-purple);"></i> Top 10 Research Institutions by Citations</span>
                            <span class="chart-badge">Citations Count</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="citationsLeaderChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: STUDENT ANALYTICS -->
            <div id="tab-student" class="tab-pane">
                <div class="chart-row" style="grid-template-columns: 1fr 1fr;">
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-passport" style="color: var(--accent-orange);"></i> International Student Percentage Distribution</span>
                            <span class="chart-badge">Country Benchmarking</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="studentDistChart"></canvas>
                        </div>
                    </div>
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-scale-balanced" style="color: var(--accent-pink);"></i> Faculty-to-Student Ratio vs Global Ranking Score</span>
                            <span class="chart-badge">Scatter Correlation</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="sfrScoreChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 4: COUNTRY COMPARISON -->
            <div id="tab-country" class="tab-pane">
                <div class="chart-row" style="grid-template-columns: 1.2fr 0.8fr;">
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-flag" style="color: var(--accent-blue);"></i> Country Performance Scoreboard (Top 10 Nations)</span>
                            <span class="chart-badge">Avg Overall Score</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="countryScoreboardChart"></canvas>
                        </div>
                    </div>
                    <div class="chart-card">
                        <div class="chart-header">
                            <span class="chart-title"><i class="fa-solid fa-compass" style="color: var(--accent-gold);"></i> Regional Excellence Summary</span>
                            <span class="chart-badge">Summary</span>
                        </div>
                        <div class="chart-body">
                            <canvas id="regionalSummaryChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- FOOTER -->
    <footer class="footer-banner">
        <div>
            <b>Source:</b> QS World University Rankings 2024 &bull; Times Higher Education World University Rankings 2024
        </div>
        <div>
            <b>Note:</b> All metrics are for 2024 unless otherwise selected in filters. Workbook deliverable: <code>EduVision_DV.twbx</code>
        </div>
    </footer>

    <!-- INLINE DATA & INTERACTION LOGIC -->
    <script>
        const rawDataset = {data_json};

        let currentFilters = {{
            year: 2024,
            region: "All",
            country: "All",
            subject: "All"
        }};

        // Charts handles
        let trendChartInst = null;
        let regionDonutInst = null;
        let pubsBarInst = null;
        let intlRegionInst = null;
        let sfrRegionInst = null;
        let researchScatterInst = null;
        let citationsLeaderInst = null;
        let studentDistInst = null;
        let sfrScoreInst = null;
        let countryScoreboardInst = null;
        let regionalSummaryInst = null;

        function getFilteredData() {{
            return rawDataset.filter(d => {{
                if (d.year != currentFilters.year) return false;
                if (currentFilters.region !== "All" && d.region !== currentFilters.region) return false;
                if (currentFilters.country !== "All" && d.country_clean !== currentFilters.country) return false;
                if (currentFilters.subject !== "All" && d.subject_area !== currentFilters.subject) return false;
                return true;
            }});
        }}

        function updateOverview() {{
            const filtered = getFilteredData();
            
            // 1. Update KPI Cards
            if (filtered.length > 0) {{
                const sortedByRank = [...filtered].sort((a,b) => a.rank - b.rank);
                const top1 = sortedByRank[0];
                document.getElementById("kpiTopRank").innerText = `#${{top1.rank}} ${{top1.university_name_standardized.split('(')[0].trim()}}`;
                document.getElementById("kpiTopSub").innerText = top1.university_name_standardized;

                document.getElementById("kpiTotalUnis").innerText = filtered.length.toLocaleString();
                
                const avgScore = (filtered.reduce((sum, d) => sum + d.global_ranking_score, 0) / filtered.length).toFixed(1);
                document.getElementById("kpiAvgScore").innerText = avgScore;

                const avgIntl = (filtered.reduce((sum, d) => sum + d.international_student_pct, 0) / filtered.length).toFixed(1);
                document.getElementById("kpiIntlPct").innerText = `${{avgIntl}}%`;

                const avgSfr = (filtered.reduce((sum, d) => sum + d.student_faculty_ratio, 0) / filtered.length).toFixed(1);
                document.getElementById("kpiFacultyRatio").innerText = `1 : ${{avgSfr}}`;

                const totalPubs = (filtered.reduce((sum, d) => sum + d.publications_count, 0) / 1000000).toFixed(2);
                document.getElementById("kpiTotalPubs").innerText = `${{totalPubs}}M`;

                // Update Table
                const tbody = document.querySelector("#topRankTable tbody");
                tbody.innerHTML = "";
                const top10 = sortedByRank.slice(0, 10);
                top10.forEach(u => {{
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td><span class="rank-badge">${{u.rank}}</span></td>
                        <td style="font-weight: 600; color: #fff;">${{u.university_name_standardized}}</td>
                        <td><span style="color: var(--text-muted);">${{u.country_clean}}</span></td>
                        <td>
                            <div class="score-bar-container"><div class="score-bar" style="width: ${{u.global_ranking_score}}%;"></div></div>
                            <span style="font-weight: 700; color: var(--accent-teal);">${{u.global_ranking_score.toFixed(1)}}</span>
                        </td>
                    `;
                    tbody.appendChild(tr);
                }});
            }}

            updateCharts();
        }}

        function updateCharts() {{
            // 1. Score Trend Line Chart (Top 5 institutions over 2020-2024)
            const top5Names = [
                "MIT (Massachusetts Institute of Technology)",
                "University of Cambridge",
                "University of Oxford",
                "Harvard University",
                "Stanford University"
            ];
            const years = [2020, 2021, 2022, 2023, 2024];
            const colorPalette = ["#845ec2", "#00c9a7", "#ff9671", "#ffc75f", "#d65db1"];

            const trendDatasets = top5Names.map((name, idx) => {{
                const univData = rawDataset.filter(d => d.university_name_standardized === name);
                const points = years.map(y => {{
                    const match = univData.find(d => d.year === y);
                    return match ? match.global_ranking_score : null;
                }});
                return {{
                    label: name.split('(')[0].trim(),
                    data: points,
                    borderColor: colorPalette[idx],
                    backgroundColor: colorPalette[idx],
                    tension: 0.3,
                    pointRadius: 4
                }};
            }});

            if (trendChartInst) trendChartInst.destroy();
            trendChartInst = new Chart(document.getElementById("trendChart"), {{
                type: 'line',
                data: {{ labels: years, datasets: trendDatasets }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'top', labels: {{ color: '#c7bedb', boxWidth: 10, font: {{ size: 10 }} }} }}
                    }},
                    scales: {{
                        y: {{ min: 88, max: 101, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8' }} }},
                        x: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8' }} }}
                    }}
                }}
            }});

            // 2. Universities by Region Donut
            const filtered = getFilteredData();
            const regCounts = {{}};
            filtered.forEach(d => {{ regCounts[d.region] = (regCounts[d.region] || 0) + 1; }});
            const regLabels = Object.keys(regCounts);
            const regData = Object.values(regCounts);

            if (regionDonutInst) regionDonutInst.destroy();
            regionDonutInst = new Chart(document.getElementById("regionDonutChart"), {{
                type: 'doughnut',
                data: {{
                    labels: regLabels,
                    datasets: [{{
                        data: regData,
                        backgroundColor: ["#845ec2", "#00c9a7", "#ff9671", "#2c73d2", "#ffc75f"],
                        borderWidth: 2,
                        borderColor: '#1c0e35'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '68%',
                    plugins: {{
                        legend: {{ position: 'right', labels: {{ color: '#c7bedb', boxWidth: 10, font: {{ size: 9 }} }} }}
                    }}
                }}
            }});

            // 3. Publications Top 5 Horizontal Bars
            const top5Pubs = [...filtered].sort((a,b) => b.publications_count - a.publications_count).slice(0, 5);
            if (pubsBarInst) pubsBarInst.destroy();
            pubsBarInst = new Chart(document.getElementById("pubsBarChart"), {{
                type: 'bar',
                data: {{
                    labels: top5Pubs.map(d => d.university_name_standardized.split('(')[0].trim()),
                    datasets: [{{
                        label: 'Publications',
                        data: top5Pubs.map(d => d.publications_count),
                        backgroundColor: '#00c9a7',
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        x: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8', callback: v => (v/1000) + 'K' }} }},
                        y: {{ grid: {{ display: false }}, ticks: {{ color: '#ffffff', font: {{ size: 9 }} }} }}
                    }}
                }}
            }});

            // 4. International % by Region
            const regIntl = {{}};
            regLabels.forEach(r => {{
                const items = filtered.filter(d => d.region === r);
                regIntl[r] = (items.reduce((s, d) => s + d.international_student_pct, 0) / items.length).toFixed(1);
            }});

            if (intlRegionInst) intlRegionInst.destroy();
            intlRegionInst = new Chart(document.getElementById("intlRegionChart"), {{
                type: 'bar',
                data: {{
                    labels: regLabels,
                    datasets: [{{
                        label: 'Intl %',
                        data: Object.values(regIntl),
                        backgroundColor: '#ff9671',
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        y: {{ max: 50, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8', callback: v => v + '%' }} }},
                        x: {{ grid: {{ display: false }}, ticks: {{ color: '#ffffff', font: {{ size: 9 }} }} }}
                    }}
                }}
            }});

            // 5. Faculty Ratio by Region
            const regSfr = {{}};
            regLabels.forEach(r => {{
                const items = filtered.filter(d => d.region === r);
                regSfr[r] = (items.reduce((s, d) => s + d.student_faculty_ratio, 0) / items.length).toFixed(1);
            }});

            if (sfrRegionInst) sfrRegionInst.destroy();
            sfrRegionInst = new Chart(document.getElementById("sfrRegionChart"), {{
                type: 'bar',
                data: {{
                    labels: regLabels,
                    datasets: [{{
                        label: 'Faculty Ratio (1:X)',
                        data: Object.values(regSfr),
                        backgroundColor: '#d65db1',
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        y: {{ max: 30, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8', callback: v => '1:' + v }} }},
                        x: {{ grid: {{ display: false }}, ticks: {{ color: '#ffffff', font: {{ size: 9 }} }} }}
                    }}
                }}
            }});

            // 6. Research Analytics Scatter Plot
            if (document.getElementById("researchScatterChart")) {{
                if (researchScatterInst) researchScatterInst.destroy();
                const scatterPoints = filtered.slice(0, 150).map(d => ({{
                    x: d.academic_reputation_score,
                    y: d.research_impact_score
                }}));
                researchScatterInst = new Chart(document.getElementById("researchScatterChart"), {{
                    type: 'scatter',
                    data: {{
                        datasets: [{{
                            label: 'Institutions',
                            data: scatterPoints,
                            backgroundColor: 'rgba(0, 201, 167, 0.6)',
                            borderColor: '#00c9a7'
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{ legend: {{ display: false }} }},
                        scales: {{
                            x: {{ title: {{ display: true, text: 'Academic Reputation Score', color: '#9e93b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8' }} }},
                            y: {{ title: {{ display: true, text: 'Research Impact Score', color: '#9e93b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8' }} }}
                        }}
                    }}
                }});
            }}

            // 7. Top Citations Leaderboard
            if (document.getElementById("citationsLeaderChart")) {{
                if (citationsLeaderInst) citationsLeaderInst.destroy();
                const topCits = [...filtered].sort((a,b) => b.citations_count - a.citations_count).slice(0, 8);
                citationsLeaderInst = new Chart(document.getElementById("citationsLeaderChart"), {{
                    type: 'bar',
                    data: {{
                        labels: topCits.map(d => d.university_name_standardized.split('(')[0].trim()),
                        datasets: [{{
                            label: 'Total Citations',
                            data: topCits.map(d => d.citations_count),
                            backgroundColor: '#845ec2',
                            borderRadius: 4
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{ legend: {{ display: false }} }},
                        scales: {{
                            y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8', callback: v => (v/1000) + 'K' }} }},
                            x: {{ grid: {{ display: false }}, ticks: {{ color: '#ffffff', font: {{ size: 8 }} }} }}
                        }}
                    }}
                }});
            }}

            // 8. Country Scoreboard
            if (document.getElementById("countryScoreboardChart")) {{
                if (countryScoreboardInst) countryScoreboardInst.destroy();
                const countryScores = {{}};
                filtered.forEach(d => {{
                    if (!countryScores[d.country_clean]) countryScores[d.country_clean] = [];
                    countryScores[d.country_clean].push(d.global_ranking_score);
                }});
                const sortedCountries = Object.keys(countryScores)
                    .map(c => ({{ country: c, avg: countryScores[c].reduce((a,b)=>a+b,0)/countryScores[c].length }}))
                    .sort((a,b) => b.avg - a.avg).slice(0, 8);

                countryScoreboardInst = new Chart(document.getElementById("countryScoreboardChart"), {{
                    type: 'bar',
                    data: {{
                        labels: sortedCountries.map(c => c.country),
                        datasets: [{{
                            label: 'Avg Score',
                            data: sortedCountries.map(c => c.avg.toFixed(1)),
                            backgroundColor: '#2c73d2',
                            borderRadius: 4
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{ legend: {{ display: false }} }},
                        scales: {{
                            y: {{ min: 50, max: 100, grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9e93b8' }} }},
                            x: {{ grid: {{ display: false }}, ticks: {{ color: '#ffffff', font: {{ size: 9 }} }} }}
                        }}
                    }}
                }});
            }}
        }}

        function onFilterChange(type, val) {{
            currentFilters[type] = (type === 'year') ? parseInt(val) : val;
            syncSelects(type, val);
            updateOverview();
        }}

        function syncFilters(type, val) {{
            currentFilters[type] = (type === 'year') ? parseInt(val) : val;
            syncSelects(type, val);
            updateOverview();
        }}

        function syncSelects(type, val) {{
            const topMap = {{ year: 'topYearFilter', region: 'topRegionFilter', country: 'topCountryFilter', subject: 'topSubjectFilter' }};
            const sideMap = {{ year: 'sideYear', region: 'sideRegion', country: 'sideCountry', subject: 'sideSubject' }};
            if (document.getElementById(topMap[type])) document.getElementById(topMap[type]).value = val;
            if (document.getElementById(sideMap[type])) document.getElementById(sideMap[type]).value = val;
        }}

        function resetAllFilters() {{
            currentFilters = {{ year: 2024, region: 'All', country: 'All', subject: 'All' }};
            ['year', 'region', 'country', 'subject'].forEach(t => syncSelects(t, currentFilters[t]));
            updateOverview();
        }}

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.menu-item').forEach(el => el.classList.remove('active'));
            
            const targetPane = document.getElementById('tab-' + tabId);
            const targetMenu = document.getElementById('menu-' + tabId);
            if (targetPane) targetPane.classList.add('active');
            if (targetMenu) targetMenu.classList.add('active');

            setTimeout(() => {{
                updateCharts();
            }}, 50);
        }}

        // Initial render
        window.addEventListener('DOMContentLoaded', () => {{
            updateOverview();
        }});
    </script>
</body>
</html>
"""
    # Write to dashboard/index.html and project root index.html
    target_dashboard_html = os.path.join("dashboard", "index.html")
    with open(target_dashboard_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    shutil.copy(target_dashboard_html, "EduVision_Dashboard.html")
    print(f"[SUCCESS] Interactive Web Dashboard generated:")
    print(f"1. {target_dashboard_html}")
    print(f"2. EduVision_Dashboard.html (root)")

if __name__ == "__main__":
    build_dashboard_html()
