# Maurice Davis 4-30-25
# CIS 129 Lab 11.2
"""
This program reads a list of student grades from a file named 'grades.txt',
where each line in the file contains a single integer grade. It processes the
grades by:

1. Converting each line to an integer.
2. Displaying each individual grade.
3. Calculating and displaying the total number of grades, the sum of all grades,
   and the average grade (rounded to two decimal places).

The program assumes the file exists and contains only valid integer grades.
"""

# Open the file for reading
with open('grades.txt', 'r') as class_grades:
    # Read all lines and convert to integers
    grades = [int(line.strip()) for line in class_grades]

# Display individual grades
print("Grades entered:")
for grade in grades:
    print(grade)

# Calculate total, count, and average
total = sum(grades)
count = len(grades)
average = total / count if count > 0 else 0

# Display results
print(f'\nTotal: {total}')
print(f'Number of grades: {count}')
print(f'Average: {average:.2f}')
