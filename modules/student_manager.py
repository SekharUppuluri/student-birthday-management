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

def view_all_students():
    """ Fetch and display all students """
    students = fetch_all_students()
    if not students :
        print("no students")
        return
    print("\n all registered students ")
    for s in students :
        print(f"{s['Name']} - {s['DOB']}")
    print(f"total students : {len(students)}")