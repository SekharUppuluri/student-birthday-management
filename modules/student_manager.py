"""
Manage student data Operations using Google Sheets as backend
"""
import streamlit as st
import pandas as pd
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
    if not students:
        st.warning("No students found.")
        return
    st.write("All registered students:")
    # Convert to DataFrame for proper table display
    df = pd.DataFrame(students)
    st.dataframe(df, hide_index=True)
    st.info(f"Total students: {len(students)}")


def search_student(roll_no):
    """Finding a student by Roll Number"""
    students = fetch_all_students()
    if not students:
        st.warning("No students found.")
        return
    roll_no = str(roll_no).strip().lower()
    found = None
    for s in students:
        sheet_roll = str(s.get("Roll No", "")).strip().lower()
        if sheet_roll == roll_no:
            found = s
            break
    if found:
        st.success(f"✅ Student Found: {found['Name']}")
        st.markdown("### Student Details")
        st.dataframe(pd.DataFrame([found]), hide_index=True)
    else:
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