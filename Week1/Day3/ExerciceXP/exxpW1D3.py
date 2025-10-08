# #### Exercice 1 : Cats
# Step 1: create cat objects

class cat(): # creation of the class named Cat
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# 3 cat objects
cat1 = ["Tchipie", 1]
cat2 = ["Simba", 3]
cat3 = ["Nala", 2]

# step2: create a function to find the oldest cat
# conditions to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        oldest = cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
        oldest = cat2
    else: 
        oldest = cat3

    return oldest

# Step 3: call the function and print oldest cat's details

oldest_cat = find_oldest_cat(cat1, cat2, cat3) # variable to call the function created before

print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.”)
      

# #### Exercice 2 : Dogs

# Step 1: create a dog class 

class Dog(): 
    def __init__ (self, dog_name, dog_height ):
        self.name = dog_name
        self.height = dog_height
    def bark(self):
        print(f"(self.name) goes woof!")
    def jump(self):
        print(f"(self.name) jumps (self.height * 2) cm high!")

# step 2: create dog objects

dog1 = [Davids_dog, 45]
dog2 = [Sarahs_dog, 20]

# Step 3: Print Dog details and call method

; 
print(f"(dog1.name) is (dog1.height) cm tall"); 
print(f"(dog2.name) is (dog2.height) cm tall")

# call method
dog1.bark()
dog1.jump()

dog2.bark()
dog2.jump()

# Step 4: Compare dog Sizes

if dog1.height > dog2.height: 
    print(f"the bigger dog is {dog1.name}")
if dog2.height > dog1.height: 
    print(f"the bigger dog is {dog2.name}")
else:
    print("Both dogs are the sale height.")


# #### Exercice 3: Who's the song producer

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# Call the method to sing the song
stairway.sing_me_a_song()

# #### Exercice 4: Afternoon at the zoo

# Step1: Define the zoo class

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = [] #  empty list to store animal names
    def add_animal(self, new_animal): 
        if new_animal not in self.animals: # sanity check not to have a double entry of an animal
            self.animals.append(new_animal)
            print(f"{new_animal}  added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")
    def get_animals(self): # adding a method get_animals()
        print(f"Animals currently in {self.name}:")
        for animal in self.animals:
            print(f"- {animal}")
    def sell_animal(self, animal_sold): # adding a method sell_animal()
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold and removed from the zoo.")
        else:
            print(f"{animal_sold} is not found in the zoo.")
    def sort_animals(self): # addinf a method sort_animal()
        self.animals.sort()
        grouped = {}
        # Group animals by first letter
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped: # avoiding duplicates
                grouped[first_letter] = [animal]
            else:
                grouped[first_letter].append(animal)
        return grouped

# Step 2: Create the zoo
my_zoo = Zoo("Central Park")

# Step 3: Testing Add animals
my_zoo.add_animal("Elephant")
my_zoo.add_animal("Tiger")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Eagle")
my_zoo.add_animal("Snake")
my_zoo.add_animal("Tiger") #testing duplicates

# Testing  Get animals
my_zoo.get_animals()

# Testing Sort and group animals
grouped_animals = my_zoo.sort_animals()

# Testing Display the grouped dictionary
print("\nGrouped animals:")
for letter, names in grouped_animals.items():
    print(f"{letter}: {names}")
