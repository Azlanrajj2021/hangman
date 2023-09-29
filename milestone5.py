
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """The code checks if the guessed letter is in the word and if so it updates variables 
        
        Args:
            guess: the guess by the user

        Returns:
            Currently returns True 
        """
        format_guess = guess.lower()
        if format_guess in self.word:
            print(f"Good guess! {format_guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == format_guess:
                    self.word_guessed[i] = format_guess
            self.num_letters -= 1
            return True
        else:
            self.num_lives -= 1
            print(f"Sorry, {format_guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
    
    def ask_for_input(self):
        """The code continously runs the loop, to keep the game going until a end statement is specified
        
        Args:
            None

        Returns:
            Currently returns nothing, a loop exist statement needs to be defined
        """
        while True:
            guess = input("Please guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                if not self.check_guess(guess):
                    break
                self.list_of_guesses.append(guess)
                
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()
            

word_list = ["banana", "mango", "orange", "pineapple", "watermellon"]

play_game(word_list)







