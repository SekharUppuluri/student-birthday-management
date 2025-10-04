# internal requirements
import json
import os
from datetime import datetime
import sys

# external requirements

# constants
DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
   os.makedirs(DATA_DIR)

STUDENTS_FILE = os.path.join( DATA_DIR , "students.txt" )
# functions
def register_student():
   """ Register a new student and save to file with validations """
   print()
   print("\n --- Welcome to Registration Section --- \n")
   student = {}
   # --- Roll Number ---
   roll_no = input("Enter Roll Number : ").strip()
   student["roll_no"] = roll_no
   # --- Name ---
   name = input("Enter Name : ").strip()
   student["Name"] = name 
   # --- Course ---
   course = input("Enter Course : ").strip()
   student["Course"] = course 
   # --- Year ---
   year = input("Enter Year (1/2/3/4) : ").strip()
   student["year"] = year
   # --- Date of Birth ---
   dob = input("Enter Date of Birth (DD-MM-YYYY) : ").strip()
   student["DOB"] = dob
   # --- promise ---
   promise = input("Enter your promise message : ").strip()
   student["promise"] = promise

   # --- Save to file ---
   with open(STUDENTS_FILE, "a") as sf :
      sf.write( json.dumps(student) + "\n" )
      print("\n ✅ Student Registered Successfully! \n")

def check_birthdays():
    """ Check and display students having birthday today """
    # clear_screen()
    print("\n --- Birthday Checker Section --- \n")
    today = datetime.now().strftime("%d-%m")
    birthday_students = []
    found = False
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as sf:
            for line in sf:
                student = json.loads(line.strip())
                dob = student.get("DOB", "")
                if dob:
                    dob_date = datetime.strptime(dob, "%d-%m-%Y")
                    if dob_date.strftime("%d-%m") == today:
                        birthday_students.append(student)
            if birthday_students:
                print(f"🎉 Today's birthdays 🎉 \n")
                found = True
                for student in birthday_students:
                    print(f"Roll No: {student['roll_no']}, Name: {student['Name']}, DOB: {student['DOB']} , Promise: {student['promise']}")   

                filename = os.path.join(DATA_DIR, datetime.now().strftime("%d-%m-%Y") + ".txt")
                with open(filename, "w") as daily_file:
                    for student in birthday_students:
                        daily_file.write(json.dumps(student) + "\n")
                print(f"\n ✅ Birthday list saved to {filename}\n")       
    if not found:
        print("❌ No birthdays today.🎂")
    input("\nPress Enter to continue...")

def exit_program():
    """Gracefully exit the program."""
    print("\nThank you for using the Student Birthday Management System!")
    print("Exiting the program. Goodbye! 👋\n")
    exit(0)

def invalid_choice():
    """Handle invalid menu choices."""
    print("\n❌ Invalid choice. Please select a valid option from the menu.\n") 
    print("Returning to the main menu...\n")
    input("Press Enter to continue...")
    print()
    return