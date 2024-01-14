import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get user input for password complexity
    complexity_options = ["easy", "medium", "hard"]
    while True:
        complexity = input("Choose password complexity (easy/medium/hard): ").lower()
        if complexity in complexity_options:
            break
        else:
            print("Invalid choice. Please choose from 'easy', 'medium', or 'hard'.")

    # Generate and display the password
    password = generate_password(length, complexity)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
