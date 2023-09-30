import streamlit as st
import dashboard
import classifyPage

# Add custom CSS to style the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa; /* Background color */
        padding: 20px; /* Padding inside the sidebar */
        border-radius: 10px; /* Rounded corners */
    }
    .sidebar .sidebar-content .sidebar-radio {
        margin-top: 10px; /* Margin between radio buttons */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set Streamlit page configuration
st.set_page_config(
    page_title="Deforgify",
    page_icon="🤖",
    layout="wide"
)

# Define the pages and icons
PAGES = {
    "Dashboard": {"page": dashboard, "icon": "📊"},
    "Classify Image": {"page": classifyPage, "icon": "🖼️"}
}

# Sidebar styling
st.sidebar.title("SAFIRE")
st.sidebar.markdown("SAFIRE is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones.")
st.sidebar.subheader('Navigation')

# Radio buttons for page selection with icons
selection = st.sidebar.radio("", list(PAGES.keys()), format_func=lambda page_name: f"{PAGES[page_name]['icon']} {page_name}")

# Get the selected page and its corresponding icon
selected_page = PAGES[selection]['page']

# Display the selected page
selected_page.app()
