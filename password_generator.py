
import string
import secrets

# Password Generator
print("Welcome to Password Generator!")

length = int(input("Enter the desired password length: "))

if length < 1:
    print("Please enter a valid password length.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))

    print("Generated Password:", password)
