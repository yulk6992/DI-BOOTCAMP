##### Exercise 1: Converting Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_values = dict(zip(keys, values))
print(keys_values)

##### Exercise 2: Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total =0 # to store the final result requested at the end
cost = 0 # to store the price per family member

for name, age in family.items(): 
    if age <= 3: 
        cost = 0
    elif 3 < age >= 12: 
        cost = 10
    else: 
        cost = 15
    print(f"the ticket price for {name} is ${cost}.")
    total += cost # to sum all the costs
    print(f"the family will have to pay ${total}.")
    

##### Exercice 3: Zara

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}


brand["number_stores"] = 2 #Change the value of number_stores to 2
print(brand.items()) # to ckeck the changes

print(f"Zara’s clients are {', '.join(brand['type_of_clothes'])}.") # Zara’s clients using type_of_clothes

brand["country_creation"] = "Spain" # Add a new key country_creation = "Spain"

# Check if international_competitors exists. If it exists, add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand.items()) # to ckeck the changes

del brand["creation_date"] # Delete the creation_date key
print(brand.items()) # to ckeck the changes

print("Last international competitor is ", brand["international_competitors"][-1]) # Print the last item in international_competitors

print("Major colors in the US:", brand["major_color"]["US"]) # Print the major colors in the US

print("Number of keys in the brand dictionary:", len(brand))  # Print the number of keys in the dictionary

print("All the keys in the Dictionary Zara are:", list(brand.keys())) # Print all keys of the dictionary


##### Exercice 4: Some Geography

# Step 1: Define the function
city_description = []
def describe_city(city, country="Unknown"):
city_description = dict{describe_city}

# Step 2: Print a message
print(f"{city} is in {country}.")

# Step 3: Call the function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")

##### Exercice 5 : Random

# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.


# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.


# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100. 



##### Exercice 6 : Let’s Create Some Personalized Shirts !

# Step 1 & 2: Define the function
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# Step 3: Call the function
make_shirt("large", "I love Python")

# Step 4: Modify the function with default values
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# Step 5: Call the function with default and custom values
make_shirt()                     # large shirt with default message
make_shirt("medium")             # medium shirt with default message
make_shirt("small", "Custom message")  # small shirt with a custom message

# Step 6 (Bonus): Keyword arguments
make_shirt(size="extra large", text="Code. Sleep. Repeat.")
make_shirt(text="Hello!", size="small")

##### Exercice 7: Temperature Advice

# no more time to do this one

