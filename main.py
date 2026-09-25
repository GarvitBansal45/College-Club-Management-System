"""
main.py - Main interactive terminal program for College Club Management System.
First-year B.Tech CSE project for Python Essentials course.
"""

import club
from club import (
    Club,
    VALID_CATEGORIES,
    ROLE_MEMBER,
    ROLE_VOLUNTEER,
    ROLE_COORDINATOR,
    get_role_description,
)


def initialize_sample_data():
    """
    Initializes sample clubs with members, activities, and past event attendance.
    Allows the evaluator to test all features immediately without manual setup.
    """
    clubs = []

    # 1. Coding Club
    c1 = Club("C101", "Coding Club", "Technical", ("Wednesday", "Lab 3"), 15000)
    c1.add_member({"roll_no": "1001", "name": "Aman Sharma", "branch": "CSE", "role_mask": ROLE_MEMBER | ROLE_COORDINATOR})
    c1.add_member({"roll_no": "1002", "name": "Priya Patel", "branch": "CSE", "role_mask": ROLE_MEMBER | ROLE_VOLUNTEER})
    c1.add_member({"roll_no": "1003", "name": "Rahul Verma", "branch": "IT", "role_mask": ROLE_MEMBER})
    c1.add_activity("Python Coding Sprint")
    c1.add_activity("Web Dev Hackathon")
    c1.record_attendance(45)
    c1.record_attendance(60)
    c1.record_attendance(52)
    clubs.append(c1)

    # 2. Robotics Club
    c2 = Club("C102", "Robotics Club", "Technical", ("Friday", "Robotics Lab"), 20000)
    c2.add_member({"roll_no": "1004", "name": "Kavya Nair", "branch": "ECE", "role_mask": ROLE_MEMBER | ROLE_COORDINATOR})
    c2.add_member({"roll_no": "1005", "name": "Rohan Gupta", "branch": "Mechanical", "role_mask": ROLE_MEMBER})
    c2.add_activity("Line Follower Bot Workshop")
    c2.record_attendance(35)
    c2.record_attendance(40)
    clubs.append(c2)

    # 3. Cultural Club
    c3 = Club("C103", "Cultural Club", "Cultural", ("Saturday", "Auditorium"), 12000)
    c3.add_member({"roll_no": "1006", "name": "Ananya Joshi", "branch": "CSE", "role_mask": ROLE_MEMBER | ROLE_COORDINATOR})
    c3.add_member({"roll_no": "1007", "name": "Vikas Rao", "branch": "Civil", "role_mask": ROLE_MEMBER | ROLE_VOLUNTEER})
    c3.add_activity("Annual Talent Hunt")
    c3.add_activity("Music Night")
    c3.record_attendance(120)
    c3.record_attendance(150)
    clubs.append(c3)

    # 4. Sports Club
    c4 = Club("C104", "Sports Club", "Sports", ("Tuesday", "Sports Ground"), 18000)
    c4.add_member({"roll_no": "1008", "name": "Siddharth Sen", "branch": "EE", "role_mask": ROLE_MEMBER | ROLE_COORDINATOR})
    c4.add_activity("Inter-Branch Cricket Tournament")
    c4.record_attendance(80)
    clubs.append(c4)

    # 5. Photography Club
    c5 = Club("C105", "Photography Club", "Literary", ("Thursday", "Media Room"), 8000)
    c5.add_member({"roll_no": "1009", "name": "Sneha Roy", "branch": "CSE", "role_mask": ROLE_MEMBER})
    c5.add_activity("Campus Photo Walk")
    c5.record_attendance(25)
    clubs.append(c5)

    return clubs


def find_club_by_id(clubs, target_id):
    """
    Searches for a club by its ID.
    Returns the Club object if found, or None.
    Demonstrates identity operator check (is / is not None).
    """
    for club_obj in clubs:
        if club_obj.club_id.upper() == target_id.strip().upper():
            return club_obj
    return None


