# Michael Witter
# October 27, 2026
# P4LAB2 - Multiplication Tables
# Use loops to display multiplication tables and repeat until the user is done.

# Pseudocode:
# Display the program title and student's name.
# Set the run-again answer to yes.
# While the run-again answer is yes:
#     Ask the user to enter an integer.
#     If the integer is zero or greater:
#         Use a for loop with multipliers from 1 through 12.
#         Multiply the integer by each multiplier and display the equation.
#     Otherwise, display that negative values are not accepted.
#     Ask whether the user wants to run the program again.
#     While the answer is neither yes nor no, ask for a valid answer.
#     If the answer is yes, repeat; if it is no, exit the loop.
# Display an exit message.

print("P4LAB2 - Multiplication Tables - Michael Witter")
print()

run_again = "yes"

while run_again == "yes":
    number = int(input("Enter an integer: "))
    print()

    if number >= 0:
        for multiplier in range(1, 13):
            print(f"{number} * {multiplier} = {number * multiplier}")
    else:
        print("Negative values are not accepted.")

    print()
    run_again = input("Would you like to run the program again? (yes/no): ")
    while run_again != "yes" and run_again != "no":
        run_again = input('Please enter "yes" or "no": ')
    print()

print("Exiting program. Goodbye!")
