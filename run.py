import random
import string

#Prompt user for name & surname
def details():
    name = input("Enter your name:")
    surname = input("Enter your last name: ")

    username = name[0:2] + surname[:-3]

    return username    
    
def generate(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
    
def run():
    username = details()
    password = generate()

    print(username)
    print(password)


if __name__ == '__main__':
    run()
