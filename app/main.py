import random

def generate_random_number():
    return random.randint(1, 100)

print("Random number:", generate_random_number())

#sdf

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print(name)
        print(email)
    
user = User("Natasha", "nat@yahoo.com")

#sdf