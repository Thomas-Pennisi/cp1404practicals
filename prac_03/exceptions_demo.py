"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the user inputs text or symbols (Not an integer).

2. When will a ZeroDivisionError occur? When the user inputs a 0 as the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, if you check if
the denominator is a valid number before dividing
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")