def display_menu():
    """Prints the main interactive menu."""
    print("\n==================================================")
    print("        COLLEGE CLUB MANAGEMENT SYSTEM            ")
    print("==================================================")
    print("1. Display All Clubs")
    print("2. View Club Details")
    print("3. Add a New Club")
    print("4. Add Member to a Club")
    print("5. Display Club Members")
    print("6. Search Member Across All Clubs")
    print("7. Remove Member from a Club")
    print("8. Register Club Activity / Event")
    print("9. Record Event Attendance & View Statistics")
    print("10. Exit System")
    print("==================================================")


def display_all_clubs(clubs):
    """Displays a simple table of all registered clubs."""
    print("\n--- LIST OF REGISTERED CLUBS ---")
    if len(clubs) == 0:
        print("No clubs are currently registered.")
        return

    print("Index | Club ID | Club Name            | Category   | Members")
    print("-------------------------------------------------------------")
    idx = 1
    for c in clubs:
        # Pad strings for simple alignment
        name_padded = c.name + " " * (20 - len(c.name)) if len(c.name) < 20 else c.name[:20]
        cat_padded = c.category + " " * (10 - len(c.category)) if len(c.category) < 10 else c.category[:10]
        print(str(idx) + "     | " + c.club_id + "    | " + name_padded + " | " + cat_padded + " | " + str(len(c.members)))
        idx += 1


def view_club_details(clubs):
    """Views complete details of a single selected club."""
    club_id_input = input("\nEnter Club ID to view (e.g. C101): ")
    selected_club = find_club_by_id(clubs, club_id_input)

    # Identity operator check: is None
    if selected_club is None:
        print("[Error] No club found with ID: " + club_id_input)
        return

    selected_club.display_club_summary()

    # Display activities from Set
    print("Planned Activities (" + str(len(selected_club.activities)) + "):")
    if len(selected_club.activities) == 0:
        print("  - No activities registered yet.")
    else:
        for act in selected_club.activities:
            print("  * " + act)

    # Display attendance history from Array
    print("Past Event Attendance History:")
    if len(selected_club.attendance_records) == 0:
        print("  - No events conducted yet.")
    else:
        event_num = 1
        for attendees in selected_club.attendance_records:
            print("  Event " + str(event_num) + ": " + str(attendees) + " students attended")
            event_num += 1
        print("  Average Attendance : " + str(selected_club.get_average_attendance()))


def add_new_club(clubs):
    """
    Creates and registers a new Club.
    Validates input using string methods and membership operators without try/except.
    """
    print("\n--- ADD A NEW CLUB ---")
    club_id = input("Enter Club ID (e.g. C106): ").strip().upper()

    if len(club_id) == 0:
        print("[Error] Club ID cannot be empty.")
        return

    # Check if club ID already exists using membership check
    existing = find_club_by_id(clubs, club_id)
    if existing is not None:
        print("[Error] A club with ID " + club_id + " already exists.")
        return

    name = input("Enter Club Name: ").strip()
    if len(name) == 0:
        print("[Error] Club Name cannot be empty.")
        return

    print("Allowed Categories: " + ", ".join(list(VALID_CATEGORIES)))
    category = input("Enter Category: ").strip()

    # Membership operator check against frozen set
    if category not in VALID_CATEGORIES:
        print("[Error] Invalid category! Must be one of: " + ", ".join(list(VALID_CATEGORIES)))
        return

    day = input("Enter Regular Meeting Day (e.g. Monday): ").strip()
    room = input("Enter Meeting Room/Venue (e.g. Room 204): ").strip()
    if len(day) == 0 or len(room) == 0:
        print("[Error] Meeting Day and Room cannot be empty.")
        return

    # Tuple data structure created for fixed schedule
    meeting_tuple = (day, room)

    budget_input = input("Enter Annual Budget (digits only): ").strip()
    # Input validation using .isdigit()
    if not budget_input.isdigit():
        print("[Error] Budget must be a positive integer.")
        return

    budget = int(budget_input)

    # Instantiate beginner-friendly Club object
    new_club = Club(club_id, name, category, meeting_tuple, budget)
    clubs.append(new_club)
    print("[Success] Club '" + name + "' added successfully with ID: " + club_id)


