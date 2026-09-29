# Michael Witter
# September 29, 2026
# P2HW1
# This program calculates travel expenses and displays
# the results in a formatted travel expense report.

# Pseudocode:
# Ask the user for their travel budget and destination.
# Ask the user for fuel, hotel, and food costs.
# Calculate the remaining budget.
# Display the travel expenses in formatted columns.

budget = float(input("Enter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))

hotel = float(input(
    "\nApproximately, how much will you need for accommodation/hotel? "
))

food = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - gas - hotel - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print()
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")