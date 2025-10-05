# internal requirements
import json
import os
from datetime import datetime
# external requirements
from pyfiglet import Figlet
from colorama import Fore, Style, init
init(autoreset=True)

# constants
DATA_DIR = "data"
DATE_FORMAT = "%d-%m-%Y"
SHORT_DATE_FORMAT = "%d-%m"

# color scheme
INFO = Fore.CYAN
SUCCESS = Fore.GREEN
ERROR = Fore.RED
WARNING = Fore.YELLOW
TITLE = Fore.MAGENTA
RESET = Style.RESET_ALL


if not os.path.exists(DATA_DIR):
   os.makedirs(DATA_DIR)

STUDENTS_FILE = os.path.join( DATA_DIR , "students.txt" )
# functions
def banner(text, color=Fore.CYAN, font="small"):
    """Prints a colored ASCII banner"""
    f = Figlet(font=font)
    print(color + f.renderText(text) + RESET)

def register_student():
   """ Register a new student and save to file with validations """
   clear_screen()
   banner("Registration", Fore.GREEN)
   print("-" * 50)
   student = {}
   # --- Roll Number ---
   while True:
       roll_no = input("Enter Roll Number : ").strip()
       duplicate = False
       if not roll_no:
            print(ERROR +"❌ Roll Number cannot be empty. Please try again.")
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
            print(f"{ERROR}❌ Roll Number '{roll_no}' is already registered. Please use a different one.")
            continue
       
       student["roll_no"] = roll_no
       break
   
   # --- Name ---
   while True:
       name = input("Enter Name : ").strip()
       if not name:
           print(ERROR +"❌ Name cannot be empty. Please try again.")
       else:
           student["name"] = name
           break
        
   # --- Course ---
   while True:
    course = input("Enter Course : ").strip()
    if not course:
        print(ERROR +"❌ Course cannot be empty. Please try again.")
    else:
        student["course"] = course
        break
   
   # --- Year ---
   while True:
    year = input("Enter Year (1/2/3/4) : ").strip()
    valid_years = [1,2,3,4,5,6]
    if not year.isdigit():
        print(ERROR +"❌ Invalid input. Please enter a number between 1 and 6.")
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
           print(ERROR +"❌ Section cannot be empty. Please try again.")
           continue
       if not section.isalnum():
           print(ERROR +"❌ Invalid section. Only letters and numbers allowed (no spaces or symbols).")
           continue
       if len(section) > 5:
           print(ERROR +"❌ Section name too long. Max 5 characters allowed.")
           continue
       student["section"] = section.upper()
       break
   
    # --- Date of Birth ---
   while True:
        dob = input("Enter Date of Birth (DD-MM-YYYY) : ").strip()
        if not dob:
            print(ERROR +"❌ Date of Birth cannot be empty. Please try again.")
            continue
        # Validate the format: DD-MM-YYYY
        if len(dob) != 10 or dob[2] != "-" or dob[5] != "-":
            print(ERROR +"❌ Invalid format. Please use DD-MM-YYYY.") 
            continue
        # Extract day, month, and year components
        day_str, month_str, year_str = dob[:2], dob[3:5], dob[6:]
        
        # Ensure all components are numeric/numbers
        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            print(ERROR +"❌ Day, month, and year must be numeric.")
            continue
        # Convert to integers for validation
        day, month, year = int(day_str), int(month_str), int(year_str)

        # Validate day range
        if not (1 <= day <= 31):
            print(ERROR +"❌ Invalid Day. Must be between 1 and 31.")
            continue
        # Validate month range
        if not (1 <= month <= 12):
            print(ERROR +"❌ Invalid Month. Must be between 1 and 12.")
            continue
        # Validate year range 
        current_year = datetime.now().year
        if not (1900 <= year <= current_year):
            print(ERROR +"❌ Year must be between 1900 and the current year.")
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

   print("-" * 50)

    
   # --- Save to file ---
   with open(STUDENTS_FILE,"a") as adding_record:
       adding_record.write(json.dumps(student) + "\n")
   print( SUCCESS + "\n ✅ Student Registered Successfully! \n")
   input(INFO + "Press Enter to return to the main menu...")


def check_birthdays():
    """ Check and display students having birthday today """
    clear_screen()
    banner("Birthday Checker", Fore.MAGENTA)
    print("-" * 50 )
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
                print(f"\n{SUCCESS} ✅ Birthday list saved to {filename}\n")       
    if not found:
        print(f"\n{ERROR} ❌ No birthdays found for today ({today}). 🎂")
    input("\nPress Enter to continue...")

def view_students():
    """ list all registered students"""
    clear_screen()
    banner("All Students", Fore.Yellow)
    print("-" * 50)

    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE,"r") as vsf:
            students = [json.loads(line.strip()) for line in vsf if line.strip()]
        if students:
            print(f"{'Roll No':<10} {'Name':<20} {'Course':<15} {'Year':<6} {'Section':<8} {'DOB':<12}")
            print("-" * 75)
            for student in students:
                print(f"{student['roll_no']:<10} {student['Name']:<20} {student['Course']:<15} {student['Year']:<6} {student['Section']:<8} {student['DOB']:<12}")
        else:
            print(ERROR + "❌ No students registered yet.")
    else :
        print(ERROR + "❌ No students registered yet./file Not Exists ")

    input(Warning + "\n Press Enter to return to the main menu ...")