def add_member_to_club(clubs):
    """Adds a new student member to a chosen club with bitwise role flags."""
    print("\n--- ADD MEMBER TO CLUB ---")
    club_id = input("Enter Club ID to join: ").strip().upper()
    selected_club = find_club_by_id(clubs, club_id)

    # Identity operator check
    if selected_club is None:
        print("[Error] Club not found.")
        return

    roll_no = input("Enter Student Roll Number (digits): ").strip()
    if not roll_no.isdigit():
        print("[Error] Roll number must contain digits only.")
        return

    # Check for duplicate member within this club
    for m in selected_club.members:
        if m["roll_no"] == roll_no:
            print("[Error] Student with Roll Number " + roll_no + " is already a member of this club.")
            return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Student Branch (e.g. CSE, ECE): ").strip()

    if len(name) == 0 or len(branch) == 0:
        print("[Error] Name and Branch cannot be empty.")
        return

    print("Select Member Role:")
    print("1. Standard Member")
    print("2. Member + Event Volunteer")
    print("3. Member + Club Coordinator")
    role_choice = input("Enter choice (1-3): ").strip()

    # Bitwise operators: assignment and bitwise OR (|)
    role_mask = ROLE_MEMBER
    if role_choice == "2":
        role_mask = role_mask | ROLE_VOLUNTEER
    elif role_choice == "3":
        role_mask = role_mask | ROLE_COORDINATOR
    elif role_choice != "1":
        print("[Notice] Invalid role choice, defaulting to Standard Member.")

    member_dict = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "role_mask": role_mask,
    }

    selected_club.add_member(member_dict)
    print("[Success] " + name + " successfully added to " + selected_club.name + "!")


def display_club_members(clubs):
    """Displays all members of a chosen club with decoded bitwise roles."""
    club_id = input("\nEnter Club ID to view members: ").strip().upper()
    selected_club = find_club_by_id(clubs, club_id)

    if selected_club is None:
        print("[Error] Club not found.")
        return

    print("\nMembers of " + selected_club.name + " (" + str(len(selected_club.members)) + " total):")
    if len(selected_club.members) == 0:
        print("No members registered in this club yet.")
        return

    print("Roll No | Name                 | Branch | Role(s)")
    print("-------------------------------------------------------------")
    for m in selected_club.members:
        name_pad = m["name"] + " " * (20 - len(m["name"])) if len(m["name"]) < 20 else m["name"][:20]
        branch_pad = m["branch"] + " " * (6 - len(m["branch"])) if len(m["branch"]) < 6 else m["branch"][:6]
        roles_str = get_role_description(m["role_mask"])
        print(m["roll_no"] + "    | " + name_pad + " | " + branch_pad + " | " + roles_str)


def search_member(clubs):
    """Searches for a student member across all clubs by roll number."""
    roll_no = input("\nEnter Roll Number to search: ").strip()
    if not roll_no.isdigit():
        print("[Error] Roll number must contain digits only.")
        return

    found = False
    print("\nSearch results for Roll Number: " + roll_no)
    for c in clubs:
        for m in c.members:
            if m["roll_no"] == roll_no:
                found = True
                print("--------------------------------------------------")
                print("Club Name : " + c.name + " (" + c.club_id + ")")
                print("Name      : " + m["name"])
                print("Branch    : " + m["branch"])
                print("Role      : " + get_role_description(m["role_mask"]))
                print("--------------------------------------------------")

    if not found:
        print("No student found with Roll Number " + roll_no + " in any club.")


def remove_member_from_club(clubs):
    """Removes a student member from a specific club."""
    club_id = input("\nEnter Club ID: ").strip().upper()
    selected_club = find_club_by_id(clubs, club_id)

    if selected_club is None:
        print("[Error] Club not found.")
        return

    roll_no = input("Enter Roll Number to remove: ").strip()
    removed = selected_club.remove_member(roll_no)

    if removed:
        print("[Success] Member with Roll Number " + roll_no + " was removed from " + selected_club.name + ".")
    else:
        print("[Error] No member with Roll Number " + roll_no + " found in this club.")


