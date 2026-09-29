# Michael Witter
# September 29, 2026
# P2HW2
# This program collects six module grades, stores them in a list,
# and displays the lowest, highest, total, and average grade.

# Pseudocode:
# Ask the user to enter a grade for Modules 1 through 6.
# Store the six grades in a list.
# Find the lowest grade, highest grade, sum, and average.
# Display the results in a formatted report.

module_1 = int(input("Enter grade for Module 1: "))
module_2 = int(input("Enter grade for Module 2: "))
module_3 = int(input("Enter grade for Module 3: "))
module_4 = int(input("Enter grade for Module 4: "))
module_5 = int(input("Enter grade for Module 5: "))
module_6 = int(input("Enter grade for Module 6: "))

module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{sum_of_grades}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("--------------------------------")