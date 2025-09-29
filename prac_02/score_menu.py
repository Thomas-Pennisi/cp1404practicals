"""
Program that displays menu and prints results
"""

MENU = "(G)et valid score\n(P)rint Result\n(S)how stars\n(Q)uit"

def main():
    """Menu and results program"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(calculate_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell")

def get_valid_score():
    """Get valid score"""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter a valid score (0-100): "))
    return score

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