"""
Program to determine score status
"""

# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")

import random

def main():
    """Program to calculate result input"""
    score = float(input("Enter score: "))
    print(calculate_result(score))

    random_score= random.randint(0,100)
    print(f"Random score: {random_score}")
    print(calculate_result(random_score))

def calculate_result(score):
    """Calculate result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()