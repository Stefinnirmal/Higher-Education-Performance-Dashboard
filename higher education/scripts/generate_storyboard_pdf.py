"""
EduVision_DV - Higher Education Performance Analytics
Module 4: Dashboard Planning & Storyboard Generation
File: scripts/generate_storyboard_pdf.py

Description:
Generates the comprehensive multi-page dashboard storyboard and wireframe architecture
deliverable `docs/dashboard_storyboard.pdf` using ReportLab.
Covers all four dashboards:
1. University Overview
2. Research Analytics
3. Student Analytics
4. Country Comparison
Includes UI component wireframes, interaction rules, filter architectures, and design tokens.
"""

import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_storyboard():
    os.makedirs("docs", exist_ok=True)
    pdf_path = os.path.join("docs", "dashboard_storyboard.pdf")
    
    # 11 x 8.5 inches landscape for presentation storyboard
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Brand Styles (Dark Purple / Deep Slate Theme matching EduVision DV mockup)
    primary_color = colors.HexColor("#1A0933")
    accent_purple = colors.HexColor("#7952B3")
    accent_teal = colors.HexColor("#00C9A7")
    accent_gold = colors.HexColor("#FFC75F")
    dark_bg = colors.HexColor("#0D061A")
    card_bg = colors.HexColor("#F4F6F9")
    text_dark = colors.HexColor("#2C3E50")
    
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#555555"),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=primary_color,
        spaceBefore=0,
        spaceAfter=8
    )
    
    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=accent_purple,
        spaceBefore=6,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=text_dark
    )
    
    body_bold = ParagraphStyle(
        "Body_Bold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=12,
        textColor=text_dark
    )

    story = []

    # -------------------------------------------------------------
    # PAGE 1: EXECUTIVE STORYBOARD & ARCHITECTURE OVERVIEW
    # -------------------------------------------------------------
    story.append(Paragraph("EduVision_DV: Higher Education Performance Dashboard", title_style))
    story.append(Paragraph("Unified Tableau Dashboard Suite Storyboard, Layout Wireframes & Interaction Matrix", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=accent_purple, spaceAfter=12))

    meta_data = [
        [Paragraph("<b>Project Scope:</b> Higher Education Analytics (1,503 Global Universities)", body_style),
         Paragraph("<b>Target Audience:</b> University Leadership, Researchers, Policy Analysts", body_style)],
        [Paragraph("<b>Data Sources:</b> QS World University Rankings & THE Rankings (2020–2024)", body_style),
         Paragraph("<b>Workbook Deliverable:</b> EduVision_DV.twbx (Tableau 2023+)", body_style)],
        [Paragraph("<b>Color Palette:</b> Dark Theme (Deep Royal Purple, Vibrant Teal, Coral, Gold)", body_style),
         Paragraph("<b>Interaction Engine:</b> Global Filter Hierarchy & Dynamic Parameters", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[360, 360])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0EDF6")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 1, accent_purple),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Executive Dashboard Navigation Architecture", h2_style))
    arch_data = [
        [Paragraph("<b>Dashboard 1: University Overview</b>", body_bold),
         Paragraph("<b>Dashboard 2: Research Analytics</b>", body_bold),
         Paragraph("<b>Dashboard 3: Student Analytics</b>", body_bold),
         Paragraph("<b>Dashboard 4: Country Comparison</b>", body_bold)],
        [
            Paragraph("• Top Global Ranking Table<br/>• 6 Primary KPI Summary Cards<br/>• Overall Score 5-Yr Trend Line<br/>• Universities by Region Donut<br/>• Publications Top 5 Bar Chart<br/>• Regional International % Map<br/>• Faculty Ratio by Region Bars", body_style),
            Paragraph("• Total Publications Distribution<br/>• Citations per Faculty vs Score<br/>• Research Impact Score Quadrant<br/>• Top 20 Research Institutions<br/>• Citations Velocity YoY Trend<br/>• Subject Area Productivity Radar", body_style),
            Paragraph("• International Student % by Region<br/>• Student-to-Faculty Ratio Dist.<br/>• Total Enrollment Comparisons<br/>• Gender Diversity (Female/Male)<br/>• Regional Student Mobility Flows<br/>• Academic Staff vs Student Growth", body_style),
            Paragraph("• Country Rankings Benchmark<br/>• Global Education Index Map<br/>• Average Overall Score by Country<br/>• High-Performing Nations Matrix<br/>• Cross-Country KPI Comparison<br/>• Regional Trajectory Benchmarks", body_style)
        ]
    ]
    arch_table = Table(arch_data, colWidths=[180, 180, 180, 180])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#EAE4F2")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#E3F7F3")),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor("#FFF4E5")),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor("#E8F0FE")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(arch_table)
    story.append(PageBreak())

    # -------------------------------------------------------------
    # PAGE 2: DASHBOARD 1 - UNIVERSITY OVERVIEW WIREFRAME
    # -------------------------------------------------------------
    story.append(Paragraph("Dashboard 1 Wireframe: University Overview", h1_style))
    story.append(Paragraph("Replicates the exact master wireframe layout specified in the EduVision DV specification (Page 10).", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent_purple, spaceAfter=8))

    wireframe_d1 = [
        [Paragraph("<b>EduVision DV</b> | Higher Education Performance Dashboard", body_bold),
         Paragraph("<b>Year:</b> [ 2024 ▼ ]  <b>Region:</b> [ (All) ▼ ]  <b>Country:</b> [ (All) ▼ ]  <b>Subject:</b> [ (All) ▼ ]", body_style),
         Paragraph("<b>Nav:</b> [ Home ] [ Dashboard ] [ About ]", body_style)],
        [
            Paragraph("<b>Navigation Sidebar:</b><br/><br/><b>[X] Overview</b><br/>[ ] Research Analytics<br/>[ ] Student Analytics<br/>[ ] Country Comparison<br/><br/><b>Filters:</b><br/>• Year: 2024<br/>• Region: (All)<br/>• Country: (All)<br/>• Subject: (All)<br/><br/><i>[ Reset Filters ]</i>", body_style),
            Paragraph("""
            <b>Top 6 KPI Summary Cards:</b><br/>
            [ #1 MIT | Top Global Ranking ]  [ 1,503 | Ranked Universities ]  [ 72.6 | Avg Overall Score (+2.4) ]<br/>
            [ 28.7% | Intl Students (+1.8%) ]  [ 1:17.3 | Faculty Ratio (+0.6) ]  [ 2.45M | Publications (+6.3%) ]<br/><br/>
            <b>Middle Visualizations:</b><br/>
            • <i>Left:</i> <b>Top 10 Universities Global Ranking Table</b> (Rank, University, Country, Overall Score)<br/>
            • <i>Center:</i> <b>5-Year Overall Score Trend Line</b> (MIT, Cambridge, Oxford, Harvard, Stanford: 2020-2024)<br/>
            • <i>Right:</i> <b>Universities by Region Donut</b> (Europe 37.6%, North America 28.3%, Asia 24.8%, Oceania 6.1%, South America 3.2%)<br/><br/>
            <b>Bottom Visualizations:</b><br/>
            • <i>Left:</i> <b>Publications by Top 5 Universities</b> (Horizontal Bar: Harvard 208K, Stanford 189K, MIT 186K, Oxford 163K, Cambridge 150K)<br/>
            • <i>Center:</i> <b>International Students % by Region Heatmap / Choropleth Map</b> (10% - 45%)<br/>
            • <i>Right:</i> <b>Faculty to Student Ratio by Region Bars</b> (North America 1:21, Europe 1:18, Asia 1:16, Oceania 1:15, South America 1:13)
            """, body_style),
            Paragraph("<b>Interactive Elements:</b><br/>• Click university to cross-filter trends<br/>• Click donut slice to filter entire view to that Region<br/>• Hover tooltip shows detailed KPI radar breakdown<br/>• Reset button restores all initial states", body_style)
        ]
    ]
    table_d1 = Table(wireframe_d1, colWidths=[200, 370, 150])
    table_d1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A0933")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#2B154A")),
        ('TEXTCOLOR', (0,1), (0,1), colors.HexColor("#EAE4F2")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (2,1), (2,1), colors.HexColor("#F8F9FA")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(table_d1)
    story.append(PageBreak())

    # -------------------------------------------------------------
    # PAGE 3: DASHBOARD 2 - RESEARCH ANALYTICS WIREFRAME
    # -------------------------------------------------------------
    story.append(Paragraph("Dashboard 2 Wireframe: Research Analytics", h1_style))
    story.append(Paragraph("In-depth evaluation of publications volume, citation impact, researcher productivity, and academic reputation.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent_teal, spaceAfter=8))

    wireframe_d2 = [
        [Paragraph("<b>EduVision DV</b> | Research & Citation Performance Suite", body_bold),
         Paragraph("<b>Year:</b> [ 2024 ▼ ]  <b>Subject Area:</b> [ Engineering & Technology ▼ ]", body_style),
         Paragraph("<b>View:</b> Research Analytics", body_style)],
        [
            Paragraph("<b>KPI Banners:</b><br/>• Total Research Papers: 2.45M<br/>• Avg Citations/Faculty: 58.4<br/>• Avg Citations/Paper: 4.8<br/>• Research Impact Score: 78.2<br/><br/><b>Navigation:</b><br/>[ ] Overview<br/><b>[X] Research Analytics</b><br/>[ ] Student Analytics<br/>[ ] Country Comparison", body_style),
            Paragraph("""
            <b>Main Analytics Panels:</b><br/><br/>
            <b>1. Research Impact vs Productivity Scatter Quadrant (X: Productivity Index, Y: Impact Score)</b><br/>
            - <i>High Impact, High Volume (Top Right):</i> Flagship global powerhouses (MIT, Harvard, Cambridge)<br/>
            - <i>High Impact, Specialized (Top Left):</i> Elite niche research institutes (Caltech, Princeton)<br/>
            - Bubble size represents Total Citations; color denotes Region.<br/><br/>
            <b>2. Top 20 Global Institutions by Citations Count (Lollipop Chart)</b><br/>
            - Ranks institutions by citation volume with color coding by Academic Reputation Score.<br/><br/>
            <b>3. 5-Year Publications & Citations Growth Velocity (Dual-Axis Area Chart)</b><br/>
            - Tracks year-over-year annual publication output (bars) against cumulative citation count (line).
            """, body_style),
            Paragraph("<b>Research Insights:</b><br/>• Research Impact Score heavily drives Global Rank ($r=0.88$).<br/>• Engineering & Technology accounts for highest annual citation velocity.<br/>• North America & Europe generate 65.9% of total global publications.", body_style)
        ]
    ]
    table_d2 = Table(wireframe_d2, colWidths=[200, 370, 150])
    table_d2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0D47A1")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#E3F2FD")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (2,1), (2,1), colors.HexColor("#F8F9FA")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(table_d2)
    story.append(PageBreak())

    # -------------------------------------------------------------
    # PAGE 4: DASHBOARD 3 - STUDENT ANALYTICS WIREFRAME
    # -------------------------------------------------------------
    story.append(Paragraph("Dashboard 3 Wireframe: Student Analytics", h1_style))
    story.append(Paragraph("Deep dive into international student diversity, faculty-to-student ratios, and campus capacity benchmarks.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent_gold, spaceAfter=8))

    wireframe_d3 = [
        [Paragraph("<b>EduVision DV</b> | Student Analytics & Diversity Dashboard", body_bold),
         Paragraph("<b>Year:</b> [ 2024 ▼ ]  <b>Region:</b> [ (All) ▼ ]", body_style),
         Paragraph("<b>View:</b> Student Analytics", body_style)],
        [
            Paragraph("<b>KPI Banners:</b><br/>• Global Intl Student %: 28.7%<br/>• Median Faculty Ratio: 1:17.3<br/>• Total Student Body: 38.2M<br/>• Academic Staff: 2.21M<br/><br/><b>Navigation:</b><br/>[ ] Overview<br/>[ ] Research Analytics<br/><b>[X] Student Analytics</b><br/>[ ] Country Comparison", body_style),
            Paragraph("""
            <b>Main Analytics Panels:</b><br/><br/>
            <b>1. International Student Share by Country & Tier (Box & Whisker / Strip Plot)</b><br/>
            - Highlights distribution of international student ratios across UK (42%), Australia (43%), USA (26%), and Asia (16%).<br/><br/>
            <b>2. Faculty-to-Student Ratio vs Overall Ranking Score (Scatter Plot with Reference Bands)</b><br/>
            - Evaluates class intimacy vs institutional prestige. Shows that institutions with ratios below 1:8 dominate the Top 20.<br/><br/>
            <b>3. Total Enrollment vs International Students (Bubble Treemap)</b><br/>
            - Visualizes university size (tile size) and internationalization index (color saturation).
            """, body_style),
            Paragraph("<b>Diversity Takeaways:</b><br/>• UK and Australian institutions exhibit the highest international student density (>40%).<br/>• Elite institutions maintain faculty ratios under 1:6.<br/>• Higher international faculty strongly correlates with international student pull.", body_style)
        ]
    ]
    table_d3 = Table(wireframe_d3, colWidths=[200, 370, 150])
    table_d3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E65100")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#FFF3E0")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (2,1), (2,1), colors.HexColor("#F8F9FA")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(table_d3)
    story.append(PageBreak())

    # -------------------------------------------------------------
    # PAGE 5: DASHBOARD 4 - COUNTRY COMPARISON WIREFRAME
    # -------------------------------------------------------------
    story.append(Paragraph("Dashboard 4 Wireframe: Country Comparison", h1_style))
    story.append(Paragraph("Macro-level benchmarking comparing higher education systems across nations, regions, and competitive clusters.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2E7D32"), spaceAfter=8))

    wireframe_d4 = [
        [Paragraph("<b>EduVision DV</b> | Country-Level Higher Education Benchmarking", body_bold),
         Paragraph("<b>Year:</b> [ 2024 ▼ ]  <b>Metric:</b> [ Global Ranking Score ▼ ]", body_style),
         Paragraph("<b>View:</b> Country Comparison", body_style)],
        [
            Paragraph("<b>Macro KPIs:</b><br/>• Countries Evaluated: 42<br/>• Top Nation: United States<br/>• Highest Avg Score: Switzerland (84.1)<br/>• Highest Intl %: Australia (42.8%)<br/><br/><b>Navigation:</b><br/>[ ] Overview<br/>[ ] Research Analytics<br/>[ ] Student Analytics<br/><b>[X] Country Comparison</b>", body_style),
            Paragraph("""
            <b>Main Analytics Panels:</b><br/><br/>
            <b>1. Global Education Excellence Map (Choropleth World Map)</b><br/>
            - Color-coded by average institutional score per country with institutional count overlays.<br/><br/>
            <b>2. Country Performance Scoreboard (Top 15 Countries Multi-KPI Bar Table)</b><br/>
            - Side-by-side comparative ranking: University Count, Avg Overall Score, Top 100 Universities Count, Avg Citations.<br/><br/>
            <b>3. Regional Performance Radar & Boxplot</b><br/>
            - Compares North America, Europe, Asia, Oceania, and South America across all 6 core KPIs simultaneously.
            """, body_style),
            Paragraph("<b>Policy Benchmarking:</b><br/>• Switzerland and Singapore lead in average system score.<br/>• USA dominates in absolute Top 100 representation (42%).<br/>• Asia demonstrates the highest 5-year growth trajectory in research volume.", body_style)
        ]
    ]
    table_d4 = Table(wireframe_d4, colWidths=[200, 370, 150])
    table_d4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1B5E20")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#E8F5E9")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (2,1), (2,1), colors.HexColor("#F8F9FA")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(table_d4)
    story.append(PageBreak())

    # -------------------------------------------------------------
    # PAGE 6: INTERACTION MATRIX & DESIGN SPECIFICATIONS
    # -------------------------------------------------------------
    story.append(Paragraph("System Interactivity, Action Filters & Design Tokens", h1_style))
    story.append(Paragraph("Architectural matrix defining filter scopes, parameter controls, URL routing, and layout guidelines.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent_purple, spaceAfter=8))

    matrix_data = [
        [Paragraph("<b>Component</b>", body_bold), Paragraph("<b>Trigger / Scope</b>", body_bold), Paragraph("<b>Target Sheets / Action</b>", body_bold), Paragraph("<b>Behavior Description</b>", body_bold)],
        [Paragraph("Year Parameter", body_style), Paragraph("Global (All Dashboards)", body_style), Paragraph("All KPI Cards, Trends, Rank Tables", body_style), Paragraph("Selects reporting year [2020-2024]; shifts YoY comparison baseline automatically.", body_style)],
        [Paragraph("Region Filter", body_style), Paragraph("Global / Dashboard", body_style), Paragraph("Country Map, Regional Donut, University Table", body_style), Paragraph("Hierarchical cascade: selecting Region updates Country dropdown choices dynamically.", body_style)],
        [Paragraph("Country Filter", body_style), Paragraph("Global / Dashboard", body_style), Paragraph("University Table, Scatter Plots, Bar Charts", body_style), Paragraph("Filters data down to individual national systems (e.g. USA, UK, Switzerland, Singapore).", body_style)],
        [Paragraph("Table Row Selection", body_style), Paragraph("Dashboard 1 Table", body_style), Paragraph("5-Year Score Trend Line", body_style), Paragraph("Clicking a university filters the line chart to display that specific institution's trajectory.", body_style)],
        [Paragraph("Donut Slice Action", body_style), Paragraph("Dashboard 1 Donut", body_style), Paragraph("Top Universities & Publications Bars", body_style), Paragraph("Clicking 'Europe' filters university table and bars to European institutions.", body_style)],
        [Paragraph("Tab Navigation", body_style), Paragraph("Top / Sidebar Buttons", body_style), Paragraph("Active Dashboard Viewport", body_style), Paragraph("Switches smoothly between Overview, Research, Student, and Country dashboards.", body_style)]
    ]
    table_matrix = Table(matrix_data, colWidths=[120, 140, 200, 260])
    table_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F9F9FB")]),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(table_matrix)
    story.append(Spacer(1, 12))

    design_tokens = [
        [Paragraph("<b>Design Token</b>", body_bold), Paragraph("<b>Specification / Hex Value</b>", body_bold), Paragraph("<b>Usage & Typography</b>", body_bold)],
        [Paragraph("Primary Dark Background", body_style), Paragraph("#1A0933 / #120A24", body_style), Paragraph("Dashboard canvas background and header styling", body_style)],
        [Paragraph("KPI Card Backgrounds", body_style), Paragraph("#2B154A (Overview) / Multi-tinted cards", body_style), Paragraph("Card containers with 4px border radius and 1px borders", body_style)],
        [Paragraph("Accent / Highlight Colors", body_style), Paragraph("Teal (#00C9A7), Coral (#FF8066), Gold (#FFC75F)", body_style), Paragraph("Bar charts, positive trend indicators, regional color maps", body_style)],
        [Paragraph("Typography Standards", body_style), Paragraph("Segoe UI / Arial / Tableau Book", body_style), Paragraph("Headers: 14-18pt Bold; KPIs: 22-26pt Bold; Data labels: 9-10pt Regular", body_style)]
    ]
    table_tokens = Table(design_tokens, colWidths=[160, 200, 360])
    table_tokens.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), accent_purple),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F9F9FB")]),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(table_tokens)

    doc.build(story)
    print(f"[SUCCESS] Storyboard PDF generated successfully: {pdf_path}")
    # Also copy to root for immediate user access
    import shutil
    shutil.copy(pdf_path, "dashboard_storyboard.pdf")
    print("Copied to: dashboard_storyboard.pdf")

if __name__ == "__main__":
    create_storyboard()
