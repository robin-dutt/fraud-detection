import streamlit as st
import dashboard
import classifyPage

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
