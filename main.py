import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import dashboard
import aboutus

# Load environment variables
load_dotenv()

# Set up the page configuration
st.set_page_config(page_title="SmartBin")

# Google Analytics setup (ensure the tag is correct)
analytics_tag = os.getenv('analytics_tag')
if analytics_tag:
    st.markdown(
        f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={analytics_tag}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{analytics_tag}');
        </script>
        """,
        unsafe_allow_html=True
    )

# Initialize the app management class
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar with navigation
        with st.sidebar:        
            app = option_menu(
                menu_title='SmartBin',
                options=['Home', 'About'],
                icons=['house-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Load the appropriate app based on the selection
        if app == "Home":
            dashboard.app()
        elif app == 'About':
            aboutus.app()

# Run the multi-app manager
if __name__ == "__main__":
    app = MultiApp()
    app.run()