def register_activity(clubs):
    """Adds a new activity or workshop to a club's Set of activities."""
    club_id = input("\nEnter Club ID: ").strip().upper()
    selected_club = find_club_by_id(clubs, club_id)

    if selected_club is None:
        print("[Error] Club not found.")
        return

    activity_name = input("Enter New Activity Name: ").strip()
    if len(activity_name) == 0:
        print("[Error] Activity name cannot be empty.")
        return

    # Check set membership operator
    if activity_name in selected_club.activities:
        print("[Notice] Activity '" + activity_name + "' already exists for " + selected_club.name + ".")
        return

    selected_club.add_activity(activity_name)
    print("[Success] Activity '" + activity_name + "' registered successfully!")


def view_and_record_statistics(clubs):
    """
    Demonstrates arithmetic operations, division for mixed types,
    operator precedence, type() function, and array usage.
    """
    club_id = input("\nEnter Club ID for Statistics & Records: ").strip().upper()
    selected_club = find_club_by_id(clubs, club_id)

    if selected_club is None:
        print("[Error] Club not found.")
        return

    print("\n--- STATISTICS & PERFORMANCE: " + selected_club.name.upper() + " ---")
    
    # 1. type() function demonstration
    print("[Data Type Verification]")
    print("Type of Club ID       : " + str(type(selected_club.club_id)))
    print("Type of Budget        : " + str(type(selected_club.budget)))
    print("Type of Meeting Info  : " + str(type(selected_club.meeting_info)))
    print("Type of Attendance Rec: " + str(type(selected_club.attendance_records)))
    
    # 2. Arithmetic calculations
    total_members = len(selected_club.members)
    print("\nTotal Members Registered: " + str(total_members))

    # Float division (/)
    if total_members > 0:
        budget_per_member = selected_club.budget / total_members
        print("Budget Allocated per Member: Rs. " + str(round(budget_per_member, 2)))
    else:
        print("Budget Allocated per Member: N/A (No members)")

    # 3. Array attendance records and float vs floor division
    total_events = len(selected_club.attendance_records)
    print("Total Past Events Recorded: " + str(total_events))
    
    if total_events > 0:
        avg_att = selected_club.get_average_attendance()
        print("Average Event Attendance (Float /): " + str(round(avg_att, 2)))
        
        # Operator precedence formula demonstration:
        # Score = ((total_attendance * 2) + bonus_points) // total_events
        bonus = 10
        score = selected_club.calculate_activity_score(bonus)
        print("Engagement Rating Index (Precedence Demo): " + str(score) + " pts")
    else:
        print("No attendance recorded yet.")

    # Option to record new event attendance in the array
    print("\nWould you like to record attendance for a newly conducted event?")
    record_choice = input("Enter 'Y' to record, or any other key to return: ").strip().upper()
    if record_choice == "Y":
        count_input = input("Enter number of student attendees (digits): ").strip()
        if count_input.isdigit():
            count = int(count_input)
            selected_club.record_attendance(count)
            print("[Success] Recorded " + str(count) + " attendees into event attendance array!")
            print("Updated Average Attendance: " + str(round(selected_club.get_average_attendance(), 2)))
        else:
            print("[Error] Attendance count must be a positive integer.")


def main():
    """Main function controlling the application loop."""
    print("Initializing College Club Management System...")
    clubs = initialize_sample_data()
    print("Sample data loaded: " + str(len(clubs)) + " clubs ready.")

    # Control flow: while loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        # Membership operator check: in
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("[Warning] Invalid choice! Please enter a number between 1 and 10.")
            continue

        # Control flow: if / elif / else
        if choice == "1":
            display_all_clubs(clubs)
        elif choice == "2":
            view_club_details(clubs)
        elif choice == "3":
            add_new_club(clubs)
        elif choice == "4":
            add_member_to_club(clubs)
        elif choice == "5":
            display_club_members(clubs)
        elif choice == "6":
            search_member(clubs)
        elif choice == "7":
            remove_member_from_club(clubs)
        elif choice == "8":
            register_activity(clubs)
        elif choice == "9":
            view_and_record_statistics(clubs)
        elif choice == "10":
            # Control flow: break
            print("\nThank you for using the College Club Management System!")
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
