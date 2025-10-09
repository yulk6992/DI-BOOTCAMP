# ##### Exercice 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class siamese(Cat): # Step 1: create the siamese class, no specifics method to be applied
    def sing(self, sounds):
        return f'{sounds}'

# step 2: create a List of Cat Instances

# giving each cat a name and age
Bengal_obj = Bengal('Simba', 3)
Chartreux_obj = Chartreux('Nala', 4)
siamese_obj = siamese('chipie', 6)

all_cats = [Bengal_obj, Chartreux_obj, siamese_obj]

# step 3: create a pets instance

sara_pets = Pets(all_cats)

# step 4: Take cats for a walk

sara_pets.walk()

# note that Exercice 2 is saved as exxpW1D4_Dog_class.py

# ##### Exercice 3: Dogs Domesticated

# Step 1: Import the dog Class

from exxpW1D4_Dog_class import Dog

# Step 2: Create the pet Dog Class

# just for the purpose of this exercice, copying the previous Dog Class here

class Dog: 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self): 
        return f"{self.name} is barking"
    def run_speed(self): 
        return self.weight / self.age *10
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else: 
            return f"it's a draw between {self.name} and {other_dog.name}!"
    
# Pet Dog class that inherits from the dog Class

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Step 3: Test PetDog methods

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

# ##### Exercice 4: Family And Person Classes

# Step 1: create the Person Class

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  # initialized as empty string

    def is_18(self):
        if self.age >= 18: 
            return True
        else:
            return False

# Step 2: Create the family class

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # list of Person objects

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"{first_name} {self.last_name} has been born into the family.")

    def check_majority(self, first_name):
        # Find the person by first name
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name} {member.last_name}, Age: {member.age}")

# Step 3 : Test the methods

# Create a family
smith_family = Family("Smith")

# Add family members
smith_family.born("Alice", 17)
smith_family.born("Bob", 20)
smith_family.born("Charlie", 15)

# Check majority
smith_family.check_majority("Bob")
smith_family.check_majority("Alice")

# Display family info
smith_family.family_presentation()