import random
import string

def generate_password():
    try:
        length = int(input("enter the desired length for the password: "))

        if length <= 0:
            print("please enter a positive number for the length.")
            return

        all_characters = string.ascii_letters + string.digits + string.punctuation
        
        password = "".join(random.choice(all_characters) for i in range(length))
        
        print(f"generated password: {password}")

    except ValueError:
        print("invalid input. please enter a number.")

if __name__ == "__main__":
    generate_password()