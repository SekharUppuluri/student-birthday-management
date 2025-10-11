"""
Manage student data Operations using Google Sheets as backend
"""
from services.sheet_service import fetch_all_students, add_student_record, update_student_record

def register_student(student):
    """ Adding a new student record to Google Sheet """
    success = add_student_record(student)
    if success :
        print(f" student {student['Name']} added successfully ")
    else:
        print("Failed to add student")