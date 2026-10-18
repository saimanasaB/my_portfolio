# portfolio_app.py

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Sai Manasa B - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    [data-testid="stSidebar"] { display: none; }
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1629 100%);
        color: #e6eaf0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #0a0e27; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    .block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1400px; }
    
    .nav-container {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 1rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .nav-brand {
        font-size: 26px;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }
    
    .stRadio > label { display: none !important; }
    .stRadio > div { display: flex !important; flex-direction: row !important; gap: 8px !important; background: transparent !important; padding: 0 !important; }
    div[role="radiogroup"] { display: flex !important; gap: 8px !important; flex-direction: row !important; flex-wrap: wrap !important; }
    
    .stRadio label {
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(10px) !important;
        color: #a8b2d1 !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        letter-spacing: 0.3px !important;
    }
    
    .stRadio label span, .stRadio label div, .stRadio label p { color: #a8b2d1 !important; }
    
    .stRadio label:hover {
        background: rgba(102,126,234,0.15) !important;
        border-color: rgba(102,126,234,0.5) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102,126,234,0.2);
    }
    
    .stRadio label:has(input:checked) {
        background: linear-gradient(135deg, rgba(102,126,234,0.2) 0%, rgba(118,75,162,0.2) 100%) !important;
        border: 1px solid rgba(102,126,234,0.6) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(102,126,234,0.3);
    }
    
    .stRadio label:has(input:checked) span,
    .stRadio label:has(input:checked) div,
    .stRadio label:has(input:checked) p { color: #ffffff !important; font-weight: 600 !important; }
    
    .stRadio input[type="radio"] { display: none !important; }
    
    h1, h2, h3, h4 { font-family: 'Inter', sans-serif; font-weight: 800; letter-spacing: -1px; }
    h1 { color: #ffffff !important; font-size: 56px; line-height: 1.1; }
    h2 { color: #ffffff !important; font-size: 36px; border: none !important; margin-bottom: 2rem !important; position: relative; display: inline-block; }
    h2::after { content: ''; position: absolute; bottom: -8px; left: 0; width: 60px; height: 4px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 2px; }
    h3 { color: #a8b2d1 !important; font-size: 24px; font-weight: 700; }
    h4 { color: #8892b0 !important; font-size: 18px; font-weight: 600; }
    p, li { color: #8892b0 !important; line-height: 1.8; font-weight: 400; }
    strong { color: #ccd6f6 !important; font-weight: 600; }
    
    .hero-container { text-align: center; padding: 4rem 2rem; margin-bottom: 3rem; position: relative; }
    .hero-greeting { font-size: 18px; color: #667eea; font-weight: 600; margin-bottom: 1rem; letter-spacing: 2px; text-transform: uppercase; }
    .hero-name { font-size: 72px; font-weight: 900; background: linear-gradient(135deg, #ffffff 0%, #a8b2d1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; line-height: 1.1; letter-spacing: -2px; }
    .hero-title { font-size: 24px; color: #8892b0; margin-top: 1rem; font-weight: 400; line-height: 1.6; }
    .hero-title span { color: #667eea; font-weight: 600; }
    
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 3rem 0; }
    
    .stat-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); }
    .stat-card:hover { transform: translateY(-8px); border-color: rgba(102,126,234,0.5); box-shadow: 0 12px 40px rgba(102,126,234,0.2); }
    .stat-number { font-size: 48px; font-weight: 800; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; }
    .stat-label { font-size: 14px; color: #8892b0; margin-top: 0.5rem; font-weight: 500; letter-spacing: 0.5px; }
    
    .content-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .content-card:hover { transform: translateY(-4px); border-color: rgba(102,126,234,0.3); box-shadow: 0 12px 40px rgba(0,0,0,0.3); }
    .content-card h4 { color: #ccd6f6 !important; margin-top: 0 !important; margin-bottom: 1rem; }
    .content-card ul { list-style: none; padding: 0; margin: 1rem 0; }
    .content-card li { padding-left: 1.5rem; position: relative; margin: 0.8rem 0; }
    .content-card li::before { content: '▹'; color: #667eea; font-size: 18px; position: absolute; left: 0; font-weight: bold; }
    
    .timeline-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        border-left: 4px solid #667eea;
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
    }
    
    .timeline-card h3 { color: #ccd6f6 !important; margin-top: 0; }
    .company { color: #667eea !important; font-weight: 600; font-size: 16px; }
    .date { color: #8892b0 !important; font-size: 14px; font-style: italic; }
    .badge { display: inline-block; background: rgba(102,126,234,0.15); border: 1px solid rgba(102,126,234,0.4); color: #667eea !important; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin: 2px; }
    
    .skill-badge {
        display: inline-block;
        background: rgba(102,126,234,0.1);
        border: 1px solid rgba(102,126,234,0.3);
        color: #667eea !important;
        padding: 10px 20px;
        border-radius: 25px;
        margin: 6px;
        font-size: 14px;
        font-weight: 600;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    
    .skill-badge:hover { background: rgba(102,126,234,0.2); border-color: rgba(102,126,234,0.6); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(102,126,234,0.3); }
    
    .tech-stack { background: rgba(102,126,234,0.1); border: 1px solid rgba(102,126,234,0.3); color: #667eea !important; padding: 12px 24px; border-radius: 30px; display: inline-block; font-weight: 600; margin-top: 1rem; font-size: 14px; }
    
    .contact-info-card { background: linear-gradient(135deg, rgba(102,126,234,0.15) 0%, rgba(118,75,162,0.15) 100%); border: 1px solid rgba(102,126,234,0.3); padding: 2rem; border-radius: 20px; backdrop-filter: blur(10px); }
    .contact-info-card p, .contact-info-card a, .contact-info-card strong { color: #ccd6f6 !important; }
    .contact-info-card a:hover { color: #667eea !important; }
    
    .stTextInput input, .stTextArea textarea, .stSelectbox select { background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important; color: #ccd6f6 !important; border-radius: 12px !important; font-family: 'Inter', sans-serif !important; }
    .stTextInput input:focus, .stTextArea textarea:focus { border-color: rgba(102,126,234,0.5) !important; box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important; }
    .stTextInput label, .stTextArea label, .stSelectbox label { color: #a8b2d1 !important; font-weight: 600 !important; }
    
    .stButton > button { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; color: white !important; border: none !important; padding: 12px 32px !important; border-radius: 30px !important; font-weight: 600 !important; font-size: 16px !important; letter-spacing: 0.5px !important; transition: all 0.3s ease !important; box-shadow: 0 4px 15px rgba(102,126,234,0.3) !important; }
    .stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(102,126,234,0.4) !important; }
    
    a { color: #667eea !important; text-decoration: none; transition: all 0.3s ease; font-weight: 500; }
    a:hover { color: #8892ff !important; }
    
    hr { border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(102,126,234,0.3), transparent); margin: 2rem 0; }
    
    .footer { text-align: center; padding: 2rem; color: #8892b0; font-size: 14px; margin-top: 4rem; }
    
    .cert-card { background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%); border: 1px solid rgba(102,126,234,0.3); padding: 1.2rem 1.8rem; border-radius: 14px; margin: 0.8rem 0; display: flex; align-items: center; gap: 1rem; }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class='nav-container'>
    <div class='nav-brand'>⚡ SAI MANASA B</div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "Navigation",
    ["🏠 About", "💼 Experience", "🚀 Projects", "⚡ Skills", "🎓 Certifications", "📧 Contact"],
    horizontal=True,
    key="navigation"
)

st.markdown("<hr>", unsafe_allow_html=True)

page_name = page.split(" ", 1)[1] if " " in page else page

# ==================== ABOUT ====================
if page_name == "About":
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-greeting'>👋 Hello, I'm</div>
        <h1 class='hero-name'>Sai Manasa B</h1>
        <div class='hero-title'>
            Backend Developer · <span>FastAPI</span> · <span>MySQL</span> · <span>AWS Lambda</span> · <span>Azure</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='stat-card'><div class='stat-number'>70+</div><div class='stat-label'>APIs Deployed</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stat-card'><div class='stat-number'>1K+</div><div class='stat-label'>Active Users</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='stat-card'><div class='stat-number'>60%</div><div class='stat-label'>Query Improvement</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='stat-card'><div class='stat-number'>3K+</div><div class='stat-label'>Daily Requests</div></div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("## About Me")
    st.markdown("""
    <div class='content-card'>
        <p>I'm a Backend Developer with 2+ years of experience building scalable production REST APIs. I specialize in <strong>FastAPI</strong>, <strong>Django REST Framework</strong>, <strong>MySQL</strong>, and cloud deployment on <strong>AWS Lambda</strong> and <strong>Microsoft Azure</strong>.</p>
        <p>I've worked across agri-tech, plantation management, and enterprise web platforms — designing database schemas from scratch, optimizing queries, and ensuring code quality through security and linting tools. Currently exploring Microsoft Azure and pursuing the AI Cloud Developer Associate certification.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Let's Connect")
        st.markdown("""
        - 📧 **Email:** [saimanasab10@gmail.com](mailto:saimanasab10@gmail.com)
        - 📞 **Phone:** +91 8667564076
        - 📍 **Location:** Open to Hyderabad (relocating)
        """)
    with col2:
        st.markdown("### Find Me Online")
        st.markdown("""
        - 💼 **LinkedIn:** [Sai Manasa B](https://www.linkedin.com/in/sai-manasa-b-1765b420b/)
        - 💻 **GitHub:** [saimanasaB](https://github.com/saimanasaB)
        """)

# ==================== EXPERIENCE ====================
elif page_name == "Experience":
    st.markdown("## Professional Experience")
    st.markdown("<br>", unsafe_allow_html=True)

    # GeakMinds
    st.markdown("""
    <div class='timeline-card'>
        <h3>Associate Software Engineer</h3>
        <p class='company'>GeakMinds Technologies · Remote (US-based IT Consulting Firm)</p>
        <p class='date'>📅 April 2026 – Present</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='content-card'>
            <h4>🛠️ Projects Worked On</h4>
            <ul>
                <li>Worked across <strong>4 projects</strong> — OVEAT, Mapping UI, Proposal UI, New User UI</li>
                <li>Built and enhanced <strong>FastAPI endpoints</strong>, added new features</li>
                <li>Fixed endpoint-level issues including document generation and alignment in BOM Template</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='content-card'>
            <h4>✅ Code Quality & Testing</h4>
            <ul>
                <li>Wrote <strong>unit test cases</strong> for all endpoints across OVEAT, Mapping UI, and Proposal UI</li>
                <li>Applied <strong>Ruff, Black, isort, Bandit, Pylint, Mypy, Flake8, Snyk</strong> fixes across all projects</li>
                <li>Managed <strong>Git</strong> — commits, PRs, branch management, and merge conflict resolution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Satyukt
    st.markdown("""
    <div class='timeline-card'>
        <h3>Backend Developer</h3>
        <p class='company'>Satyukt Analytics Pvt. Ltd · Bengaluru (Agri-Tech Startup)</p>
        <p class='date'>📅 December 2024 – March 2026 &nbsp;|&nbsp; Intern (Dec 2024 – May 2025) · Full-Time (Jun 2025 – Mar 2026)</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='content-card'>
            <h4>🚀 API Development</h4>
            <ul>
                <li>Built and deployed <strong>70+ REST APIs</strong> using FastAPI on AWS Lambda</li>
                <li>Serving <strong>1000+ active users</strong> and <strong>3000+ daily requests</strong></li>
                <li>Custom domain with API Gateway and Lambda Layers for dependency management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='content-card'>
            <h4>💾 Database & Performance</h4>
            <ul>
                <li>Designed <strong>MySQL schema from scratch</strong> — 15+ normalized tables</li>
                <li>Reduced query response time from <strong>850ms to 340ms (60% improvement)</strong></li>
                <li>Implemented <strong>JWT-based auth</strong> with role-level access control for 6 user roles</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== PROJECTS ====================
elif page_name == "Projects":
    st.markdown("## Featured Projects")
    st.markdown("<br>", unsafe_allow_html=True)

    # OVEAT
    st.markdown("""
    <div class='content-card'>
        <h2 style='color:#ccd6f6;margin-top:0;'>📊 OVEAT</h2>
        <h4 style='color:#8892b0;font-weight:400;margin-bottom:1rem;'>Excel-to-Web Migration Platform</h4>
        <div class='tech-stack'>FastAPI • Pydantic • Azure SQL • Azure Storage • Unit Testing</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 What I Built**
        - Designed and developed **REST API endpoints** using FastAPI + Pydantic
        - Converted manual Excel-based workflows into a fully functional web backend
        - DB population scripts to migrate Excel data into Azure SQL
        """)
    with col2:
        st.markdown("""
        **⚡ Additional Contributions**
        - Read files from **Azure Storage**, persist into **Azure SQL Database**
        - Wrote **unit tests**, source-mapping docs, and API design documentation
        - Vulnerability fixes using Ruff, Black, Bandit, Mypy
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Sat2Farm
    st.markdown("""
    <div class='content-card'>
        <h2 style='color:#ccd6f6;margin-top:0;'>🌾 Sat2Farm</h2>
        <h4 style='color:#8892b0;font-weight:400;margin-bottom:1rem;'>Agricultural Monitoring Platform</h4>
        <div class='tech-stack'>FastAPI • MySQL • AWS Lambda • API Gateway • S3</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Scale**
        - **25+ REST APIs** serving **1000+ farmers**
        - Managing **1500+ farm plots** with 100K+ DB records
        - Deployed on **AWS Lambda** with API Gateway and S3
        """)
    with col2:
        st.markdown("""
        **⚡ Features**
        - Real-time crop health monitoring (NDVI)
        - Soil analysis and weather forecasting
        - Farm CRUD with polygon boundary validation
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # SayTrees
    st.markdown("""
    <div class='content-card'>
        <h2 style='color:#ccd6f6;margin-top:0;'>🌳 Say Trees</h2>
        <h4 style='color:#8892b0;font-weight:400;margin-bottom:1rem;'>Tree Plantation Management System</h4>
        <div class='tech-stack'>Python • Django REST Framework • MySQL • GitHub</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Architecture**
        - REST APIs using **Django REST Framework**
        - Query-based approach with `views.py` and `urls.py`
        - Class-based and function-based views
        """)
    with col2:
        st.markdown("""
        **⚡ Features**
        - MySQL schema with **15+ tables**
        - Role-based access for **5 user types**
        - Full order lifecycle: ordering → logistics → delivery
        - **GitHub** branching, PRs, conflict resolution
        """)

# ==================== SKILLS ====================
elif page_name == "Skills":
    st.markdown("## Technical Skills")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Languages & Frameworks")
        st.markdown("""
        <span class='skill-badge'>Python</span>
        <span class='skill-badge'>FastAPI</span>
        <span class='skill-badge'>Django REST Framework</span>
        <span class='skill-badge'>Flask</span>
        <span class='skill-badge'>SQL</span>
        <span class='skill-badge'>Pydantic</span>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Databases")
        st.markdown("""
        <span class='skill-badge'>MySQL</span>
        <span class='skill-badge'>Azure SQL</span>
        <span class='skill-badge'>Schema Design</span>
        <span class='skill-badge'>Query Optimization</span>
        <span class='skill-badge'>Indexing</span>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Code Quality & Security")
        st.markdown("""
        <span class='skill-badge'>Ruff</span>
        <span class='skill-badge'>Black</span>
        <span class='skill-badge'>isort</span>
        <span class='skill-badge'>Bandit</span>
        <span class='skill-badge'>Pylint</span>
        <span class='skill-badge'>Mypy</span>
        <span class='skill-badge'>Flake8</span>
        <span class='skill-badge'>Snyk</span>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Cloud & DevOps")
        st.markdown("""
        <span class='skill-badge'>AWS Lambda</span>
        <span class='skill-badge'>API Gateway</span>
        <span class='skill-badge'>Amazon S3</span>
        <span class='skill-badge'>Lambda Layers</span>
        <span class='skill-badge'>Microsoft Azure</span>
        <span class='skill-badge'>Azure Storage</span>
        <span class='skill-badge'>Docker</span>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Tools & Concepts")
        st.markdown("""
        <span class='skill-badge'>Git</span>
        <span class='skill-badge'>GitHub</span>
        <span class='skill-badge'>Postman</span>
        <span class='skill-badge'>Linux</span>
        <span class='skill-badge'>REST API Design</span>
        <span class='skill-badge'>JWT / OAuth</span>
        <span class='skill-badge'>RBAC</span>
        <span class='skill-badge'>Unit Testing</span>
        """, unsafe_allow_html=True)

# ==================== CERTIFICATIONS ====================
elif page_name == "Certifications":
    st.markdown("## Certifications & Learning")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='content-card'>
        <h4>🎓 Currently Pursuing</h4>
        <div class='cert-card'>
            <div>
                <strong style='color:#ccd6f6;font-size:16px;'>Microsoft Azure AI Fundamentals — AI-900</strong><br/>
                <span style='color:#8892b0;font-size:14px;'>Microsoft · In Progress</span>
            </div>
        </div>
        <div class='cert-card'>
            <div>
                <strong style='color:#ccd6f6;font-size:16px;'>Microsoft AI Cloud Developer Associate — AZ-200 Course</strong><br/>
                <span style='color:#8892b0;font-size:14px;'>Microsoft · Pursuing</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content-card'>
        <h4>📚 Education</h4>
        <div class='cert-card'>
            <div>
                <strong style='color:#ccd6f6;font-size:16px;'>Integrated M.Sc. in Decision and Computing Sciences (5-Year)</strong><br/>
                <span style='color:#8892b0;font-size:14px;'>Coimbatore Institute of Technology · Sep 2020 – May 2025 · CGPA: 8.5/10</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content-card'>
        <h4>🔭 Currently Exploring</h4>
        <br/>
        <span class='skill-badge'>Microsoft Azure</span>
        <span class='skill-badge'>Docker</span>
        <span class='skill-badge'>CI/CD Pipelines</span>
        <span class='skill-badge'>Azure Functions</span>
        <span class='skill-badge'>PostgreSQL</span>
        <span class='skill-badge'>System Design</span>
        <span class='skill-badge'>DSA</span>
    </div>
    """, unsafe_allow_html=True)

# ==================== CONTACT ====================
elif page_name == "Contact":
    st.markdown("## Get In Touch")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Send a Message")
        st.markdown("Open to backend developer opportunities in Hyderabad. Feel free to reach out!")
        st.markdown("<br>", unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", placeholder="John Doe")
            email = st.text_input("Your Email", placeholder="john@example.com")
            subject = st.selectbox("Subject", ["Job Opportunity", "Project Collaboration", "General Inquiry", "Other"])
            message = st.text_area("Your Message", placeholder="Write your message here...", height=150)

            submitted = st.form_submit_button("Send Message 🚀")
            if submitted:
                if name and email and message:
                    st.success(f"✅ Thanks {name}! Your message has been received.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")

    with col2:
        st.markdown("### Contact Information")
        st.markdown("""
        <div class='contact-info-card'>
            <p><strong>📧 Email</strong><br/>saimanasab10@gmail.com</p>
            <p><strong>📞 Phone</strong><br/>+91 8667564076</p>
            <p><strong>📍 Location</strong><br/>Open to Hyderabad</p>
            <p><strong>💼 LinkedIn</strong><br/><a href='https://www.linkedin.com/in/sai-manasa-b-1765b420b/'>Sai Manasa B</a></p>
            <p><strong>💻 GitHub</strong><br/><a href='https://github.com/saimanasaB'>saimanasaB</a></p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class='footer'>
    <p>© 2026 Sai Manasa B • Backend Developer • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
