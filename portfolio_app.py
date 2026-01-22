# portfolio_app.py

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Sai Manasa B - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Dark theme background */
    .stApp {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* NAVIGATION STYLING - CRITICAL */
    /* Container for the entire navigation area */
    .nav-wrapper {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
    }
    
    /* Logo text styling */
    .nav-logo {
        color: white !important;
        font-size: 24px;
        font-weight: 700;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Hide the radio group label */
    .stRadio > label {
        display: none !important;
    }
    
    /* Radio buttons container */
    .stRadio > div {
        display: flex !important;
        flex-direction: row !important;
        gap: 10px !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    div[role="radiogroup"] {
        display: flex !important;
        gap: 10px !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
    }
    
    /* Individual radio button labels - FORCE WHITE TEXT */
    .stRadio label {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        padding: 12px 24px !important;
        border-radius: 25px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        border: 2px solid transparent !important;
        display: inline-flex !important;
        align-items: center !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        margin: 0 !important;
    }
    
    /* Force all text inside labels to be white */
    .stRadio label span,
    .stRadio label div,
    .stRadio label p {
        color: white !important;
    }
    
    .stRadio label:hover {
        background: rgba(255, 255, 255, 0.25) !important;
        border: 2px solid white !important;
        transform: translateY(-2px);
    }
    
    /* Active/selected state - WHITE BACKGROUND WITH PURPLE TEXT */
    .stRadio label:has(input:checked) {
        background: white !important;
        color: #667eea !important;
        font-weight: 600 !important;
        border: 2px solid white !important;
    }
    
    /* Force active tab text to be purple */
    .stRadio label:has(input:checked) span,
    .stRadio label:has(input:checked) div,
    .stRadio label:has(input:checked) p {
        color: #667eea !important;
    }
    
    /* Hide the actual radio circle */
    .stRadio input[type="radio"] {
        display: none !important;
    }
    
    /* Headers - ALL PROPERLY COLORED */
    h1 {
        color: white !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #58a6ff !important;
        border-bottom: 3px solid #58a6ff;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    
    h3 {
        color: #79c0ff !important;
        margin-top: 25px;
    }
    
    h4 {
        color: #58a6ff !important;
    }
    
    /* All paragraph and text elements */
    p, li, span:not(.stRadio span), div:not(.stRadio div) {
        color: #c9d1d9 !important;
    }
    
    /* Strong tags */
    strong {
        color: #58a6ff !important;
        font-weight: 600;
    }
    
    /* Hero section styling */
    .hero-title {
        color: white !important;
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #8b949e !important;
        text-align: center;
        font-size: 18px;
        font-weight: 400;
        margin-bottom: 30px;
    }
    
    /* Card-like sections */
    .project-card {
        background: #161b22 !important;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border-left: 5px solid #4B9CD3;
        margin: 15px 0;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(75, 156, 211, 0.3);
    }
    
    .project-card h2,
    .project-card h3,
    .project-card h4 {
        color: #58a6ff !important;
        margin-top: 0;
    }
    
    .project-card p,
    .project-card ul,
    .project-card li {
        color: #c9d1d9 !important;
    }
    
    .project-card li {
        margin: 8px 0;
    }
    
    /* Stats boxes */
    .stat-box {
        background: linear-gradient(135deg, #1f6feb 0%, #0969da 100%);
        padding: 30px 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 5px 20px rgba(31, 111, 235, 0.3);
        transition: transform 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(31, 111, 235, 0.5);
    }
    
    .stat-number {
        font-size: 48px;
        font-weight: bold;
        margin: 10px 0;
        color: white !important;
    }
    
    .stat-label {
        font-size: 15px;
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 500;
    }
    
    /* Skill badges */
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #1f6feb 0%, #0969da 100%);
        color: white !important;
        padding: 10px 18px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(31, 111, 235, 0.3);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #1f6feb 0%, #0969da 100%) !important;
        color: white !important;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(31, 111, 235, 0.5);
    }
    
    /* Timeline styling */
    .timeline-item {
        border-left: 3px solid #1f6feb;
        padding-left: 20px;
        margin-left: 10px;
        margin-bottom: 30px;
        position: relative;
    }
    
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: #1f6feb;
        border: 3px solid #0e1117;
        box-shadow: 0 0 0 2px #1f6feb;
    }
    
    .timeline-item h3 {
        color: #58a6ff !important;
    }
    
    .timeline-item p {
        color: #8b949e !important;
    }
    
    /* Profile summary box */
    .profile-summary {
        background: linear-gradient(135deg, #161b22 0%, #1c2128 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #1f6feb;
        color: #c9d1d9 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .profile-summary p {
        color: #c9d1d9 !important;
        line-height: 1.6;
    }
    
    .profile-summary strong {
        color: #58a6ff !important;
    }
    
    /* Contact info card */
    .contact-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
    }
    
    .contact-card p,
    .contact-card strong,
    .contact-card a {
        color: white !important;
    }
    
    /* Links */
    a {
        color: #58a6ff !important;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    a:hover {
        color: #79c0ff !important;
        text-decoration: underline;
    }
    
    /* Form inputs */
    .stTextInput input,
    .stTextArea textarea {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    
    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #1f6feb !important;
        box-shadow: 0 0 0 3px rgba(31, 111, 235, 0.1) !important;
    }
    
    .stSelectbox select {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
    }
    
    /* Labels for form fields */
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #c9d1d9 !important;
    }
    
    /* Info/success boxes */
    .stAlert {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
    }
    
    /* Tech stack badge */
    .tech-badge {
        background: linear-gradient(135deg, #1f6feb 0%, #0969da 100%);
        color: white !important;
        padding: 10px 20px;
        border-radius: 10px;
        display: inline-block;
        font-weight: 500;
        margin-top: 10px;
        box-shadow: 0 3px 10px rgba(31, 111, 235, 0.3);
    }
    
    /* Horizontal rule */
    hr {
        border-color: #30363d !important;
        margin: 2rem 0 !important;
    }
    
    /* Markdown bullets */
    .stMarkdown ul {
        color: #c9d1d9 !important;
    }
    
    .stMarkdown ul li {
        color: #c9d1d9 !important;
    }
</style>
""", unsafe_allow_html=True)

# Top Navigation - Using custom HTML structure
st.markdown("""
<div class='nav-wrapper'>
    <div class='nav-logo'>💼 Sai Manasa B</div>
</div>
""", unsafe_allow_html=True)

# Navigation Radio Buttons
page = st.radio(
    "Navigation",
    ["🏠 About Me", "💼 Experience", "🚀 Projects", "⚡ Skills", "📧 Contact"],
    horizontal=True,
    key="navigation"
)

st.markdown("<hr>", unsafe_allow_html=True)

# Extract the page name without emoji
page_name = page.split(" ", 1)[1] if " " in page else page

# ----------------- About Me -----------------
if page_name == "About Me":
    # Hero Section
    st.markdown("""
    <div class='hero-title'>Sai Manasa B</div>
    <div class='hero-subtitle'>Backend Developer | REST APIs | FastAPI | MySQL | AWS</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stats Section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>70+</div>
            <div class='stat-label'>APIs Deployed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>1000+</div>
            <div class='stat-label'>Active Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>60%</div>
            <div class='stat-label'>Query Optimization</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>3000+</div>
            <div class='stat-label'>Daily Requests</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Profile Summary
    st.markdown("## 👨‍💻 Profile Summary")
    st.markdown("""
    <div class='profile-summary'>
    <p>Backend Developer specializing in production REST APIs using <strong>FastAPI</strong>, <strong>MySQL</strong>, and <strong>AWS serverless architecture</strong>.
    Designed database schemas from scratch and deployed <strong>70+ APIs</strong> on AWS Lambda with custom domain. 
    Optimized queries achieving <strong>60% performance improvement</strong>, architected multi-role systems, and delivered scalable solutions serving <strong>1000+ users</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact Info Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📫 Get In Touch")
        st.markdown("""
        - 📧 **Email:** [saimanasab10@gmail.com](mailto:saimanasab10@gmail.com)
        - 📞 **Phone:** +91 8667564076
        """)
    
    with col2:
        st.markdown("### 🔗 Connect Online")
        st.markdown("""
        - 💼 **LinkedIn:** [Sai Manasa](https://www.linkedin.com/in/sai-manasa-b-1765b420b/)
        - 💻 **GitHub:** [saimanasaB](https://github.com/saimanasaB)
        """)

# ----------------- Experience -----------------
elif page_name == "Experience":
    st.markdown("# 💼 Professional Experience")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Timeline Item
    st.markdown("""
    <div class='timeline-item'>
        <h3>API (Backend) Developer</h3>
        <p style='font-style: italic; margin: 5px 0;'>Satyukt Analytics Pvt. Ltd, Bengaluru</p>
        <p style='font-size: 14px; margin-bottom: 15px;'>📅 December 2024 – Present</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Achievements
    st.markdown("### 🎯 Key Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='project-card'>
            <h4>🚀 API Development & Deployment</h4>
            <ul>
                <li>Architected and deployed <strong>70+ REST APIs</strong> using FastAPI and MySQL on AWS Lambda</li>
                <li>Supporting <strong>1000+ active users</strong> and handling <strong>3000+ daily requests</strong></li>
                <li>Configured AWS Lambda with API Gateway custom domain and Lambda Layers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='project-card'>
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
        <div class='project-card'>
            <h4>💾 Database Architecture</h4>
            <ul>
                <li>Designed MySQL database schema with <strong>15+ normalized tables</strong></li>
                <li>Optimized queries reducing response time from 850ms to 340ms (<strong>60% improvement</strong>)</li>
                <li>Built multi-role platform supporting 6 user types</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='project-card'>
            <h4>🛰️ Specialized Development</h4>
            <ul>
                <li>Developed RESTful APIs for <strong>satellite data retrieval</strong></li>
                <li>Implemented geospatial coordinate processing</li>
                <li>Integrated real-time data processing pipelines</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ----------------- Projects -----------------
elif page_name == "Projects":
    st.markdown("# 🚀 Key Projects")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sat2Farm Project
    st.markdown("""
    <div class='project-card'>
        <h2>🌾 Sat2Farm - Agricultural Monitoring Platform</h2>
        <div class='tech-badge'>
            <strong>Tech Stack:</strong> FastAPI | MySQL | AWS S3 | Satellite APIs
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Core Features:**
        - Built backend with **25+ REST APIs**
        - Serving **1000+ farmers**
        - Managing **1500+ farm plots**
        - Real-time crop health monitoring (NDVI)
        """)
    
    with col2:
        st.markdown("""
        **⚡ Key Implementations:**
        - Integrated satellite data APIs
        - Soil analysis and weather forecasting
        - Farm CRUD with polygon validation
        - Image advisory system with AWS S3
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Say Trees Project
    st.markdown("""
    <div class='project-card'>
        <h2>🌳 Say Trees - Tree Plantation Management</h2>
        <div class='tech-badge'>
            <strong>Tech Stack:</strong> FastAPI | AWS Lambda | MySQL | API Gateway
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Architecture:**
        - Designed schema with **15+ normalized tables**
        - Deployed **35+ APIs** on AWS Lambda
        - Built role-based access for **5 user types**
        """)
    
    with col2:
        st.markdown("""
        **⚡ Order Lifecycle Management:**
        - Sapling ordering system
        - Inventory validation
        - Logistics assignment
        - Real-time delivery tracking
        """)

# ----------------- Skills -----------------
elif page_name == "Skills":
    st.markdown("# ⚡ Technical Skills")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Skill categories
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🐍 Backend & Frameworks")
        st.markdown("""
        <span class='skill-badge'>Python</span>
        <span class='skill-badge'>FastAPI</span>
        <span class='skill-badge'>Flask</span>
        <span class='skill-badge'>REST APIs</span>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 💾 Database")
        st.markdown("""
        <span class='skill-badge'>MySQL</span>
        <span class='skill-badge'>SQL</span>
        <span class='skill-badge'>Database Design</span>
        <span class='skill-badge'>Query Optimization</span>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ☁️ Cloud & DevOps")
        st.markdown("""
        <span class='skill-badge'>AWS Lambda</span>
        <span class='skill-badge'>API Gateway</span>
        <span class='skill-badge'>S3</span>
        <span class='skill-badge'>Linux/Ubuntu</span>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🛠️ Tools & Other")
        st.markdown("""
        <span class='skill-badge'>Git</span>
        <span class='skill-badge'>JWT</span>
        <span class='skill-badge'>Geospatial APIs</span>
        <span class='skill-badge'>Serverless</span>
        """, unsafe_allow_html=True)

# ----------------- Contact -----------------
elif page_name == "Contact":
    st.markdown("# 📧 Get In Touch")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Send Me a Message")
        st.markdown("I'd love to hear from you! Whether you have a question or just want to say hi, feel free to reach out.")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", placeholder="John Doe")
            email = st.text_input("Your Email", placeholder="john@example.com")
            subject = st.selectbox("Subject", ["General Inquiry", "Job Opportunity", "Project Collaboration", "Other"])
            message = st.text_area("Your Message", placeholder="Write your message here...", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀")
            
            if submitted:
                if name and email and message:
                    st.success(f"✅ Thanks {name}! Your message has been sent successfully. I'll get back to you soon!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
    
    with col2:
        st.markdown("### 📍 Contact Information")
        st.markdown("""
        <div class='contact-card'>
            <p><strong>📧 Email</strong><br/>saimanasab10@gmail.com</p>
            <p><strong>📞 Phone</strong><br/>+91 8667564076</p>
            <p><strong>💼 LinkedIn</strong><br/><a href='https://www.linkedin.com/in/sai-manasa-b-1765b420b/'>Sai Manasa</a></p>
            <p><strong>💻 GitHub</strong><br/><a href='https://github.com/saimanasaB'>saimanasaB</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### ⏰ Response Time")
        st.info("I typically respond within 24-48 hours.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='color: #8b949e;'>© 2025 Sai Manasa B | Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
