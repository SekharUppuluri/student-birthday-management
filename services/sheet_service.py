"""
Handles all Google Sheets read/write operations for the Student Birthday Management System
"""
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from .google_client import get_gspread_client

SPREADSHEET_NAME = "Student Data"

def get_worksheet(sheet_name="Sheet1"):
    """Open the Google Sheet and return the specified worksheet"""
    try:
        client = get_gspread_client()
        spreadsheet = client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.worksheet(sheet_name)
        return worksheet
    except Exception as e:
        import streamlit as st
        st.error("⚠️ Could not connect to Google Sheet. Please verify name & credentials.")
        st.error(str(e))
        st.stop()


def fetch_all_students():
    """ Fetch all student records as a list of dictionaries """
    worksheet = get_worksheet()
    return worksheet.get_all_records()

def add_student_record(student_data: dict):
    """Add a new student record to the sheet in correct column order."""
    worksheet = get_worksheet()
    if not worksheet:
        return False
    try:
        headers = worksheet.row_values(1)
        new_row = [student_data.get(h, "") for h in headers]
        worksheet.append_row(new_row)
        print(f"✅ Added student: {student_data.get('Name', 'Unknown')}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to add student: {e}")
        return False


def update_student_record(row_number : int , updated_student_data : dict ):
    """ Update an existing student record """
    worksheet = get_worksheet()
    headers = worksheet.row_values(1)
    for idx  , key in enumerate( headers  , start = 1):
        if key in updated_student_data :
            worksheet.update_cell(row_number  , idx  , updated_student_data[key])