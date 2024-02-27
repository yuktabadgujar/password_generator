import string
import random

def generate_password(length=12):
    """
    Generate a strong, random password.

    Args:
        length (int): The length of the password. Default is 12.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    """
    Generate multiple strong, random passwords.

    Args:
        num_passwords (int): The number of passwords to generate.
        length (int): The length of each password. Default is 12.

    Returns:
        list: A list of generated passwords.
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    """
    Main function to generate random passwords based on user input.
    """
    try:
        print("Welcome to the Secure Password Generator!")
        print("This tool generates strong, random passwords for your security needs.")
        length = int(input("Enter the length of the password(s): "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if length <= 0 or num_passwords <= 0:
            print("Please enter valid length and number of passwords.")
            return

        passwords = generate_multiple_passwords(num_passwords, length)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"Password {i}: {password}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
