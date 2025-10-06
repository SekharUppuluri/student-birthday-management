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

STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")


# ================================
# Utility Functions
# ================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner(text, color=Fore.CYAN, font="small"):
    """Prints a colored ASCII banner"""
    f = Figlet(font=font)
    print(color + f.renderText(text) + RESET)


def load_students():
    """Load all students from file"""
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            return [json.loads(line.strip()) for line in f if line.strip()]
    return []


def save_students(students):
    """Save all students back to file"""
    with open(STUDENTS_FILE, "w") as f:
        for student in students:
            f.write(json.dumps(student) + "\n")


# ================================
# Core Features
# ================================
def register_student():
    """Register a new student and save to file with validations"""
    clear_screen()
    banner("Registration", Fore.GREEN)
    print("-" * 50)

    student = {}
    # --- Roll Number ---
    while True:
        roll_no = input("Enter Roll Number : ").strip()
        if not roll_no:
            print(ERROR + "❌ Roll Number cannot be empty. Please try again.")
            continue

        students = load_students()
        if any(s["roll_no"] == roll_no for s in students):
            print(ERROR + f"❌ Roll Number '{roll_no}' already exists.")
            continue

        student["roll_no"] = roll_no
        break

    # --- Name ---
    while True:
        name = input("Enter Name : ").strip()
        if not name:
            print(ERROR + "❌ Name cannot be empty.")
        else:
            student["name"] = name
            break

    # --- Course ---
    while True:
        course = input("Enter Course : ").strip()
        if not course:
            print(ERROR + "❌ Course cannot be empty.")
        else:
            student["course"] = course
            break

    # --- Year ---
    while True:
        year = input("Enter Year (1-6) : ").strip()
        if not year.isdigit() or int(year) not in range(1, 7):
            print(ERROR + "❌ Enter a valid number between 1 and 6.")
        else:
            student["year"] = int(year)
            break

    # --- Section ---
    while True:
        section = input("Enter Section (e.g., A1, CSE01): ").strip()
        if not section:
            print(ERROR + "❌ Section cannot be empty.")
            continue
        if not section.isalnum() or len(section) > 5:
            print(ERROR + "❌ Invalid section. Use up to 5 letters/numbers.")
            continue
        student["section"] = section.upper()
        break

    # --- DOB ---
    while True:
        dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(dob, DATE_FORMAT)
            student["dob"] = dob
            break
        except ValueError:
            print(ERROR + "❌ Invalid date format. Please use DD-MM-YYYY.")

    # --- Promise Note ---
    promise = input("Enter your promise message : ").strip()
    student["promise_note"] = promise if promise else "Promise Note not given."

    students.append(student)
    save_students(students)

    print(SUCCESS + "\n✅ Student Registered Successfully!\n")
    input(INFO + "Press Enter to return to the main menu...")


def view_students():
    """List all registered students"""
    clear_screen()
    banner("All Students", Fore.YELLOW)
    print("-" * 50)

    students = load_students()
    if not students:
        print(ERROR + "❌ No students registered yet.")
    else:
        print(f"{'Roll No':<10} {'Name':<20} {'Course':<15} {'Year':<6} {'Section':<8} {'DOB':<12}")
        print("-" * 75)
        for s in students:
            print(f"{s['roll_no']:<10} {s['name']:<20} {s['course']:<15} {s['year']:<6} {s['section']:<8} {s['dob']:<12}")
        print(INFO + f"\nTotal students: {len(students)}")

    input(WARNING + "\nPress Enter to return to the main menu...")


def check_birthdays():
    """Check and display students having birthday today"""
    clear_screen()
    banner("Birthday Checker", Fore.MAGENTA)
    print("-" * 50)

    today = datetime.now().strftime(SHORT_DATE_FORMAT)
    students = load_students()
    birthday_students = [
        s for s in students
        if datetime.strptime(s["dob"], DATE_FORMAT).strftime(SHORT_DATE_FORMAT) == today
    ]

    if birthday_students:
        print(f"🎉 Today's Birthdays 🎉\n")
        print(f"{'Roll No':<10} {'Name':<20} {'DOB':<15} {'Promise':<30}")
        print("-" * 75)
        for s in birthday_students:
            print(f"{s['roll_no']:<10} {s['name']:<20} {s['dob']:<15} {s['promise_note']:<30}")

        filename = os.path.join(DATA_DIR, datetime.now().strftime(DATE_FORMAT) + ".txt")
        save_students(birthday_students)
        print(SUCCESS + f"\n✅ Birthday list saved to {filename}")
    else:
        print(ERROR + f"\n❌ No birthdays found for today ({today}). 🎂")

    input("\nPress Enter to continue...")


