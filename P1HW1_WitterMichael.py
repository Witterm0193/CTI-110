# Michael Witter
# 9/17/2026
# Assignment Name: P1HW1 - Converting User Input / Order of Precedence
# This program calculates an exponent from user input, then adds two
# integers and subtracts a third from the sum.

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent

print()
print(str(base) + " raised to the power of " + str(exponent) + " is " + str(result) + " !!")
print()

print("-----Addition and Subtraction-----")
print()

start = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))

final_result = start + add_num - sub_num

print()
print(str(start) + " + " + str(add_num) + " - " + str(sub_num) + " is equal to " + str(final_result))
