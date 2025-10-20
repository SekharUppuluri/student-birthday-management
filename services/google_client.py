"""
Handles Google API authentication and returns an authorized gspread client
"""
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Access Scope
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_gspread_client():
    """ 
    Initialize and return an authorized gspread client using Streamlit secrets
    """
    try:
        # This works for both local and cloud as long as secrets are properly set up
        sa_info = st.secrets["google_service_account"]
        creds = Credentials.from_service_account_info(sa_info, scopes=SCOPES)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error("Failed to connect to Google Sheets API")
        st.error(f"Error details: {str(e)}")
        st.info("Please check your credentials in .streamlit/secrets.toml (local) or Streamlit Cloud secrets")
        st.stop()