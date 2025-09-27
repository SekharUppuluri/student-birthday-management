import os
import json
import datetime
import tempfile
import pytest

# Import your functions from src
from src.main import register_student, check_birthdays, STUDENTS_FILE, DATA_DIR

@pytest.fixture(autouse=True)
def clean_data_dir():
    """Fixture to ensure data directory is clean before each test"""
    if os.path.exists(STUDENTS_FILE):
        os.remove(STUDENTS_FILE)
    yield
    # cleanup after
    if os.path.exists(STUDENTS_FILE):
        os.remove(STUDENTS_FILE)

def test_register_student(monkeypatch):
    """Test registering a new student"""
    inputs = iter([
        "101",         # Roll number
        "Alice",       # Name
        "CS",          # Course
        "2",           # Year
        "A",           # Section
        "25-09-2000",  # DOB
        "Work hard",   # Promise
        "y"            # Confirm
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    register_student()
    assert os.path.exists(STUDENTS_FILE)

    with open(STUDENTS_FILE, "r") as f:
        data = json.loads(f.readline().strip())
    assert data["rollno"] == "101"
    assert data["name"] == "Alice"

def test_check_birthdays(monkeypatch, capsys):
    """Test birthday check when student has today’s birthday"""
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    student = {
        "rollno": "102",
        "name": "Bob",
        "course": "IT",
        "year": 3,
        "section": "B",
        "dob": today,
        "promise": "Be kind"
    }
    with open(STUDENTS_FILE, "a") as f:
        f.write(json.dumps(student) + "\n")

    check_birthdays()
    captured = capsys.readouterr()
    assert "Bob" in captured.out
    daily_file = os.path.join(DATA_DIR, datetime.datetime.now().strftime("%d-%m-%Y") + ".txt")
    assert os.path.exists(daily_file)
