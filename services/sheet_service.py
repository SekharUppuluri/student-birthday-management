"""
Handles all Google Sheets read/write operations for the Student Birthday Management System
"""
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from .google_client import get_gspread_client

SPREADSHEET_NAME = "Student Data"

def get_worksheet(sheet_name = "sheet1"):
    """ Open the Google Sheet and return the specified worksheet """
    client = get_gspread_client()
    spreadsheet = client.open(SPREADSHEET_NAME)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet
