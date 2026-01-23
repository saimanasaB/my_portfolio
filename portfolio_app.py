# portfolio_app.py

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Sai Manasa B - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, unique styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Hide sidebar and default elements */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Modern dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1629 100%);
        color: #e6eaf0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0e27;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* ==================== NAVIGATION ==================== */
    .nav-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
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
    
    /* Hide radio label */
    .stRadio > label {
        display: none !important;
    }
    
    /* Radio container */
    .stRadio > div {
        display: flex !important;
        flex-direction: row !important;
        gap: 8px !important;
        background: transparent !important;
        padding: 0 !important;
    }
    
    div[role="radiogroup"] {
        display: flex !important;
        gap: 8px !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
    }
    
    /* Radio buttons - Modern glass morphism style */
    .stRadio label {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        color: #a8b2d1 !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        letter-spacing: 0.3px !important;
    }
    
    .stRadio label span,
    .stRadio label div,
    .stRadio label p {
        color: #a8b2d1 !important;
    }
    
    .stRadio label:hover {
        background: rgba(102, 126, 234, 0.15) !important;
        border-color: rgba(102, 126, 234, 0.5) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
    }
    
    /* Active state */
    .stRadio label:has(input:checked) {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%) !important;
        border: 1px solid rgba(102, 126, 234, 0.6) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
    }
    
    .stRadio label:has(input:checked) span,
    .stRadio label:has(input:checked) div,
    .stRadio label:has(input:checked) p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .stRadio input[type="radio"] {
        display: none !important;
    }
    
    /* ==================== TYPOGRAPHY ==================== */
    h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    h1 {
        color: #ffffff !important;
        font-size: 56px;
        line-height: 1.1;
    }
    
    h2 {
        color: #ffffff !important;
        font-size: 36px;
        border: none !important;
        margin-bottom: 2rem !important;
        position: relative;
        display: inline-block;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    h3 {
        color: #a8b2d1 !important;
        font-size: 24px;
        font-weight: 700;
    }
    
    h4 {
        color: #8892b0 !important;
        font-size: 18px;
        font-weight: 600;
    }
    
    p, li {
        color: #8892b0 !important;
        line-height: 1.8;
        font-weight: 400;
    }
    
    strong {
        color: #ccd6f6 !important;
        font-weight: 600;
    }
    
    /* ==================== HERO SECTION ==================== */
    .hero-container {
        text-align: center;
        padding: 4rem 2rem;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .hero-greeting {
        font-size: 18px;
        color: #667eea;
        font-weight: 600;
        margin-bottom: 1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .hero-name {
        font-size: 72px;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #a8b2d1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -2px;
    }
    
    .hero-title {
        font-size: 24px;
        color: #8892b0;
        margin-top: 1rem;
        font-weight: 400;
        line-height: 1.6;
    }
    
    .hero-title span {
        color: #667eea;
        font-weight: 600;
    }
    
    /* ==================== STATS SECTION ==================== */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .stat-card:hover {
        transform: translateY(-8px);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.2);
    }
    
    .stat-number {
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }
    
    .stat-label {
        font-size: 14px;
        color: #8892b0;
        margin-top: 0.5rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    /* ==================== CARDS ==================== */
    .content-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .content-card:hover {
        transform: translateY(-4px);
        border-color: rgba(102, 126, 234, 0.3);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
    }
    
    .content-card h4 {
        color: #ccd6f6 !important;
        margin-top: 0 !important;
        margin-bottom: 1rem;
    }
    
    .content-card ul {
        list-style: none;
        padding: 0;
        margin: 1rem 0;
    }
    
    .content-card li {
        padding-left: 1.5rem;
        position: relative;
        margin: 0.8rem 0;
    }
    
    .content-card li::before {
        content: '▹';
        color: #667eea;
        font-size: 18px;
        position: absolute;
        left: 0;
        font-weight: bold;
    }
    
    /* ==================== TIMELINE ==================== */
    .timeline-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 4px solid #667eea;
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
    }
    
    .timeline-card h3 {
        color: #ccd6f6 !important;
        margin-top: 0;
    }
    
    .company {
        color: #667eea !important;
        font-weight: 600;
        font-size: 16px;
    }
    
    .date {
        color: #8892b0 !important;
        font-size: 14px;
        font-style: italic;
    }
    
    /* ==================== SKILL BADGES ==================== */
    .skill-badge {
        display: inline-block;
        background: rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #667eea !important;
        padding: 10px 20px;
        border-radius: 25px;
        margin: 6px;
        font-size: 14px;
        font-weight: 600;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    
    .skill-badge:hover {
        background: rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.6);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* ==================== TECH BADGE ==================== */
    .tech-stack {
        background: rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #667eea !important;
        padding: 12px 24px;
        border-radius: 30px;
        display: inline-block;
        font-weight: 600;
        margin-top: 1rem;
        font-size: 14px;
    }
    
    /* ==================== CONTACT CARD ==================== */
    .contact-info-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    .contact-info-card p,
    .contact-info-card a,
    .contact-info-card strong {
        color: #ccd6f6 !important;
    }
    
    .contact-info-card a:hover {
        color: #667eea !important;
    }
    
    /* ==================== FORM STYLING ==================== */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox select {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #ccd6f6 !important;
        border-radius: 12px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: rgba(102, 126, 234, 0.5) !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #a8b2d1 !important;
        font-weight: 600 !important;
    }
    
    /* ==================== BUTTON ==================== */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 32px !important;
        border-radius: 30px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* ==================== LINKS ==================== */
    a {
        color: #667eea !important;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    a:hover {
        color: #8892ff !important;
    }
    
    /* ==================== DIVIDER ==================== */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.3), transparent);
        margin: 2rem 0;
    }
    
    /* ==================== FOOTER ==================== */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #8892b0;
        font-size: 14px;
        margin-top: 4rem;
    }
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
    ["🏠 About", "💼 Experience", "🚀 Projects", "⚡ Skills", "📧 Contact"],
    horizontal=True,
    key="navigation"
)

