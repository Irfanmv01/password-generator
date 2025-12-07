import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

print("\nRandom Password Generator...\n")
user_length = int(input("Enter the required length > "))
password = generate_password(user_length)
print(f"\nYour generated password is: {password}\n")