"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def get_score_result(score):
    """Return the result string for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(f"User score {score} is {result}")

    if result == "Excellent":
        print("You get a prize!")

    random_score = random.uniform(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random: {int(random_score)} = {random_result}")


main()
