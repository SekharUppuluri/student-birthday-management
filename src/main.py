import json
import datetime
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR , "data" )
STUDENTS_FILE = os.path.join(DATA_DIR , "students.txt" )

# Ensure data folder exists
if not os.path.exists(DATA_DIR) :
   os.makedirs(DATA_DIR)
   
def register_student():
   """ Register a new student and save to file with validations """
   print()
   print("\n --- Welcome to Registration Section --- \n")
   student = {}
   # --- Roll Number ---
   while True :
      rollno = input("Enter Roll Number : ").strip()
      duplicate = False
      if os.path.exists(STUDENTS_FILE):
         with open(STUDENTS_FILE, "r") as sf :
            for line in sf :
               existing = json.loads(line.strip())
               if existing["rollno"] == rollno :
                  duplicate = True
                  break
      if duplicate :
         print("\n ❌ Roll Number already exists! Try again. \n")
      elif not rollno :
         print("\n ❌ Roll Number Cannot be empty! Try again. \n")
      else :
         break
   student["rollno"] = rollno
   
   # --- Name ---
   while True :
      name = input("Enter Name : ").strip()
      if name :
         student["name"] = name 
         break
      print("\n ❌ Name cannot be empty! Please try again.\n")
   # --- Course ---
   while True :
      course = input("Enter Course : ").strip()
      if course :
         student["course"] = course
         break
      print("\n ❌ Course cannot be empty! Please try again.\n")
   # --- Year ---
   while True :
      year  = input("Enter Year (1/2/3/4) : ").strip()
      VALID_YEARS = [1,2,3,4,5,6]
      if  year.isdigit() :
         int_year = int(year)  
         if int_year in VALID_YEARS :
            student["year"] = int(year)
            break
      print("\n ❌ Year must be  1 , 2 , 3 , 4 , 5 or 6! Please Try again.\n")
   # --- Section ---
   while True :
      section = input("Enter Section : ").strip().upper()
      if section :
         student["section"] = section
         break 
      else :
         print("\n ❌ Section must be a single letter!\n")
   # --- DOB ---
   while True :
      dob = input("Enter Date of Birth (dd-mm-yyyy) : ").strip()
      try :
         datetime.datetime.strptime(dob , "%d-%m-%Y")
         student["dob"] = dob
         break
      except ValueError :
         print("\n ❌ Invalid DOB format! Use dd-mm-yyyy.\n")
      
   
   # --- Promise ---
   student["promise"] = input("Enter Promise Distribution note : ").strip()
   
   # Save student record to file
   confirm = input("Save this Student (y/n) : ").strip().lower()
   if confirm != 'y':
      print("\n ❌ Registration Cancelled.\n")
      return
   with open(STUDENTS_FILE,"a") as sf :
      sf.write(json.dumps(student) + "\n")
   print(f"\n ✅ Student {student['name']} registered successfully! \n")
   
def check_birthdays():
   """ Check today's Birthdays """
   print("\n --- Welcome to Check Birthdays Section --- ")
   if not os.path.exists(STUDENTS_FILE):
      print("\n ⚠️ No student records found.\n")
      return
   today_obj = datetime.datetime.now()
   today = today_obj.strftime("%d-%m")
   birthday_students = []
   
   with open(STUDENTS_FILE, "r") as sf :
      for line in sf :
         student = json.loads(line.strip())
         if student["dob"][:5] == today :
            birthday_students.append(student)
            
      if birthday_students:
         print("\n 🎉 Today's Birthdays 🎉 ")
         for student in birthday_students :
            print(
               f"Roll: {student['rollno']}, Name: {student['name']}, " 
               f"DOB: {student['dob']}, Promise: {student['promise']}"
                  )
         # save to daily file 
         filename = os.path.join(
            DATA_DIR, today_obj.strftime("%d-%m-%Y") + ".txt"
            )
         with open(filename,"w") as fn :
            for student in birthday_students:
               fn.write(json.dumps(student) + "\n")
            print(f"\n ✅ Birthday List saved to {filename}\n")
      else :
         print("\nNo Birthdays Today 🎂\n ")
   
def main():
   while True :
      print("===== Student Birthday Management System =====")
      print("1. Register New Student ")
      print("2. Check Today's Birthdays ")
      print("3. Exit ")
      choice = input("Enter your choice (1-3) : ")
      
      if choice == "1" :
         register_student()
      elif choice == "2" :
         check_birthdays()
      elif choice == "3" :
         print("\n 👋 Exiting program... Goodbye! \n")
         break
      else :
         print("\n ⚠️ Invalid Choice. Please try again.\n")

if __name__ == "__main__" :
   main()
   
