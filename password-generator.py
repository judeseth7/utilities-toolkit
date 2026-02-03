import random
import string

def generate_password(length):
    password_character_pool = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        choice = random.choice(password_character_pool)
        password += choice
    return password


try:
    length = int(input("Enter password length: "))
    if length >= 1:
        pw = generate_password(length)
        print(pw)
    else: 
        print("Enter number greater than 0")
except ValueError:
    print("Enter a valid number: ")
