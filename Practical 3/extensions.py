"""Practical 3 - Extension tasks B to E.
(Task A, the average option, is in utility.py.)
Run with: python extensions.py
"""

from utility import add, show_summary


# ---------- Task B: grade_from_marks ----------
def grade_from_marks(marks, maximum=100):
    """Return a grade for the marks, after validating the range.

    NOTE: the grade bands below are PLACEHOLDERS. Replace them with the
    bands your instructor gives you.
    """
    if maximum <= 0:
        raise ValueError("maximum must be greater than 0.")
    if not 0 <= marks <= maximum:
        raise ValueError(f"marks must be between 0 and {maximum}.")

    percent = marks / maximum * 100
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


print("--- Task B: grade_from_marks ---")
print("85 out of 100 ->", grade_from_marks(85))
print("42 out of 50  ->", grade_from_marks(42, 50))
try:
    grade_from_marks(120)
except ValueError as error:
    print("Out-of-range marks ->", error)


# ---------- Task C: scope ----------
def make_local():
    secret = "I exist only inside this function"
    return secret


print("\n--- Task C: scope ---")
make_local()
try:
    print(secret)
except NameError as error:
    print("NameError:", error)
# Explanation: `secret` is a local variable. It is created when make_local()
# runs and destroyed when the function ends, so the outside code cannot see it.


# ---------- Task D: add(2, 4, 6, 8) ----------
print("\n--- Task D: *args ---")
print("add(2, 4, 6, 8) =", add(2, 4, 6, 8))


# ---------- Task E: show_summary with keyword arguments ----------
print("\n--- Task E: **kwargs ---")
show_summary(student="Student A", practical=3, status="Complete")
