"""
Manage student data Operations using Google Sheets as backend
"""
import streamlit as st

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
        st.warning("no students")
        return
    st.write(" all registered students ")
    for s in students :
        st.write(f"{s['Name']} - {s['DOB']}")
    st.info(f"total students : {len(students)}")

def search_student(roll_no):
    """Finding a student by Roll Number"""
    students = fetch_all_students()
    if not students:
        st.warning("No students found.")
        return

    roll_no = str(roll_no).strip().lower()

    for s in students:
        # Normalize roll numbers before comparison
        sheet_roll = str(s.get("Roll No", "")).strip().lower()
        if sheet_roll == roll_no:
            st.success("✅ Student Found!")
            st.table([s])  # neatly display single student record
            return  # <-- inside the IF block

    # runs only if no match found
    st.error(f"❌ Student with Roll No '{roll_no}' not found.")



def edit_student(roll_no , update_data):
    """ Edit a student details (by Roll Number...) """
    students = fetch_all_students()
    for idx , s in enumerate( students , start = 2):
        if s['Roll No'] == roll_no:
            success = update_student_record(idx , update_data )
            if success:
                st.write(f" updated record for {s['Name']} ")
            return
    st.warning("student not found")