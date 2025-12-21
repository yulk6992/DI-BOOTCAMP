# W1D1 XP GOLD

# Exercise 1: What Is The Season?

# Ask the user to input a month (1 to 12).
# Display the season of the month received:
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input("Enter a month number (1 to 12): "))

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month")

# Exercice 2: 

# Write a for loop to print all numbers from 1 to 20, inclusive.
for i in range(1, 21):
    print(i)

# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercice 3: 

# Write a while loop that keeps asking the user to enter their name.

name = ""

while name != "Claude":
    name = input("Enter my name: ")

print("Correct! Loop stopped.")

# Stop the loop if the user’s input is your name.

name = ""

while name != "Claude":
    name = input("Enter my name: ")
    if name != "Claude":
        print("Wrong name, try again!")

print("Well done! You found the correct name.")


# Exercice4: 

# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    print(names.index(user_name))
else:
    print("Name not found")


# Exercice5:

n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
n3 = int(input("Input the 3rd number: "))

if n1 >= n2 and n1 >= n3:
    greatest = n1
elif n2 >= n1 and n2 >= n3:
    greatest = n2
else:
    greatest = n3

print("The greatest number is:", greatest)

# Answer more concice

n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
n3 = int(input("Input the 3rd number: "))

print("The greatest number is:", max(n1, n2, n3))


# Exercice6: 

import random

user_number = int(input("Enter a number between 1 and 9: "))
random_number = random.randint(1, 9)

if user_number == random_number:
    print("Winner")
else:
    print("Better luck next time.")

print("Random number was:", random_number)

# Bonus

import random

play = "y"

while play == "y":
    user_number = int(input("Enter a number between 1 and 9: "))
    random_number = random.randint(1, 9)

    if user_number == random_number:
        print("Winner")
    else:
        print("Better luck next time.")

    print("Random number was:", random_number)
    play = input("Do you want to play again? (y/n): ")


# Bonus2: 

import random

wins = 0
losses = 0
play = "y"

while play == "y":
    user_number = int(input("Enter a number between 1 and 9: "))
    random_number = random.randint(1, 9)

    if user_number == random_number:
        print("Winner")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

    print("Random number was:", random_number)
    play = input("Do you want to play again? (y/n): ")

print("\nGame Over")
print("Total wins:", wins)
print("Total losses:", losses)


