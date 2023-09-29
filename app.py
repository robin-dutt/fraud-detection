import streamlit as st
import dashboard
import classifyPage

st.set_page_config(
    page_title="Deforgify",
    page_icon="🤖",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    "Classify Image": classifyPage
}

st.sidebar.title("SAFIRE")

st.sidebar.write("SAFIRE is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones.")

st.sidebar.subheader('Navigation')

# Define icons for the buttons
dashboard_icon = "📊"
classify_icon = "🖼️"

# Use HTML to include icons with the buttons
if st.sidebar.button(f"{dashboard_icon} Dashboard"):
    page = PAGES["Dashboard"]
    page.app()

if st.sidebar.button(f"{classify_icon} Classify Image"):
    page = PAGES["Classify Image"]
    page.app()
