# Michael Witter
# September 29, 2026
# P2LAB2
# This program stores vehicle MPG values in a dictionary and
# calculates the gallons of gas needed for a trip.

# Pseudocode:
# Create a dictionary of vehicles and their MPG values.
# Print the available vehicle keys.
# Ask the user for a vehicle and display its MPG.
# Ask for the number of miles to drive.
# Calculate and display gallons of gas needed.

car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = car_mpg.keys()
print(keys)

vehicle = input("Enter a vehicle: ")
mpg = car_mpg[vehicle]

print(f"The {vehicle} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")