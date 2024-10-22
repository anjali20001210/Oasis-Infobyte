import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    # Define character sets
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z and A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*() etc.

    # If no character set is selected, raise an error
    if not characters:
        raise ValueError("You must select at least one character type (letters, digits, symbols).")

    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Input validation for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Ask user for character set preferences
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    try:
        # Generate and display the password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nYour random password is: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
