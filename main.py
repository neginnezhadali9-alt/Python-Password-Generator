# Password-Generator

import secrets 
import string 

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        length = int(input("Enter password length:"))

        if length < 12:
            print("Password must be at least 12 characters.")
        else:
            break

    except ValueError:
        print("Please enter a valid number!")

password = ""

password += secrets.choice(string.ascii_letters)
password += secrets.choice(string.digits)
password += secrets.choice(string.punctuation)

for i in range(length - 3):
    password += secrets.choice(characters)

password_list = list(password)

secrets.SystemRandom().shuffle(password_list)

password = "".join(password_list)

print("Generated password:", password)

    
        
    
