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

# Sidebar styling using custom CSS
st.sidebar.title("SAFIRE")
st.sidebar.markdown("SAFIRE is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones.")
st.sidebar.subheader('Navigation')

# Radio buttons for page selection with icons
selection = st.sidebar.radio("", list(PAGES.keys()), format_func=lambda page_name: f"{PAGES[page_name]['icon']} {page_name}")

# Get the selected page and its corresponding icon
selected_page = PAGES[selection]['page']

# Apply custom CSS styles
custom_css = """
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
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Display the selected page
selected_page.app()
