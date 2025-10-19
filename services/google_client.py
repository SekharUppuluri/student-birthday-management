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
    sa_info = st.secrets["google_service_account"]
    creds = Credentials.from_service_account_info(sa_info, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client
