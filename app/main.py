import streamlit as st

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.student_manager import register_student, view_all_students, search_student
 

st.set_page_config(page_title= "Student Birthday Management", layout="wide")
st.title("🎓 Student Birthday Management System")

menu = ["Home","Register Student","View Students","Search Student" ]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Welcome: Use the menu to navigate")
elif choice == "Register Student":
    st.subheader("Register a New Student")
    name = st.text_input("Name")
    roll_no = st.text_input("Roll Number")
    course = st.text_input("Course")
    year = st.number_input("Year",min_value= 1 , max_value= 6)
    section = st.text_input("Section")
    dob = st.date_input("Date of Birth")
    promise_note = st.text_area("Promise Note")

    if st.button("Register"):
        dob_str = dob.strftime("%d-%m-%Y")
        student = {
            "Roll No" :roll_no ,
            "Name" : name ,
            "Course" : course ,
            "Year" : year ,
            "Section" : section ,
            "DOB" : dob_str ,
            "Promise Note" : promise_note
        }
        register_student(student)
        st.success(f"Student {name} registerd! ")
elif choice == "View Students":
    st.subheader("All Students")
    view_all_students()
elif choice == "Search Student":
    st.subheader("Search Student by Roll NUmber")
    roll_no = st.text_input("Enter ROll Number")
    if st.button("Search"):
        search_student(roll_no)