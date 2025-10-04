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
