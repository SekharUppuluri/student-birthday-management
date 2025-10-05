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
       duplicate = False
       if not roll_no:
            print("❌ Roll Number cannot be empty. Please try again.")
            continue
       
       if os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE,"r") as records:
                for record in records:
                    if not record.strip():
                        continue
                    student_data = json.loads(record.strip())
                    if student_data.get("roll_no") == roll_no:
                        duplicate = True
                        break
       if duplicate:
            print(f"❌ Roll Number '{roll_no}' is already registered. Please use a different one.")
            continue
       
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
   while True:
       section = input("Enter Section (eg; 01/1/CA01): ").strip()
       if not section:
           print("❌ Section cannot be empty. Please try again.")
           continue
       if not section.isalnum():
           print("❌ Invalid section. Only letters and numbers allowed (no spaces or symbols).")
           continue
       if len(section) > 5:
           print("❌ Section name too long. Max 5 characters allowed.")
           continue
       student["section"] = section.upper()
       break
   
    # --- Date of Birth ---
   while True:
        dob = input("Enter Date of Birth (DD-MM-YYYY) : ").strip()
        if not dob:
            print("❌ Date of Birth cannot be empty. Please try again.")
            continue
        # Validate the format: DD-MM-YYYY
        if len(dob) != 10 or dob[2] != "-" or dob[5] != "-":
            print("❌ Invalid format. Please use DD-MM-YYYY.") 
            continue
        # Extract day, month, and year components
        day_str, month_str, year_str = dob[:2], dob[3:5], dob[6:]
        
        # Ensure all components are numeric/numbers
        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            print("❌ Day, month, and year must be numeric.")
            continue
        # Convert to integers for validation
        day, month, year = int(day_str), int(month_str), int(year_str)

        # Validate day range
        if not (1 <= day <= 31):
            print("❌ Invalid Day. Must be between 1 and 31.")
            continue
        # Validate month range
        if not (1 <= month <= 12):
            print("❌ Invalid Month. Must be between 1 and 12.")
            continue
        # Validate year range 
        current_year = datetime.now().year
        if not (1900 <= year <= current_year):
            print("❌ Year must be between 1900 and the current year.")
            continue
        
        # Store the validated date of birth
        student["dob"] = dob
        break
   
   # --- promise ---
   promise = input("Enter your promise message : ").strip()
   if promise:
       student["promise_note"] = promise
   else:
       student["promise_note"] = "Promise Note not given."
    
   # --- Save to file ---
   with open(STUDENTS_FILE,"a") as adding_record:
       adding_record.write(json.dumps(student) + "\n")
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
                    print(f"{student['roll_no']:<10} {student['name']:<20} {student['dob']:<15} {student['promise_note']:<30}")

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
