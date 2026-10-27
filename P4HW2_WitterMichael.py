# Michael Witter
# October 27, 2026
# P4HW2 - Salary Calculator
# Calculate employee pay and running totals until the name entered is Done.

# Pseudocode:
# Display the student's name and the program title.
# Set the employee count and all pay totals to zero.
# Ask for an employee name, or Done to finish.
# While the employee name is not exactly Done:
#     Ask for the employee's pay rate and hours worked.
#     If hours worked exceed 40:
#         Set overtime hours to hours worked minus 40.
#         Calculate overtime pay at one and a half times the pay rate.
#         Calculate regular pay for 40 hours.
#     Otherwise:
#         Set overtime hours and overtime pay to zero.
#         Calculate regular pay for all hours worked.
#     Add regular pay and overtime pay to get gross pay.
#     Display the employee's name, hours, rate, and pay information.
#     Add each pay amount to its running total.
#     Increase the employee count by one.
#     Ask for another employee name, or Done to finish.
# Display the employee count and the overtime, regular, and gross pay totals.

print("P4HW2 - Salary Calculator - Michael Witter")
print()

employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

employee_name = input('Enter employee name or "Done" to terminate: ')

while employee_name != "Done":
    pay_rate = float(input("Enter employee pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0.0
        overtime_pay = 0.0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print()
    print("---------------------------------------------------------------")
    print(f"Employee name: {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}"
          f"{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("---------------------------------------------------------------")
    print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}"
          f"{overtime_pay:<15.2f}{regular_pay:<15.2f}${gross_pay:.2f}")
    print()

    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay
    employee_count = employee_count + 1

    employee_name = input('Enter employee name or "Done" to terminate: ')

print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
