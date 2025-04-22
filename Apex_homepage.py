import streamlit as st
import base64 # Needed for the logo method from Code 1
from pathlib import Path
import os # Still useful for checking file existence

# -----------------------------------------------------------------------------
# Configuration (Adapted from Code 2, using Code 1's specifics where needed)
# -----------------------------------------------------------------------------

# --- Page Config ---
st.set_page_config(
    page_title="Phronesis Apex", # From Code 1
    page_icon="📊",             # From Code 1
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- App Details (From Code 1) ---
APP1_NAME = "Response Analysis App"
APP1_DESC = "Analyzes the contextual relevance of Open Ends to Survey Questions."
APP1_URL = "#insight-hub" # Use '#' or actual links if available

APP2_NAME = "AI Themer"
APP2_DESC = "Topic modelling for Open-Ended responses."
APP2_URL = "#strategy-forge" # Use '#' or actual links if available

# --- Logo Configuration ---
# Use the logo file path and loading method from Code 1
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
LOGO_PATH = current_dir / "apexlogo.png" # Path from Code 1

# Function to load and encode image to base64 (from Code 1)
def get_base64_of_bin_file(bin_file):
    try:
        # Ensure the path is treated as a string for open()
        with open(str(bin_file), 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        # Use st.warning for less intrusive error display in app
        st.warning(f"Warning: Logo file not found at {bin_file}")
        return None
    except Exception as e:
        st.error(f"Error loading logo: {e}")
        return None

logo_base64 = get_base64_of_bin_file(LOGO_PATH)
# Use a placeholder div if logo fails to load (from Code 1)
logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="Phronesis Apex Logo" class="logo">' if logo_base64 else '<div class="logo-placeholder">Logo</div>'


# --- Style Configuration (Variables primarily from Code 2 theme, adapted) ---
PRIMARY_ACCENT_COLOR = "#cd669b"  # Pinkish from Code 1's --primary-color
PRIMARY_ACCENT_COLOR_RGB = "205, 102, 155" # RGB for the pinkish color

CARD_TEXT_COLOR = "#a9b4d2"       # From Code 1's --text-medium
CARD_TITLE_TEXT_COLOR = PRIMARY_ACCENT_COLOR # Use Primary Accent for Card Title

MAIN_TITLE_COLOR = "#f0f8ff" # From Code 1's --text-light
BODY_TEXT_COLOR = "#a9b4d2"  # From Code 1's --text-medium
SUBTITLE_COLOR = "#8b98b8"   # Slightly adjusted medium text color

MAIN_BACKGROUND_COLOR = "#0b132b" # From Code 1 --background-color
CARD_BACKGROUND_COLOR = "#1c2541" # From Code 1 --card-background
HOVER_GLOW_COLOR = f"rgba({PRIMARY_ACCENT_COLOR_RGB}, 0.4)" # Glow effect color

# Optional: Card background image from Code 2 - set to None if not desired
CARD_BACKGROUND_IMAGE_URL = None # "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1000&q=80"
WHITE_OVERLAY_OPACITY_STATIC = 0 # Set to 0 if not using white overlay on cards
WHITE_OVERLAY_OPACITY_HOVER = 0 # Set to 0 if not using white overlay on cards
WHITE_RGB = "255, 255, 255"

CONTAINER_BG_COLOR = "rgba(11, 19, 43, 0.0)" # Transparent, rely on body background
CONTAINER_BORDER_RADIUS = "15px"

# --- Font Families (Consolidated from Code 2) ---
TITLE_FONT = "'Montserrat', sans-serif" # Or 'Orbitron'
BODY_FONT = "'Roboto', sans-serif"
CARD_TITLE_FONT = "'Montserrat', sans-serif"

# -----------------------------------------------------------------------------
# Styling (CSS) - Base from Code 2, Header/Logo/Title section from Code 1
# -----------------------------------------------------------------------------

st.markdown(f"""
<style>
    /* --- Import Fonts (From Code 2) --- */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap');

    /* --- Streamlit Main Page Background --- */
    body {{
        background-color: {MAIN_BACKGROUND_COLOR};
        min-height: 100vh;
        color: {BODY_TEXT_COLOR};
        font-family: {BODY_FONT};
    }}

    /* Make Streamlit header transparent */
    .stApp > header {{
        background-color: transparent;
    }}

    /* --- Streamlit Block Container Styling --- */
    .main .block-container {{
        max-width: 1100px; /* Max width from Code 1 */
        padding: 2rem 1rem 4rem 1rem; /* Padding closer to Code 1 */
        background-color: {CONTAINER_BG_COLOR};
        border-radius: {CONTAINER_BORDER_RADIUS};
        color: {BODY_TEXT_COLOR};
        margin: auto;
    }}

    /* --- Header Section - Adopted from Code 1 --- */
    .header-container {{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        margin-bottom: 4rem;
        text-align: left; /* Text aligns left relative to logo */
    }}

    .logo {{
        height: 100px;          /* ADJUST height as needed */
        width: auto;
        margin-right: 1.5rem;   /* Space between logo and title */
        margin-bottom: 0;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        flex-shrink: 0;
        vertical-align: middle; /* Helps alignment */
    }}

    /* Style for placeholder if logo fails (from Code 1) */
    .logo-placeholder {{
        height: 80px;  /* Adjust placeholder size */
        width: 80px;
        margin-right: 1.5rem;
        background-color: #333;
        border: 1px dashed #555;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888;
        font-size: 0.9em;
        text-align: center;
        border-radius: 5px;
        flex-shrink: 0;
    }}

    .title {{ /* Styling for H1 title from Code 1 structure */
        font-family: {TITLE_FONT}; /* Use configured title font */
        font-size: 2.8rem;     /* Adjust size as needed */
        font-weight: 700;
        color: {MAIN_TITLE_COLOR}; /* Use configured title color */
        letter-spacing: 1px;
        margin: 0;
        padding: 0; /* Ensure no extra padding */
        line-height: 1.2;
        text-shadow: 0 0 8px rgba({PRIMARY_ACCENT_COLOR_RGB}, 0.3); /* Optional subtle glow */
    }}
    /* --- End Header Section --- */


    /* --- Subtitle Styling (Optional - from Code 2, if needed later) --- */
    /* .launcher-subtitle {{ ... }} */

    /* --- App Card Link Styling (From Code 2) --- */
    .app-card-link {{
        text-decoration: none !important;
        display: block;
        height: 100%;
        color: inherit;
    }}
    .app-card-link:hover {{
        text-decoration: none !important;
    }}

    /* --- App Card Styling (Adapted from Code 2 using Code 1 colors/style) --- */
    /* Uses 'app-card' class now, matching the HTML below */
    .app-card {{
        background-color: {CARD_BACKGROUND_COLOR};
        {'background-image: linear-gradient(rgba({WHITE_RGB}, {WHITE_OVERLAY_OPACITY_STATIC}), rgba({WHITE_RGB}, {WHITE_OVERLAY_OPACITY_STATIC})), url("{CARD_BACKGROUND_IMAGE_URL}");' if CARD_BACKGROUND_IMAGE_URL and WHITE_OVERLAY_OPACITY_STATIC > 0 else ''}
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;

        border: 2px solid transparent;
        border-radius: 15px;
        padding: 2rem 1.5rem;
        margin: 0; /* Remove potential column margins */
        text-align: left;
        transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1),
                    box-shadow 0.4s cubic-bezier(0.25, 0.8, 0.25, 1),
                    border-color 0.4s ease,
                    background-color 0.4s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        min-height: 230px; /* Adjusted height */
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;
        cursor: pointer;
        height: 100%; /* Make card fill column space */
    }}

    /* --- Card Hover Animation --- */
    .app-card:hover {{
        transform: translateY(-10px);
        border-color: {PRIMARY_ACCENT_COLOR};
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3), 0 0 20px {HOVER_GLOW_COLOR};

        {'background-image: linear-gradient(rgba({WHITE_RGB}, {WHITE_OVERLAY_OPACITY_HOVER}), rgba({WHITE_RGB}, {WHITE_OVERLAY_OPACITY_HOVER})), url("{CARD_BACKGROUND_IMAGE_URL}");' if CARD_BACKGROUND_IMAGE_URL and WHITE_OVERLAY_OPACITY_HOVER > 0 else ''}
        background-color: {CARD_BACKGROUND_COLOR};
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
    }}

    /* --- Card Content (Title and Paragraph) --- */
    /* Renaming selectors to match HTML structure below */
    .app-card .card-title {{ /* Targeting H2 inside app-card */
        font-family: {CARD_TITLE_FONT};
        font-weight: 600;
        color: {CARD_TITLE_TEXT_COLOR};
        font-size: 1.6rem; /* From Code 1 card-title */
        margin-bottom: 0.8rem;
        margin-top: 0;
        text-shadow: none;
        z-index: 1;
        position: relative;
    }}

    .app-card .card-description {{ /* Targeting P inside app-card */
        font-family: {BODY_FONT};
        color: {CARD_TEXT_COLOR};
        font-size: 0.95rem; /* From Code 1 card-description */
        line-height: 1.6;
        margin: 0;
        margin-bottom: 2.5rem; /* Space before arrow */
        text-shadow: none;
        z-index: 1;
        position: relative;
        flex-grow: 1;
    }}

    /* Arrow from Code 1 */
    .card-arrow {{
        position: absolute;
        bottom: 1.5rem;
        right: 1.5rem;
        font-size: 1.5rem;
        color: {PRIMARY_ACCENT_COLOR}; /* Use accent color */
        opacity: 0;
        transform: translateX(-10px);
        transition: opacity 0.3s ease, transform 0.3s ease;
        z-index: 2;
    }}

    .app-card:hover .card-arrow {{
        opacity: 1;
        transform: translateX(0);
    }}


    /* --- Footer Styling (Using Code 1's class name & margins) --- */
    .footer {{
        text-align: center;
        color: {SUBTITLE_COLOR};
        opacity: 0.7;
        margin: 4rem auto 1rem auto; /* Margins from Code 1 */
        font-size: 0.9rem;
        max-width: 1100px; /* Match block container */
        padding-bottom: 1rem; /* Ensure some space at bottom */
    }}

    /* --- Responsive Adjustments (Combining rules) --- */
    @media (max-width: 768px) {{
        .main .block-container {{
            padding: 2rem 1rem 3rem 1rem;
        }}
        .header-container {{
            margin-bottom: 3rem;
            /* Optional: Stack logo/title earlier if needed */
            /* flex-direction: column; */
            /* text-align: center; */
            /* gap: 0.5rem; */
        }}
        .logo {{ height: 80px; margin-right: 1rem;}} /* Code 1 responsive logo */
        .logo-placeholder {{ height: 80px; width: 80px; margin-right: 1rem; }}
        .title {{ font-size: 2.2rem; }} /* Adjusted title size */

        .app-card {{
            min-height: 200px;
            padding: 1.5rem 1rem;
            margin-bottom: 20px;
        }}
        .app-card .card-title {{ font-size: 1.4rem; }}
        .app-card .card-description {{ font-size: 0.9rem; margin-bottom: 2rem; }}
        .footer {{ margin-top: 2rem; font-size: 0.8rem; }}
    }}

    @media (max-width: 480px) {{
        .header-container {{
             flex-direction: column; /* Stack on very small screens */
             text-align: center;
             gap: 0.8rem; /* Add gap when stacked */
             margin-bottom: 2.5rem;
        }}
         .logo {{
            margin-right: 0;
            margin-bottom: 0; /* Remove bottom margin if gap is used */
            height: 60px; /* Code 1 responsive logo */
        }}
         .logo-placeholder {{
            margin-right: 0;
            margin-bottom: 0;
            height: 60px;
            width: 60px;
        }}
        .title {{ font-size: 2rem; }} /* Adjusted title size */

        /* Cards will stack naturally due to columns */
        .app-card {{
            min-height: 180px;
        }}
         .app-card .card-title {{ font-size: 1.3rem; }}
         .app-card .card-description {{ font-size: 0.85rem; }}
    }}

    /* Targeting Streamlit's built-in elements for cleanup */
    header[data-testid="stHeader"] {{
        display: none !important;
    }}
    footer {{ /* Hide default footers */
        display: none !important;
    }}
    div[data-testid="stDecoration"] {{ /* Hide "Made with Streamlit" */
         display: none !important;
     }}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# App Layout (Using Code 1's Header Structure)
# -----------------------------------------------------------------------------

# --- Header Section ---
# Use the exact markdown structure from Code 1
st.markdown(
    f"""
    <div class="header-container">
        {logo_html}
        <h1 class="title">Phronesis Apex</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# --- App Launchers using Columns ---
# Use columns like before, but ensure card HTML uses consistent classes
col1, col2 = st.columns(2, gap="large")

# --- App 1 Card ---
with col1:
    # Use a structure that matches the CSS selectors (.app-card, .card-title, etc.)
    app1_html = f"""
    <a href="{APP1_URL}" target="_self" class="app-card-link" title="{APP1_DESC}">
        <div class="app-card">
            <h2 class="card-title">{APP1_NAME}</h2>
            <p class="card-description">{APP1_DESC}</p>
            <span class="card-arrow">→</span>
        </div>
    </a>
    """
    st.markdown(app1_html, unsafe_allow_html=True)

# --- App 2 Card ---
with col2:
    # Use a structure that matches the CSS selectors (.app-card, .card-title, etc.)
    app2_html = f"""
    <a href="{APP2_URL}" target="_self" class="app-card-link" title="{APP2_DESC}">
        <div class="app-card">
            <h2 class="card-title">{APP2_NAME}</h2>
            <p class="card-description">{APP2_DESC}</p>
            <span class="card-arrow">→</span>
        </div>
    </a>
    """
    st.markdown(app2_html, unsafe_allow_html=True)


# --- Footer ---
# Use the footer class from Code 1's structure/CSS
st.markdown(
    f"""
    <div class="footer">
        <p>© 2025 Phronesis Partners. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)