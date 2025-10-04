# 🎂 Student Birthday Management System 🎉

[![Python](https://img.shields.io/badge/Python-3.12.5-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Project-Mini%20Project-success)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Problem Statement

A menu-driven Python program to manage student records and check whose birthdays fall on the current date.  
This project demonstrates Python fundamentals including conditionals, loops, dictionaries, file handling, and modules like `datetime`, `json`, and `os`.

---

## 🚀 Features (V1 – CLI)

- Register new student with:
  - Roll No, Name, Course, Year, Section, DOB, Promise Note  
- Store all student records in `students.txt` (JSON format).  
- Check today’s birthdays:
  - Compare DOB with today’s date.  
  - Print details on screen.  
  - Save results in a file named `DD-MM-YYYY.txt` inside the `data/` folder.  
- Exit the program safely.  

---
## 🛠 Tech Stack

- **Language**: Python 3.12.5  
- **Built-in Libraries**: `json`, `datetime`, `os`, `sys`
---

## 📂 Project Structure

```bash
student-birthday-management/
│
├── data/                   # Data files (students.txt, daily birthday lists)
├── src/
│   └── birthday_manager.py # Core Python code
├── .gitignore
├── LICENSE
└── README.md
``` 
---

## 📊 Flow Diagram

Here’s a high-level flow of how the system works:

```mermaid
---
config:
title: 🎂 Student Birthday Management Flowchart (V1 – CLI)
---

flowchart TD
    A(["Start"]) --> B["Display Main Menu"]
    B --> C["1. Register New Student"] & F["2. Check Today's Birthdays"] & L["3. Exit Application"]
    C --> D["Input Student Details:<br>Roll No, Name, Course, Year,<br>Section, DOB, Promise"]
    D --> E["Save Record to students.txt (JSON)"]
    E --> B
    F --> G["Compare DOB with Current Date"]
    G --> H{"Is it a Birthday Today?"}
    H -- Yes --> I["Display Today's Birthdays"]
    I --> K["Save to DD-MM-YYYY.txt"]
    K --> B
    H -- No --> J["No Birthdays Today"]
    J --> B
    L --> M(["End"])

    %% Node styles
    classDef bigEndStart fill:#f97316,stroke:#ea580c,stroke-width:5px,color:#fff,font-size:30px,font-family:Inter,Arial Black,sans-serif,font-weight:900
    classDef decision fill:#facc15,stroke:#ca8a04,stroke-width:2px,color:#000,font-family:Inter,sans-serif
    classDef inputNode fill:#10b981,stroke:#065f46,stroke-width:2px,color:#fff,font-family:Inter,sans-serif
    classDef process fill:#3b82f6, stroke:#1e40af, stroke-width:2px, color:#fff, font-family:Inter, sans-serif

    %% Apply styles
    A:::bigEndStart
    M:::bigEndStart
    B:::process
    C:::process
    F:::process
    L:::process
    D:::inputNode
    E:::process
    G:::process
    H:::decision
    I:::process
    K:::process
    J:::process

```
<!-- <p align="center">
  <img src="docs/Project%20Flow%20Chart%20%5Blec%5D.png" alt="System Flow Diagram" width="600">
</p> -->


---

## 🚀 How to Run on Your Machine

### 1️⃣ Clone the repository and change directory (same for macOS/Linux and Windows)
```bash
git clone https://github.com/SekharUppuluri/student-birthday-management.git
cd student-birthday-management
```

### 2️⃣ Run the Program and Tests

Follow the steps below to run the program and tests on your system:

|   Step       |      macOS/Linux           |       Windows                   |
|:------------- |:--------------------------|:-------------------------------|
| **Run program** | `python3 src/birthday_manager.py`      | `python src\birthday_manager.py`             |

> **Note**: On **Windows**, make sure to use `src\birthday_manager.py` with backslashes for the file path.


## 📸 Screenshots (V1)
- ✅ Full CLI DEMO

![FULL CLI ](Screenshots/FULL%20CLI.png)

- 📝 Register a Student
  
![Register a Student](Screenshots/Registration_Section.png)

- 🎉 Check Today’s Birthdays

![Check Today’s Birthdays](Screenshots/Check_Birthdays_Section.png)

- ❌ Exit 

![Exit from program](Screenshots/Exit.png)


### 📜 License  
This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 Author  
**Sekhar Uppuluri**  
[GitHub: @SekharUppuluri](https://github.com/SekharUppuluri)


