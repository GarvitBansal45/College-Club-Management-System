"""
test_project.py - Verification suite for College Club Management System.
Uses ONLY plain Python assert statements (no unittest, pytest, or external frameworks).
Run with: python tests/test_project.py
"""

import sys
import os

# Add parent directory to path so club and main modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from club import (
    Club,
    VALID_CATEGORIES,
    ROLE_MEMBER,
    ROLE_VOLUNTEER,
    ROLE_COORDINATOR,
    get_role_description,
)
from main import initialize_sample_data, find_club_by_id


def test_club_initialization():
    """Tests basic Club object attributes and tuple handling."""
    print("Testing Club initialization...")
    meeting_tuple = ("Monday", "Room 101")
    c = Club("TEST01", "Robotics Society", "Technical", meeting_tuple, 10000)

    assert c.club_id == "TEST01", "Club ID does not match"
    assert c.name == "Robotics Society", "Club name does not match"
    assert c.category == "Technical", "Club category does not match"
    assert isinstance(c.meeting_info, tuple), "Meeting info must be a tuple"
    assert c.meeting_info[0] == "Monday", "Meeting day tuple element incorrect"
    assert c.meeting_info[1] == "Room 101", "Meeting room tuple element incorrect"
    assert c.budget == 10000, "Budget does not match"
    assert len(c.members) == 0, "Initial members list should be empty"
    assert len(c.activities) == 0, "Initial activities set should be empty"
    assert len(c.attendance_records) == 0, "Initial attendance array should be empty"
    print("[PASS] Club initialization passed.")


def test_member_addition_and_removal():
    """Tests list operations for members."""
    print("Testing member addition and removal...")
    c = Club("TEST02", "Music Club", "Cultural", ("Wednesday", "Studio"), 5000)
    m1 = {"roll_no": "2001", "name": "Rohan", "branch": "CSE", "role_mask": ROLE_MEMBER}
    m2 = {"roll_no": "2002", "name": "Meera", "branch": "ECE", "role_mask": ROLE_MEMBER | ROLE_VOLUNTEER}

    c.add_member(m1)
    c.add_member(m2)
    assert len(c.members) == 2, "Members list should have 2 elements"
    assert c.members[0]["roll_no"] == "2001", "First member roll number incorrect"
    assert c.members[1]["roll_no"] == "2002", "Second member roll number incorrect"

    # Test removal
    removed = c.remove_member("2001")
    assert removed is True, "remove_member should return True for existing member"
    assert len(c.members) == 1, "Members list should have 1 element after removal"
    assert c.members[0]["roll_no"] == "2002", "Remaining member is incorrect"

    # Test removing non-existent member
    removed_non_existent = c.remove_member("9999")
    assert removed_non_existent is False, "remove_member should return False for non-existent member"
    assert len(c.members) == 1, "Members list length should remain unchanged"
    print("[PASS] Member addition and removal passed.")


def test_activity_set():
    """Tests set uniqueness for club activities."""
    print("Testing activity set operations...")
    c = Club("TEST03", "Coding Club", "Technical", ("Thursday", "Lab 1"), 8000)
    c.add_activity("Hackathon")
    c.add_activity("CodeSprint")
    # Adding duplicate
    c.add_activity("Hackathon")

    assert isinstance(c.activities, set), "Activities must be stored in a set"
    assert len(c.activities) == 2, "Duplicate activity was not prevented by set"
    assert "Hackathon" in c.activities, "'Hackathon' should be in activities set"
    assert "CodeSprint" in c.activities, "'CodeSprint' should be in activities set"
    print("[PASS] Activity set uniqueness passed.")


def test_attendance_array_and_calculations():
    """Tests array operations, float division, and operator precedence."""
    print("Testing attendance array and calculations...")
    c = Club("TEST04", "Drama Club", "Cultural", ("Friday", "Hall"), 6000)
    
    # Empty attendance checks
    assert c.get_average_attendance() == 0.0, "Average with 0 events should be 0.0"
    assert c.calculate_activity_score(10) == 0, "Activity score with 0 events should be 0"

    # Record attendance in array
    c.record_attendance(50)
    c.record_attendance(70)
    c.record_attendance(60)

    assert len(c.attendance_records) == 3, "Attendance array should have 3 items"
    # Total = 50 + 70 + 60 = 180; Average = 180 / 3 = 60.0
    avg = c.get_average_attendance()
    assert avg == 60.0, "Average attendance calculation is incorrect"
    assert isinstance(avg, float), "Average attendance should return a float"

    # Precedence formula: (total_attendance * 2 + bonus_points) // total_events
    # (180 * 2 + 15) // 3 = (360 + 15) // 3 = 375 // 3 = 125
    bonus = 15
    score = c.calculate_activity_score(bonus)
    assert score == 125, "Precedence calculation returned incorrect score"
    assert isinstance(score, int), "Score must be an integer due to // floor division"
    print("[PASS] Attendance array and calculation formulas passed.")


def test_bitwise_role_permissions():
    """Tests bitwise OR (|) for granting roles and bitwise AND (&) for checks."""
    print("Testing bitwise role permission masks...")
    # Base member
    role_mask = ROLE_MEMBER
    assert role_mask & ROLE_MEMBER != 0, "Member role bit should be active"
    assert (role_mask & ROLE_VOLUNTEER) == 0, "Volunteer role bit should not be active"
    assert get_role_description(role_mask) == "Member"

    # Add volunteer role using bitwise OR
    role_mask = role_mask | ROLE_VOLUNTEER
    assert role_mask & ROLE_MEMBER != 0, "Member role bit should remain active"
    assert role_mask & ROLE_VOLUNTEER != 0, "Volunteer role bit should be active"
    assert (role_mask & ROLE_COORDINATOR) == 0, "Coordinator role bit should not be active"
    assert get_role_description(role_mask) == "Member, Volunteer"

    # Add coordinator role
    role_mask = role_mask | ROLE_COORDINATOR
    assert role_mask & ROLE_COORDINATOR != 0, "Coordinator role bit should be active"
    assert get_role_description(role_mask) == "Member, Volunteer, Coordinator"
    print("[PASS] Bitwise role permissions passed.")


def test_sample_data_and_search():
    """Tests sample data loading and identity checks."""
    print("Testing sample data initialization and search...")
    clubs = initialize_sample_data()
    assert len(clubs) == 5, "Sample data should initialize exactly 5 clubs"

    # Test search with identity check
    c101 = find_club_by_id(clubs, "C101")
    assert c101 is not None, "Club C101 should be found"
    assert c101.name == "Coding Club", "Club C101 name mismatch"

    c_fake = find_club_by_id(clubs, "C999")
    assert c_fake is None, "Non-existent club should return None"
    print("[PASS] Sample data and search passed.")


def run_all_tests():
    """Runs all test functions sequentially."""
    print("==================================================")
    print("   RUNNING PROJECT TESTS (PLAIN PYTHON ASSERTS)   ")
    print("==================================================")
    test_club_initialization()
    test_member_addition_and_removal()
    test_activity_set()
    test_attendance_array_and_calculations()
    test_bitwise_role_permissions()
    test_sample_data_and_search()
    print("==================================================")
    print("   ALL TESTS PASSED SUCCESSFULLY! (6/6 TEST SUITES)")
    print("==================================================")


if __name__ == "__main__":
    run_all_tests()
