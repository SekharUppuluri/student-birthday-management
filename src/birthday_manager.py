# internal requirements
import json
import os
from datetime import datetime
import sys

# external requirements

# constants
DATA_DIR = "data"
DATE_FORMAT = "%d-%m-%Y"
SHORT_DATE_FORMAT = "%d-%m"

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
   while True:
       roll_no = input("Enter Roll Number : ").strip()
       if not roll_no:
            print("❌ Roll Number cannot be empty. Please try again.")
       else:
            student["roll_no"] = roll_no
            break
   
   # --- Name ---
   while True:
       name = input("Enter Name : ").strip()
       if not name:
           print("❌ Name cannot be empty. Please try again.")
       else:
           student["name"] = name
           break
        
   # --- Course ---
   while True:
    course = input("Enter Course : ").strip()
    if not course:
        print("❌ Course cannot be empty. Please try again.")
    else:
        student["course"] = course
        break
   
   # --- Year ---
   while True:
    year = input("Enter Year (1/2/3/4) : ").strip()
    valid_years = [1,2,3,4,5,6]
    if not year.isdigit():
        print("❌ Invalid input. Please enter a number between 1 and 6.")
        continue
    year = int(year)
    if year not in valid_years :
        print("Year out of range. Please enter a number between 1 and 6.")
    else:
        student["year"] = year
        break
    
   # --- Section ---
   section = input("Enter Section : ").strip()
   student["section"] = section
   # --- Date of Birth ---
   dob = input("Enter Date of Birth (DD-MM-YYYY) : ").strip()
   student["dob"] = dob
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
    today = datetime.now().strftime(SHORT_DATE_FORMAT)
    birthday_students = []
    found = False
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as sf:
            for line in sf:
                student = json.loads(line.strip())
                dob = student.get("dob", "")
                if dob:
                    dob_date = datetime.strptime(dob, DATE_FORMAT)
                    if dob_date.strftime(SHORT_DATE_FORMAT) == today:
                        birthday_students.append(student)
            if birthday_students:
                print(f"🎉 Today's birthdays 🎉 \n")
                found = True
                print(f"{'Roll No':<10} {'Name':<20} {'DOB':<15} {'Promise':<30}")
                print("-" * 75)  # Decorative line for separation
                for student in birthday_students:
                    print(f"{student['roll_no']:<10} {student['name']:<20} {student['dob']:<15} {student['promise']:<30}")

                filename = os.path.join(DATA_DIR, datetime.now().strftime(DATE_FORMAT) + ".txt")
                with open(filename, "w") as daily_file:
                    for student in birthday_students:
                        daily_file.write(json.dumps(student) + "\n")
                print(f"\n ✅ Birthday list saved to {filename}\n")       
    if not found:
        print(f"❌ No birthdays found for today ({today}). 🎂")
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

# def clear_screen():
#     """ Clears the console screen """
#     if os.name == 'nt':  # For Windows
#         os.system('cls')
#     else:  # For macOS/Linux
#         os.system('clear')

def main():
    while True :
        print("===== Student Birthday Management System =====")
        print("1. Register New Student ")
        print("2. Check Today's Birthdays ")
        print("3. Exit ")
        choice = input("Enter your choice (1-3) : ").strip()
        
        if choice == "1" :
            register_student()
        elif choice == "2" :
            check_birthdays()
        elif choice == "3" :
            exit_program()
        else :
            invalid_choice()


if __name__ == "__main__":
    print("\n🚀 Welcome to Student Birthday Management System (CLI Version)\n")
    main()
