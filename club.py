"""
club.py - Module defining the Club class and role permission constants.
College Club Management System (First-Year Python Essentials Project)
"""

import array

# Frozen set of standard, immutable club categories recognized by the college
VALID_CATEGORIES = frozenset(["Technical", "Cultural", "Sports", "Literary"])

# Bitwise role flags for club members
# 1 (001 in binary) = Basic Member
# 2 (010 in binary) = Event Volunteer
# 4 (100 in binary) = Club Coordinator
ROLE_MEMBER = 1
ROLE_VOLUNTEER = 2
ROLE_COORDINATOR = 4


def get_role_description(role_mask):
    """
    Returns a readable string of assigned roles using bitwise AND (&) checks.
    """
    roles = []
    # Bitwise AND to check if specific role bit is active
    if role_mask & ROLE_MEMBER:
        roles.append("Member")
    if role_mask & ROLE_VOLUNTEER:
        roles.append("Volunteer")
    if role_mask & ROLE_COORDINATOR:
        roles.append("Coordinator")
    
    if len(roles) == 0:
        return "None"
    return ", ".join(roles)


class Club:
    """
    Represents a student club in the college.
    Stores basic details, member records, activities, and event attendance counts.
    """
    def __init__(self, club_id, name, category, meeting_info, budget):
        # Basic attributes
        self.club_id = club_id
        self.name = name
        self.category = category
        # Tuple data structure: stores fixed meeting schedule (Day, Room)
        self.meeting_info = meeting_info
        # Numeric attribute
        self.budget = budget
        # List data structure: stores member dictionaries
        self.members = []
        # Set data structure: stores unique activity names
        self.activities = set()
        # Array data structure: stores integer attendance counts of past events
        self.attendance_records = array.array('i', [])

    def add_member(self, member_dict):
        """Adds a student member dictionary to the club's member list."""
        self.members.append(member_dict)

    def remove_member(self, roll_no):
        """
        Removes a member matching the given roll number.
        Returns True if found and removed, False otherwise.
        """
        target_index = -1
        for i in range(len(self.members)):
            if self.members[i]["roll_no"] == roll_no:
                target_index = i
                break
        
        if target_index != -1:
            self.members.pop(target_index)
            return True
        return False

    def add_activity(self, activity_name):
        """Adds an activity name to the set of activities."""
        self.activities.add(activity_name)

    def record_attendance(self, count):
        """Appends the event attendance count to the attendance array."""
        self.attendance_records.append(count)

    def get_average_attendance(self):
        """
        Calculates average attendance using arithmetic division.
        Demonstrates float division (/) and mixed data type handling.
        """
        total_events = len(self.attendance_records)
        if total_events == 0:
            return 0.0
        
        total_attendees = 0
        for count in self.attendance_records:
            total_attendees += count
        
        # Float division (/) gives a float result
        avg = total_attendees / total_events
        return avg

    def calculate_activity_score(self, bonus_points):
        """
        Demonstrates operator precedence and associativity:
        parentheses () are evaluated first, then multiplication (*),
        then addition (+), followed by integer floor division (//).
        Formula: ((total_attendance * 2) + bonus_points) // total_events
        """
        total_events = len(self.attendance_records)
        if total_events == 0:
            return 0
        
        total_attendance = 0
        for count in self.attendance_records:
            total_attendance += count
        
        # Precedence demonstration:
        # 1. total_attendance * 2
        # 2. + bonus_points
        # 3. // total_events
        score = (total_attendance * 2 + bonus_points) // total_events
        return score

    def display_club_summary(self):
        """Prints a simple formatted overview of the club."""
        print("--------------------------------------------------")
        print("Club ID          : " + str(self.club_id))
        print("Club Name        : " + str(self.name))
        print("Category         : " + str(self.category))
        print("Regular Meeting  : " + str(self.meeting_info[0]) + " at " + str(self.meeting_info[1]))
        print("Annual Budget    : Rs. " + str(self.budget))
        print("Total Members    : " + str(len(self.members)))
        print("Total Activities : " + str(len(self.activities)))
        print("Events Conducted : " + str(len(self.attendance_records)))
        print("--------------------------------------------------")