def search_student():
    """ search for a student by roll number / by name """
    clear_screen()
    banner("Search Student",Fore.CYAN)
    print("-" * 50)
    
    print(INFO + "1. Search by Roll No ")
    print(INFO + "2. Search by Name ")
    search_choice = input("Enter your choice (1-2) :  ").strip()

    if search_choice == "1" :
        key = "roll_no"
        search_value = input("Enter Roll Number to search : ").strip()
    elif search_choice == "2":
        key = "name"
        search_value = input("Enter Full Name to search : ").strip()
    else:
        print(ERROR + "❌ Invalid choice.")
        input(WARNING + "Press Enter to return to the main menu...")
        return
    if not search_value :
        print(ERROR + "❌ Input cannot be empty.")
        input(WARNING + "Press Enter to return to the main menu...")
        return
    
    found = False 

    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as ssf:
            for student in ssf:
                student = json.loads(line.strip())
                value = student.get(key, "").strip()
                if key == "name" :
                    value = value.lower()
                
                if value == search_value :
                    found  = True
                    print(SUCCESS + "\n Student Found: \n")
                    print(f"Roll Number : {student['roll_no']}")
                    print(f"Name        : {student['name']}")
                    print(f"Course      : {student['course']}")
                    print(f"Year        : {student['year']}")
                    print(f"Section     : {student['section']}")
                    print(f"DOB         : {student['dob']}")
                    print(f"Promise Note: {student['promise_note']}")
                    break
    else:
        print(ERROR + "File not found ")
    if not found :
        print(ERROR + "❌ Student not found. ")
    input(WARNING + "Press Enter to return to the main menu...")
    return
    
def edit_student():
    """ Update details of an existing student """
    clear_screen()
    banner("Edit Student", Fore.CYAN)
    print("-" * 50)
    
    print(INFO + "1. Search by Roll No")
    print(INFO + "2. Search by Name")
    search_choice = input("Enter your choice (1-2): ").strip()

    if search_choice == "1":
        key = "roll_no"
        search_value = input("Enter Roll Number to search: ").strip()
    elif search_choice == "2":
        key = "name"
        search_value = input("Enter Full Name to search: ").strip()
    else:
        print(ERROR + "❌ Invalid choice.")
        input(WARNING + "Press Enter to return to the main menu...")
        return
    
    if not search_value:
        print(ERROR + "❌ Input cannot be empty.")
        input(WARNING + "Press Enter to return to the main menu...")
        return
    
    found = False
    updated_students = []  # List to store updated student details

    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as ssf:
            for line in ssf:
                student = json.loads(line.strip())
                value = student.get(key, "").strip()
                if key == "name":
                    value = value.lower()
                
                if value == search_value:
                    found = True
                    print(SUCCESS + f"\nStudent found: {student['name']} (Roll No: {student['roll_no']})\n")
                    print("Leave fields blank to keep current value.\n")

                    # update fields
                    new_roll_no = input(f"Enter new Roll No: current roll_no: {student['roll_no']} : ")
                    if new_roll_no:
                        student["roll_no"] = new_roll_no

                    new_name = input(f"Enter new Name: current name: {student['name']} : ")
                    if new_name:
                        student["name"] = new_name

                    new_course = input(f"Enter new Course: current Course: {student['course']} : ")
                    if new_course:
                        student["course"] = new_course

                    new_year = input(f"Enter new Year: current Year: {student['year']} : ")
                    if new_year:
                        student["year"] = new_year

                    new_section = input(f"Enter new Section: current section: {student['section']} : ")
                    if new_section:
                        student["section"] = new_section

                    new_dob = input(f"Enter new DOB: current DOB: {student['dob']} : ")
                    if new_dob:
                        student["dob"] = new_dob

                    new_promise_note = input(f"Enter new Promise Note: current Promise Note: {student['promise_note']} : ")
                    if new_promise_note:
                        student["promise_note"] = new_promise_note
                    
                    # Append updated student
                    updated_students.append(student)
                else:
                    # Keep unchanged students
                    updated_students.append(student)
    
        if found:
            with open(STUDENTS_FILE, "w") as ssf:
                for student in updated_students:
                    ssf.write(json.dumps(student) + "\n")
            print(SUCCESS + "✅ Student details updated successfully!")
        else:
            print(ERROR + "❌ Student not found.")
    else:
        print(ERROR + "❌ File not found.")

    input(WARNING + "Press Enter to return to the main menu...")

def exit_program():
    """Gracefully exit the program."""
    print("\nThank you for using the Student Birthday Management System!")
    banner("Goodbye!", Fore.YELLOW)
    print("Exiting the program. Goodbye! 👋\n")
    exit(0)

def invalid_choice():
    """Handle invalid menu choices."""
    print(ERROR +"\n❌ Invalid choice. Please select a valid option from the menu.\n") 
    print(WARNING +"Returning to the main menu...\n")
    input("Press Enter to continue...")
    print()
    return

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True :
        banner("Student Birthday Management System", TITLE)
        print("=" * 50 )
        print(INFO + "1. Register New Student")
        print(INFO + "2. Check Today's Birthdays")
        print(INFO + "3. View All Students")
        print(INFO + "4. search Student")
        print(INFO + "5. Edit Student")
        print(INFO + "6. Delete Student")
        print(INFO + "7. Exit" + RESET)
        print("=" * 50)

        choice = input("Enter your choice (1-3) : ").strip()
        
        if choice == "1" :
            register_student()
        elif choice == "2" :
            check_birthdays()
        elif choice == "3" :
            view_students()
        elif choice == "4" :
            search_student()
        elif choice == "5" :
            edit_student()
        elif choice == "6" :
            pass
        elif choice == "7" :
            exit_program()
        else :
            invalid_choice()


if __name__ == "__main__":
    print(TITLE + "\n🚀 Welcome to Student Birthday Management System (CLI Version)\n")
    main()
