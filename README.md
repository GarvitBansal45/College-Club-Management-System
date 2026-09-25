# College Club Management System

A beginner-friendly, menu-driven command-line application built in Python for managing student clubs, memberships, events, and performance statistics in a college environment.

---

## 1. Project Title
**College Club Management System**  
*Course:* Python Essentials (First-Year B.Tech CSE)  
*Evaluation:* Flipped-Course Project Evaluation  

---

## 2. Project Description
The College Club Management System provides a clean, interactive terminal interface that allows college students and administrators to manage extracurricular clubs. Users can browse clubs, view detailed club records, register new student members with specialized role badges, organize activities, and track event attendance statistics without requiring any database or third-party libraries.

---

## 3. Objective
* To demonstrate practical understanding of core Python programming concepts taught in the Python Essentials course.
* To model real-world relationships using Object-Oriented Programming (Classes and Methods) and standard Python data structures.
* To provide an interactive CLI tool that operates reliably using only standard Python.

---

## 4. Features
1. **Display All Clubs**: View all registered clubs in a clear tabular format.
2. **View Club Details**: Inspect club ID, category, fixed meeting schedule (day & room), budget, planned activities, and historical event attendance.
3. **Add a New Club**: Register a new club with category validation and budget allocation.
4. **Add Member to Club**: Add student profiles (Roll Number, Name, Branch) and assign role permissions (Member, Volunteer, Coordinator) using bitwise masks.
5. **Display Club Members**: View all registered members and their active roles for any club.
6. **Search Member Across Clubs**: Locate any student across all clubs using their Roll Number.
7. **Remove Member from Club**: Remove a student record from a club.
8. **Register Club Activity**: Add unique workshops, competitions, or meetings using Python Sets.
9. **Record Event Attendance & Statistics**: Record attendee counts in a numerical Python Array, calculate floating-point average attendance, and compute club activity engagement scores using operator precedence rules.
10. **Pre-Loaded Sample Data**: Automatically loads 5 realistic clubs (Coding Club, Robotics Club, Cultural Club, Sports Club, Photography Club) for instant evaluation.

---

## 5. Technologies Used
* **Language**: Python 3 (Tested on Python 3.10+)
* **Libraries/Packages**: Standard Library only (`array`, `sys`, `os`)
* **Frameworks/Databases**: None (Strictly adheres to syllabus constraints)

---

## 6. Python Concepts Demonstrated

| Course Topic | Implementation in Project |
| :--- | :--- |
| **Python Fundamentals** | Clean variable naming, indentation, structured comments. |
| **Membership Operators (`in`, `not in`)** | Validating user menu selections and checking category existence in frozen sets. |
| **Assignment Operators (`=`, `+=`, `-=`)** | Accumulating attendance totals and updating records. |
| **Bitwise Operators (`&`, `|`)** | Bitwise role permissions: `ROLE_MEMBER (1)`, `ROLE_VOLUNTEER (2)`, `ROLE_COORDINATOR (4)`. Using `\|` to assign roles and `&` to verify roles. |
| **`type()` Function** | Displaying underlying data types in the statistics module (`<class 'str'>`, `<class 'int'>`, `<class 'tuple'>`, `<class 'array.array'>`). |
| **Identity Operators (`is`, `is not`)** | Checking object identity when searching: `if selected_club is None:`. |
| **Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`)** | Budget calculations, total attendance accumulation, score calculations. |
| **Logical OR and NOT** | Input validation: `if not budget_input.isdigit():`. |
| **Logical AND** | Multi-attribute validation: `if len(name) > 0 and len(roll_no) > 0:`. |
| **Relational / Comparison Operators** | Comparing string IDs, roll numbers, and numeric thresholds (`==`, `!=`, `<`, `>`). |
| **Division for Mixed Types** | Floating-point division (`/`) for averages and integer floor division (`//`) for discrete rating points. |
| **Input / Output Operations** | Interactive terminal prompts via `input()` and formatted tables via `print()`. |
| **Operator Precedence & Associativity** | Calculating activity score: `(total_attendance * 2 + bonus_points) // total_events`. |
| **Type Conversion** | Explicit conversions using `int()`, `float()`, `str()`, and `tuple()`. |
| **List** | Maintaining dynamic collections of `Club` objects and student member dictionaries. |
| **Tuple** | Immutable `(day, room_number)` pair for club meeting schedules. |
| **Set** | Storing unique activity names (`club.activities`) to prevent duplicate events. |
| **Dictionary** | Representing student member details: `{'roll_no': ..., 'name': ..., 'branch': ..., 'role_mask': ...}`. |
| **Frozen Set** | Immutable collection of valid club categories: `frozenset(["Technical", "Cultural", "Sports", "Literary"])`. |
| **Array Data Structure** | `array.array('i', [...])` for storing historical event attendance counts. |
| **Control Flow** | `while` loops for the interactive loop, `for` loops for record traversal, `if/elif/else` for decision branching, `break` to exit, and `continue` to re-prompt. |
| **Functions** | Structured modular functions with clear parameters and return values. |
| **Modules and Packages** | Modular division into `club.py`, `main.py`, and `tests/test_project.py`. |
| **Object-Oriented Programming** | Beginner-friendly `Club` class encapsulating attributes and methods. |

---

## 7. Project Structure
```text
college-club-management/
│
├── club.py              # Beginner Club class and bitwise permission constants
├── main.py              # CLI menu, sample data, and application logic
├── requirements.txt     # Information file confirming no external libraries are needed
├── README.md            # Comprehensive project documentation
└── tests/
    └── test_project.py  # Plain Python assert-based verification tests
```

---

## 8. Requirements
* Python 3.8 or higher installed on your computer.
* No pip packages or external libraries are required.

---

## 9. Step-by-Step Setup Instructions

1. Open your terminal (Command Prompt, PowerShell, or Bash).
2. Verify Python is installed:
   ```bash
   python --version
   ```
3. Navigate to the project directory:
   ```bash
   cd college-club-management
   ```

---

## 10. How to Run the Project from Terminal

### Running the Application:
```bash
python main.py
```

### Running the Verification Test Suite:
```bash
python tests/test_project.py
```

---

## 11. Example Usage

```text
==================================================
        COLLEGE CLUB MANAGEMENT SYSTEM            
==================================================
1. Display All Clubs
2. View Club Details
3. Add a New Club
4. Add Member to a Club
5. Display Club Members
6. Search Member Across All Clubs
7. Remove Member from a Club
8. Register Club Activity / Event
9. Record Event Attendance & View Statistics
10. Exit System
==================================================
Enter your choice (1-10): 1

--- LIST OF REGISTERED CLUBS ---
Index | Club ID | Club Name            | Category   | Members
-------------------------------------------------------------
1     | C101    | Coding Club          | Technical  | 3
2     | C102    | Robotics Club        | Technical  | 2
3     | C103    | Cultural Club        | Cultural   | 2
4     | C104    | Sports Club          | Sports     | 1
5     | C105    | Photography Club     | Literary   | 1
```

---

## 12. Limitations
* Data persists in memory only during program execution; closing the program resets data back to the default sample records (since file handling and databases are not part of the course syllabus).
* User interface is restricted strictly to terminal input/output.
* Input validation is implemented via basic string conditionals rather than exception handling blocks.

---

## 13. Future Improvements
* Add persistent data storage using text files or relational databases when those topics are studied in subsequent semesters.
* Create a Graphical User Interface (GUI) or web interface when frontend programming is introduced.
* Add automated email notifications for club meeting announcements.
