import random
import string

def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    length=int(input("Enter the desired password length:"))
    password=generate_password(length)
    
    print(f"Generated password:{password}")
    
password_generator()
