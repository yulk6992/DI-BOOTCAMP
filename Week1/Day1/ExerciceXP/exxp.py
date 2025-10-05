# Exercice 1 : Hello World
for i in range(5) : 
    print('hello World')

# Exercice 2 : some Math
print(99e3*8)

# Exercice 3 : What’s Your Name ?
your_name = input ("what's your name?")
my_name = "Cath"
if your_name != my_name : 
   print("you have a funny name")

# Exercise 4 : Tall Enough To Ride A Roller Coaster
height = input ("what is your height in centimeters? ")
if height >= '145' :
    print("your are tall enough to ride")
else : 
    print("you need to grow some more to ride")

# Exercise 5 : Favorite Numbers

my_fav_numbers = {3, 11, 14}
my_fav_numbers.add(12)
my_fav_numbers.add(15)
my_fav_numbers.remove(15)

friend_fav_numbers = {15, 5, 12}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 6 : Tuple

my_tuple = (3, 11, 14)

# impossible to add any more integer as a tuple is immutable, meaning it cannot be changed. I need to create a new tuple if I want to have more integrers inside. 

# Exercice 7 : List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercice 8 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders : 
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

sandwich_orders_two = sandwich_orders[:]

finished_sandwiches = []

for sandwich in sandwich_orders_two :
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)


for sandwich in finished_sandwiches :
    print("I made your", sandwich)
