
import streamlit as st
from streamlit_option_menu import option_menu
import os

TITLE_WEBAPP = "Visitor Monitoring Webapp"
IMAGE_LINK = "https://www.example.com/image.jpg"

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title=TITLE_WEBAPP,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.example.com/help',
            'Report a bug': 'https://www.example.com/bug',
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    
    set_custom_css()
    option = set_sidebar_menu()
    
    if option == "Upload":
        handle_upload()
    elif option == "Settings":
        show_settings()
    else:
        show_home()
        
def set_custom_css():
    """Function to set custom CSS for the Streamlit app."""
    st.markdown(f"""
        <style>
            .main .block-container{{
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}
            .stApp {{
                background: linear-gradient(to bottom, #f8f8f8, #ffffff);
            }}
            .css-1n543e5 {{
                margin-top: -50px;
                text-align: center;
            }}
        </style>
    """, unsafe_allow_html=True)

def set_sidebar_menu():
    """Function to set the sidebar menu."""
    return option_menu(
        menu_title="Main Menu", 
        options=["Home", "Upload", "Settings"],
        icons=["house", "cloud-upload", "gear"],
        menu_icon="cast",
        default_index=0,
    )

def handle_upload():
    """Function to handle file uploads."""
    st.subheader("Upload your file")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        process_file(uploaded_file)
        
def process_file(uploaded_file):
    """Function to process the uploaded file."""
    try:
        os.makedirs("uploads", exist_ok=True)
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully")
    except Exception as e:
        st.error(f"Failed to upload file: {e}")

def show_settings():
    """Function to display settings."""
    st.subheader("Settings")
    st.text("Here you can adjust the settings of your app.")

def show_home():
    """Function to display the home page."""
    st.title("Welcome to the Visitor Monitoring Webapp")
    st.markdown(f"""
        <img src="{IMAGE_LINK}" alt="Visitor Monitoring" style="width:100%; height:auto;">
    """, unsafe_allow_html=True)
    st.markdown("""
        ## About
        This webapp is designed to help you monitor and manage visitors efficiently.
        ### Features:
        - Upload visitor data
        - Customize settings
        - Monitor visitor activities
    """)

if __name__ == "__main__":
    main()
