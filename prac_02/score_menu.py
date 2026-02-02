"""
CP1404/CP5632 - Practical
Score menu program
"""

def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def get_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    print("*" * int(score))

def main():
    score = get_valid_score()

    MENU = """
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            result = get_score_result(score)
            print(result)

        elif choice == "S":
            print_stars(score)

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")

main()
