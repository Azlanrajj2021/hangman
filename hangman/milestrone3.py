import random
# Write code that will continuously ask the user for a letter and validate it.
# Create a new script called milestone_3.py. This file will contain the code for this milestone.
# Step 1:
# Create a while loop and set the condition to True. Setting the condition to True` ensures that the code runs continuously.
# In the body of the loop, write the code required for the following steps.
# Step 2:
# Ask the user to guess a letter and assign this to a variable called guess.
# Step 3:
# Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
# Step 4:
# If the guess passes the checks, break out of the loop.
# Step 5:
# If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
word_list = ["banana", "mango", "orange", "pineapple", "watermellon"]

word = random.choice(word_list)

print(word)

while True:
    guess = input("Please type a single letter of your choice: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


# Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.
# For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".
# Step 1:
# Create an if statement that checks if the guess is in the word.
# Step 2:
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
# Step 3:
# Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

