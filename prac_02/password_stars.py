"""
Get a password and display asterisks for the length

"""

MINIMUM_LENGTH = 3

def main():
    """Get and print a password"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(minimum_length):
    """Get password that meets minimum length"""
    password = input(f"Enter password with a minimum of {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(f"Enter password with a minimum of {minimum_length} characters: ")
    return password

def print_asterisks(sequence):
    """Print asterisks for number of characters"""
    print('*' * len(sequence))

main()