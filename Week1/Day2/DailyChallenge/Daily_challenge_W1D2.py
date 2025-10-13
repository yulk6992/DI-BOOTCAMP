# Daily Challenge Week1 Day2

# Ask the user for a word

word= input("Enter a word: ")

# create an empty dictionary
letter_indexes = {}

# Loop through each letter with its index
for index, letter in enumerate(word):
    # If the letter isn't in the dictionary (avoid duplicates), add it with an empty list
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    # Append the index to the list for that letter
    letter_indexes[letter].append(index)

# Print the resulting dictionary
print(letter_indexes)


