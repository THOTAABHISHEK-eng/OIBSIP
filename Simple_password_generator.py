

import random
import string

def generate_password(length, letters, numbers, symbols):
    characters = ""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Abhishek's Password Generator!")

    while True:
        try:
            length = int(input("Enter desired password length (1-128): "))
            if length < 1 or length > 128:
                print("Length must be between 1 and 128.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