def search_student():
    """Search for a student by Roll Number or Name"""
    clear_screen()
    banner("Search Student", Fore.CYAN)
    print("-" * 50)

    print(INFO + "1. Search by Roll No")
    print(INFO + "2. Search by Name")
    search_choice = input("Enter your choice (1-2): ").strip()

    if search_choice == "1":
        key = "roll_no"
        search_value = input("Enter Roll Number: ").strip()
    elif search_choice == "2":
        key = "name"
        search_value = input("Enter Full Name: ").strip()
    else:
        print(ERROR + "❌ Invalid choice.")
        input(WARNING + "Press Enter to return...")
        return

    if not search_value:
        print(ERROR + "❌ Input cannot be empty.")
        input(WARNING + "Press Enter to return...")
        return

    students = load_students()
    found = False
    for s in students:
        if s[key].strip().lower() == search_value.lower():
            found = True
            print(SUCCESS + "\n✅ Student Found:\n")
            for field, value in s.items():
                print(f"{field.title():<15}: {value}")
            break

    if not found:
        print(ERROR + "❌ Student not found.")

    input(WARNING + "Press Enter to return...")


def edit_student():
    """Edit existing student details"""
    clear_screen()
    banner("Edit Student", Fore.CYAN)
    print("-" * 50)

    students = load_students()
    roll_no = input("Enter Roll Number to edit: ").strip()
    found = False

    for s in students:
        if s["roll_no"] == roll_no:
            found = True
            print(SUCCESS + f"\nEditing Student: {s['name']} (Roll: {s['roll_no']})")
            print("Leave blank to keep current value.\n")

            s["name"] = input(f"Name [{s['name']}]: ").strip() or s["name"]
            s["course"] = input(f"Course [{s['course']}]: ").strip() or s["course"]
            s["year"] = input(f"Year [{s['year']}]: ").strip() or s["year"]
            s["section"] = input(f"Section [{s['section']}]: ").strip() or s["section"]
            s["dob"] = input(f"DOB [{s['dob']}]: ").strip() or s["dob"]
            s["promise_note"] = input(f"Promise Note [{s['promise_note']}]: ").strip() or s["promise_note"]

            save_students(students)
            print(SUCCESS + "✅ Student details updated successfully!")
            break

    if not found:
        print(ERROR + "❌ Student not found.")

    input(WARNING + "Press Enter to return...")


def delete_student():
    """Delete a student record"""
    clear_screen()
    banner("Delete Student", Fore.RED)
    print("-" * 50)

    roll_no = input("Enter Roll Number to delete: ").strip()
    students = load_students()

    filtered = [s for s in students if s["roll_no"] != roll_no]
    if len(filtered) == len(students):
        print(ERROR + f"❌ No student found with Roll No {roll_no}.")
    else:
        save_students(filtered)
        print(SUCCESS + f"✅ Student with Roll No {roll_no} deleted successfully!")

    input(WARNING + "Press Enter to return...")


def exit_program():
    """Gracefully exit the program."""
    clear_screen()
    print("\nThank you for using the Student Birthday Management System!")
    banner("Goodbye!", Fore.YELLOW)
    print("👋 Exiting the program.\n")
    exit(0)


def invalid_choice():
    """Handle invalid menu choices."""
    print(ERROR + "\n❌ Invalid choice. Please select a valid option.\n")
    input(WARNING + "Press Enter to continue...")


# ================================
# Main Menu Loop
# ================================
def main():
    while True:
        banner("Student Birthday Management System", TITLE)
        print("=" * 50)
        print(INFO + "1. Register New Student")
        print(INFO + "2. Check Today's Birthdays")
        print(INFO + "3. View All Students")
        print(INFO + "4. Search Student")
        print(INFO + "5. Edit Student")
        print(INFO + "6. Delete Student")
        print(INFO + "7. Exit" + RESET)
        print("=" * 50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            check_birthdays()
        elif choice == "3":
            view_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            edit_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            exit_program()
        else:
            invalid_choice()


if __name__ == "__main__":
    try:
        print(TITLE + "\n🚀 Welcome to Student Birthday Management System (CLI Version)\n")
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user.")
        exit_program()
