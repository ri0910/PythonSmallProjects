import string
import random


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password_generator():
    password_length = int(input("Enter the length of your password : "))
    num_of_passwords = int(input("Enter the number of passwords : "))
    random.shuffle(characters)
    for x in range(num_of_passwords):
        password = []
        for y in range(password_length):
            password.append(random.choice(characters))
            random.shuffle(password)
        password = "".join(password)
        print(f"Password {str(x+1)} : {str(password)}")

password_generator()