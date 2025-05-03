# Maurice Davis 4-30-2025
# CIS129 Lab 11 Excercise 9.3

"""
This program allows an instructor to enter student records—first name, last name, 
and three exam grades—and saves the data into a CSV file named 'grades.csv'. 
It uses input validation to ensure names contain only valid characters and 
 grades are integers between 0 and 100. The data can later be used for reporting 
 or analysis of student performance.
"""
import csv

def main():
# Open the CSV file for writing
    with open('grades.csv', mode='w', newline='') as class_grades:
        writer = csv.writer(class_grades)
        writer.writerow(['FirstName', 'LastName', 'Exam1', 'Exam2', 'Exam3'])

        while True:
            first_name = get_valid_name("Enter student's first name (or '-1' to quit):\n ")
            if first_name == '-1':
                print("Program Terminated.")
                break

            last_name = get_valid_name("Enter student's last name (or '-1' to quit):\n ")
            if last_name == '-1':
                print("Program Terminated.")
                break

            exam1 = get_valid_grade("Enter exam 1 grade (0–100):\n ")
            exam2 = get_valid_grade("Enter exam 2 grade (0–100):\n")
            exam3 = get_valid_grade("Enter exam 3 grade (0–100):\n")

            writer.writerow([first_name, last_name, exam1, exam2, exam3])
            print("Student record added.\n")


def is_valid_name(name):
    """Check if name contains only valid characters."""
    return name.replace("-", "").replace("'", "").isalpha()

def get_valid_name(prompt):
    """Prompt for a valid name."""
    while True:
        name = input(prompt).strip()
        if name.lower() == '-1':
            return '-1'
        elif is_valid_name(name):
            return name
        else:
            print("Invalid name. Only alphabetic characters, hyphens, and apostrophes are allowed.")

def get_valid_grade(prompt):
    """Prompt for a valid grade (integer between 0 and 100)."""
    while True:
        grade_input = input(prompt).strip()
        if not grade_input.isdigit():
            print("Grade must be a number between 0 and 100.")
            continue
        grade = int(grade_input)
        if 0 <= grade <= 100:
            return grade
        else:
            print("Grade must be between 0 and 100.")

main()