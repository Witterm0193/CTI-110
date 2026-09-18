# Your Name
# Date
# Assignment Name: P1HW2 - Travel Budget Calculator
# This program asks the user for a travel budget, their destination,
# and three expense amounts (gas, accommodation, food). It adds the
# expenses together, subtracts that total from the budget, and
# displays a summary of the trip's costs and remaining balance.

# Step 1: Ask the user for their total budget
budget = int(input("Enter Budget: "))
print()

# Step 2: Ask the user where they are traveling to
destination = input("Enter your travel destination: ")
print()

# Step 3: Ask the user how much they expect to spend on gas
gas = int(input("How much do you think you will spend on gas? "))
print()

# Step 4: Ask the user how much they need for accommodation/hotel
accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# Step 5: Ask the user how much they need for food
food = int(input("Last, how much do you need for food? "))
print()

# Step 6: Add up all three expenses to get the total spent
total_expenses = gas + accommodation + food

# Step 7: Subtract total expenses from the budget to get what's left
remaining_balance = budget - total_expenses

# Step 8: Display a summary of the trip expenses and remaining balance
print("------------Travel Expenses------------")
print("Location: " + destination)
print("Initial Budget: " + str(budget))
print()
print("Fuel: " + str(gas))
print("Accomodation: " + str(accommodation))
print("Food: " + str(food))
print()
print("Remaining Balance: " + str(remaining_balance))