st.markdown("<hr>", unsafe_allow_html=True)

page_name = page.split(" ", 1)[1] if " " in page else page

# ==================== ABOUT PAGE ====================
if page_name == "About":
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-greeting'>👋 Hello, I'm</div>
        <h1 class='hero-name'>Sai Manasa B</h1>
        <div class='hero-title'>
            Backend Developer specializing in <span>REST APIs</span>, <span>FastAPI</span>, <span>MySQL</span>, and <span>AWS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>70+</div>
            <div class='stat-label'>APIs Deployed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>1000+</div>
            <div class='stat-label'>Active Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>60%</div>
            <div class='stat-label'>Query Optimization</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>3000+</div>
            <div class='stat-label'>Daily Requests</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # About Me
    st.markdown("## About Me")
    st.markdown("""
    <div class='content-card'>
        <p>I'm a Backend Developer with expertise in building scalable production REST APIs. I specialize in designing efficient database architectures and deploying serverless solutions on AWS.</p>
        <p>My work focuses on creating robust, high-performance systems that serve thousands of users daily. From database schema design to API optimization, I deliver solutions that make a real impact.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact Info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Let's Connect")
        st.markdown("""
        - 📧 **Email:** [saimanasab10@gmail.com](mailto:saimanasab10@gmail.com)
        - 📞 **Phone:** +91 8667564076
        """)
    
    with col2:
        st.markdown("### Find Me Online")
        st.markdown("""
        - 💼 **LinkedIn:** [Sai Manasa B](https://www.linkedin.com/in/sai-manasa-b-1765b420b/)
        - 💻 **GitHub:** [saimanasaB](https://github.com/saimanasaB)
        """)

# ==================== EXPERIENCE PAGE ====================
elif page_name == "Experience":
    st.markdown("## Professional Experience")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='timeline-card'>
        <h3>API (Backend) Developer</h3>
        <p class='company'>Satyukt Analytics Pvt. Ltd, Bengaluru</p>
        <p class='date'>📅 December 2024 – Present</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='content-card'>
            <h4>🚀 API Development & Deployment</h4>
            <ul>
                <li>Architected and deployed <strong>70+ REST APIs</strong> using FastAPI and MySQL on AWS Lambda</li>
                <li>Supporting <strong>1000+ active users</strong> handling <strong>3000+ daily requests</strong></li>
                <li>Configured AWS Lambda with API Gateway custom domain and Lambda Layers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='content-card'>
            <h4>🔒 Security & Authentication</h4>
            <ul>
                <li>Built secure authentication workflows with <strong>JWT tokens</strong></li>
                <li>Implemented role-based authorization for 6 user types</li>
                <li>Ensured data protection and access control</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='content-card'>
            <h4>💾 Database Architecture</h4>
            <ul>
                <li>Designed MySQL database schema with <strong>15+ normalized tables</strong></li>
                <li>Optimized queries reducing response time by <strong>60%</strong> (850ms → 340ms)</li>
                <li>Built multi-role platform supporting 6 user types</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='content-card'>
            <h4>🛰️ Specialized Development</h4>
            <ul>
                <li>Developed RESTful APIs for <strong>satellite data retrieval</strong></li>
                <li>Implemented geospatial coordinate processing</li>
                <li>Integrated real-time data processing pipelines</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== PROJECTS PAGE ====================
elif page_name == "Projects":
    st.markdown("## Featured Projects")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sat2Farm
    st.markdown("""
    <div class='content-card'>
        <h2 style='color: #ccd6f6; margin-top: 0;'>🌾 Sat2Farm</h2>
        <h4 style='color: #8892b0; font-weight: 400; margin-bottom: 1rem;'>Agricultural Monitoring Platform</h4>
        <div class='tech-stack'>FastAPI • MySQL • AWS S3 • Satellite APIs</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Core Features**
        - Built backend with **25+ REST APIs**
        - Serving **1000+ farmers**
        - Managing **1500+ farm plots**
        - Real-time crop health monitoring (NDVI)
        """)
    
    with col2:
        st.markdown("""
        **⚡ Key Implementations**
        - Integrated satellite data APIs
        - Soil analysis and weather forecasting
        - Farm CRUD with polygon validation
        - Image advisory system with AWS S3
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Say Trees
    st.markdown("""
    <div class='content-card'>
        <h2 style='color: #ccd6f6; margin-top: 0;'>🌳 Say Trees</h2>
        <h4 style='color: #8892b0; font-weight: 400; margin-bottom: 1rem;'>Tree Plantation Management System</h4>
        <div class='tech-stack'>FastAPI • AWS Lambda • MySQL • API Gateway</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Architecture**
        - Designed schema with **15+ normalized tables**
        - Deployed **35+ APIs** on AWS Lambda
        - Built role-based access for **5 user types**
        """)
    
    with col2:
        st.markdown("""
        **⚡ Order Lifecycle**
        - Sapling ordering system
        - Inventory validation
        - Logistics assignment
        - Real-time delivery tracking
        """)

# ==================== SKILLS PAGE ====================
elif page_name == "Skills":
    st.markdown("## Technical Expertise")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Backend & Frameworks")
        st.markdown("""
        <span class='skill-badge'>Python</span>
        <span class='skill-badge'>FastAPI</span>
        <span class='skill-badge'>Flask</span>
        <span class='skill-badge'>REST APIs</span>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Database")
        st.markdown("""
        <span class='skill-badge'>MySQL</span>
        <span class='skill-badge'>SQL</span>
        <span class='skill-badge'>Database Design</span>
        <span class='skill-badge'>Query Optimization</span>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Cloud & DevOps")
        st.markdown("""
        <span class='skill-badge'>AWS Lambda</span>
        <span class='skill-badge'>API Gateway</span>
        <span class='skill-badge'>S3</span>
        <span class='skill-badge'>Linux/Ubuntu</span>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Tools & Technologies")
        st.markdown("""
        <span class='skill-badge'>Git</span>
        <span class='skill-badge'>JWT</span>
        <span class='skill-badge'>Geospatial APIs</span>
        <span class='skill-badge'>Serverless</span>
        """, unsafe_allow_html=True)

# ==================== CONTACT PAGE ====================
elif page_name == "Contact":
    st.markdown("## Get In Touch")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Send a Message")
        st.markdown("Have a question or want to work together? Feel free to reach out!")
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", placeholder="John Doe")
            email = st.text_input("Your Email", placeholder="john@example.com")
            subject = st.selectbox("Subject", ["General Inquiry", "Job Opportunity", "Project Collaboration", "Other"])
            message = st.text_area("Your Message", placeholder="Write your message here...", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀")
            
            if submitted:
                if name and email and message:
                    st.success(f"✅ Thanks {name}! Your message has been sent successfully.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
    
    with col2:
        st.markdown("### Contact Information")
        st.markdown("""
        <div class='contact-info-card'>
            <p><strong>📧 Email</strong><br/>saimanasab10@gmail.com</p>
            <p><strong>📞 Phone</strong><br/>+91 8667564076</p>
            <p><strong>💼 LinkedIn</strong><br/><a href='https://www.linkedin.com/in/sai-manasa-b-1765b420b/'>Sai Manasa B</a></p>
            <p><strong>💻 GitHub</strong><br/><a href='https://github.com/saimanasaB'>saimanasaB</a></p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class='footer'>
    <p>© 2025 Sai Manasa B • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
