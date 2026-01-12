import streamlit as st

# --- Configuration and Styling ---
st.set_page_config(
    page_title="Apeiron Capital Hub",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for a Modern & Elegant Look ---
st.markdown(
    """
    <style>
    /* Global Font & Color Variables */
    :root {
        --primary-color: #6b2124; /* Apeiron Capital Maroon */
        --secondary-color: #f8f9fa; /* Light Background */
        --text-color: #333333;
        --font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* General Styles */
    body {
        font-family: var(--font-family);
        color: var(--text-color);
        background-color: var(--secondary-color);
    }
    .stApp {
        background-color: var(--secondary-color);
    }

    /* 1. Header Styling */
    .header-container {
        display: flex;
        align-items: center;
        padding-bottom: 30px;
        border-bottom: 2px solid #e0e0e0;
        margin-bottom: 40px;
    }
    .logo-img {
        height: 80px; /* Adjust as needed */
        margin-right: 30px;
    }
    .header-text {
        display: flex;
        flex-direction: column;
    }
    .big-font {
        font-size: 42px !important;
        font-weight: 300; /* Lighter weight for elegance */
        color: var(--primary-color);
        margin: 0;
        letter-spacing: 1px;
    }
    .sub-font {
        font-size: 18px !important;
        font-weight: 400;
        color: #777;
        margin: 10px 0 0 0;
    }

    /* 2. Card Styling */
    .app-card {
        padding: 40px;
        border-radius: 16px;
        background-color: #ffffff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08); /* Softer, deeper shadow */
        transition: all 0.3s ease;
        min-height: 280px; /* Minimum height for consistency */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: none; /* Clean look */
        margin-bottom: 20px; /* Spacing between rows */
        overflow: visible; /* Ensure content is not clipped */
    }
    
    .app-card:hover {
        transform: translateY(-7px);
        box-shadow: 0 20px 40px rgba(107, 33, 36, 0.15); /* Shadow with primary color hint */
    }

    .card-icon {
        font-size: 48px;
        margin-bottom: 20px;
        color: var(--primary-color);
    }
    .card-title {
        font-size: 24px;
        font-weight: 500;
        color: var(--text-color);
        margin: 0 0 15px 0;
    }
    .card-desc {
        color: #666;
        font-size: 16px;
        line-height: 1.6;
        flex-grow: 1; /* Allows description to take up space */
    }

    /* 3. Button Styling */
    .launch-btn {
        background-color: var(--primary-color); 
        color: white !important;
        border: none;
        padding: 14px 28px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-size: 16px;
        border-radius: 8px;
        width: 100%;
        margin-top: 30px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s;
        box-shadow: 0 4px 12px rgba(107, 33, 36, 0.2);
    }
    .launch-btn:hover {
        background-color: #51181b; /* Slightly darker maroon */
        text-decoration: none;
    }

    /* 4. Sidebar & Footer */
    .css-1d391kg { /* Sidebar class */
        background-color: #ffffff;
    }
    .footer {
        text-align: center; 
        color: #999; 
        font-size: 14px; 
        padding: 30px 0; 
        border-top: 1px solid #e0e0e0;
        margin-top: 50px;
    }
    /* Remove default container padding for a cleaner top */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Definitions ---
apps = [
    {
        "name": "A/H Premium Analysis",
        "url": "https://ahpremium.streamlit.app/",
        "icon": "A/H",
        "description": "Real-time tracking of price disparities between Chinese A-shares and H-shares. "
    },
    {
        "name": "Portfolio Simulator",
        "url": "https://simportfolio.streamlit.app/",
        "icon": "💼",
        "description": "A comprehensive simulation environment for tracking analyst performance and managing positions"
    },
    {
    "name": "Trade Analysis",
    "url": "https://protradesys.streamlit.app/",
    "icon": "📊",
    "description": "Deep dive into historical trade records and visualize the entry and exits of each trade"
},
    {
    "name": "Add Watermark",
    "url": "https://addwatermark.streamlit.app/",
    "icon": "📜",
    "description": "Add watermark to PDF files"
},
    {
    "name": "Trade Cost",
    "url": "https://tradecost.streamlit.app/",
    "icon": "💰",
    "description": "Analyze and calculate trading costs"
}
]

# --- Sidebar Navigation ---
with st.sidebar:
    # UPDATED: Replaced use_column_width with use_container_width
    st.image("image_0.png", use_container_width=True) 
    st.markdown("### Navigation")
    for app in apps:
        st.markdown(f"[{app['icon']} {app['name']}]({app['url']})")
    st.markdown("---")
    st.caption("© 2025 Apeiron Capital")


# --- Main Content Area ---

# 1. Header with Logo
# Using columns to place the logo and text side-by-side nicely
col1, col2 = st.columns([1, 5])
with col1:
    st.image("image_0.png", width=180) # Adjust width as needed
with col2:
    st.markdown(
        """
        <div class="header-text" style="margin-left: 20px; display: flex; flex-direction: column; justify-content: center; height: 100%;">
            
            
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='margin-bottom: 60px;'></div>", unsafe_allow_html=True) # Spacer

# 2. Application Cards - Display 3 per row
CARDS_PER_ROW = 3

for row_start in range(0, len(apps), CARDS_PER_ROW):
    cols = st.columns(CARDS_PER_ROW)
    for i, col in enumerate(cols):
        app_index = row_start + i
        if app_index < len(apps):
            app = apps[app_index]
            with col:
                st.markdown(
                    f"""
                    <div class="app-card">
                        <div>
                            <div class="card-icon">{app['icon']}</div>
                            <h2 class="card-title">{app['name']}</h2>
                            <p class="card-desc">{app['description']}</p>
                        </div>
                        <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                            <div class="launch-btn">Launch Application</div>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    # Add spacer between rows
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)







