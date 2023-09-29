import random

# Step 1:
# Create a list containing the names of your 5 favorite fruits.
# Step 2:
# Assign this list to a variable called word_list.
# Step 3:
# Print out the newly created list to the standard output (screen).
word_list = ["banana", "mango", "orange", "pineapple", "watermellon"]
print(word_list)

# Step 1:
# Go to the first line of your file.
# Step 2:
# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
# Step 3:
# Create the random.choice method and pass the word_list variable into the choice method.
# Step 4:
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)
# Step 5:
# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

# In this task, you are required to take user input. As you now know, the print() function in Python displays output on the screen. Conversely, Python has an input() function that takes input from the screen. Note that the input function returns the user input in form of a string.
# Step 1:
# Using the input function, ask the user to enter a single letter.
# Step 2:
# Assign the input to a variable called guess.

guess = input("Please type a single letter of your choice: ")

# Usually, when taking input from users, it is best to validate that the input makes sense.
# For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are provided by the user.
# To do this, create conditional checks that must be passed before the input can be accepted.
# Step 1:
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
# Step 2:
# In the body of the if statement, print a message that says "Good guess!".
# Step 3:
# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# Add documentation to your GitHub README file. You can refer to the relevant lesson in the prerequisites for this task for more information.
# At minimum, your README file should contain the following information:
# Project Title
# Table of Contents, if the README file is long
# A description of the project: what it does, the aim of the project, and what you learned
# Installation instructions
# Usage instructions
# File structure of the project
# License information
# You don't have to write all of this at once, but make sure to update your README file as you go along, so that you don't forget to add anything.