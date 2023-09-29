import random

# The ask_for_input function.
# Step 1:
# Define a function called ask_for_input.
# Step 2:
# Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
# Step 3:
# Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
# Step 4:
# Outside the function, call the ask_for_input function to test your code.

def check_guess(guess):
    format_guess = guess.lower()
    if len(format_guess) == 1 and format_guess.isalpha():
        print("Valid input")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    if format_guess in word:
        print(f"Good guess! {format_guess} is in the word.")
        return True
    else:
        print(f"Sorry, {format_guess} is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        guess = input("Please type a single letter of your choice: ").lower()
        if check_guess(guess):
            break
    
word_list = ["banana", "mango", "orange", "pineapple", "watermellon"]

word = random.choice(word_list)
print(word)

ask_for_input()




