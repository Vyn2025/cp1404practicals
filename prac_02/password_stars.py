"""
CP1404 Password stars
"""

def main():
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print_stars(password)

def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print("Password too short")
        password = input("Enter password: ")
    return password

def print_stars(password):
    print("*" * len(password))

main()
