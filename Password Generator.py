import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 1:
            print("Password length must be at least 1 character.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
