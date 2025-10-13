class Farm: # Create a Farm Class
    def __init__(self, farm_name): # Create an init method with 2 attributes
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1): # create new method add_animal
        if animal_type in self.animals: # avoid duplicate of the animal type but add it to the count
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self): # create new method get_info
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    # Bonus methods
    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = []
        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animal_list.append(f"{animal}s")
            else:
                animal_list.append(animal)

        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + f" and {animal_list[-1]}"
        else:
            animals_str = animal_list[0]

        return f"{self.name}'s farm has {animals_str}."


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_short_info())