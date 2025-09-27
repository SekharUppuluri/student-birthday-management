# 🎂 Student Birthday Management System

## 1. Overview
This project is a menu-driven Python application that manages student records and identifies students whose birthdays fall on the current date.  
It demonstrates practical usage of Python fundamentals such as:
- Conditional statements  
- Loops  
- Lists & dictionaries  
- File handling  
- Modules (datetime, json, os)  

The project has been designed with real-world software development practices: structured documentation, modular code, and extendable architecture.

---

## 2. Problem Statement
The system should:
1. Register new students and store their details.  
2. Check if any students have birthdays on the current day.  
3. Display and save today’s birthday list.  
4. Exit safely when required.  

All records must be persisted in files for future access.

---

## 3. Core Features (MVP ✅)
- Register a student with details:
  - Roll Number  
  - Name  
  - Course  
  - Year  
  - Section  
  - Date of Birth (dd-mm-yyyy)  
  - Promise Distribution (custom note)  
- Save each record as a JSON string in students.txt.  
- Birthday check:
  - Compare DOB with today’s date (day & month).  
  - Print details on screen.  
  - Save results into a new file named as DD-MM-YYYY.txt.  
- Exit the application.

---

## 4. Future Enhancements (Scalable 🚀)
This project is intentionally kept simple but can be extended:
- Update or delete student records.  
- Search by roll number or name.  
- Display all students in a table format.  
- Upcoming birthdays reminder (next 7 days).  
- GUI / Web interface using Streamlit or Flask.  
- Integration with Google Sheets or SQL Database.  
- Dockerized deployment for portability.  

---

## 5. System Design

### 5.1 Data Structure
Each student is stored as a Python dictionary:
```python
{
  "rollno": "1",
  "name": "Amit",
  "course": "MCA",
  "year": "2025",
  "section": "A",
  "dob": "23-09-2002",
  "promise": "Will distribute chocolates 🎉"
}
