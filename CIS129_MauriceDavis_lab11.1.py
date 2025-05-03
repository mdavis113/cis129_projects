# Maurice Davis 4-30-2025
# CIS129 Lab 11 Excercise 9.1
"""
This script collects valid grades from the user and saves them to grades.txt
Grades must be integers from 0 to 100. Use -1 to finish entering grades.
"""


def main ():
    # Opens the file for writing
    with open('grades.txt', 'w') as class_grades:
        print("Start entering grades. Type -1 to finish.")
        while True:
            grade = get_valid_grade()
            if grade == -1:
                print("Finished entering grades.")
                break
            class_grades.write(f"{grade}\n")
            print("Grade saved.")

def get_valid_grade():
    """Prompt for a grade and validate it."""
    while True:
        grade_input = input("Enter grade (0–100) or -1 to end: ").strip()

        if grade_input == '-1':
            return -1

        if not grade_input.isdigit():
            print("Invalid input. Please enter a number between 0 and 100 or -1 to quit.")
            continue

        grade = int(grade_input)
        if 0 <= grade <= 100:
            return grade
        else:
            print("Grade must be between 0 and 100.")

main()