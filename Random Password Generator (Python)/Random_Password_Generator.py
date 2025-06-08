import random
import string
import pyperclip

print("=== 🔐 Random Password Generator ===")
print("Features:")
print("1. Generates a strong random password of your desired length.")
print("2. Includes uppercase, lowercase, digits, and special characters.")
print("3. Automatically copies the generated password to clipboard.")
print("4. Displays the generated password on screen.\n")

pass_len = int(input("What is the Password Length you want = "))

char_values = string.ascii_letters + string.digits + string.punctuation
password = ""
for _ in range(pass_len):
    password += random.choice(char_values)

# Copy to clipboard
pyperclip.copy(password)

print("\nYour Random Password is:", password)
print("✅ Password has been copied to clipboard!")