#!/usr/bin/env python3
"""
Hangman Game
A classic word guessing game where players try to guess a word letter by letter.
"""

import random
import sys

# Hangman ASCII art stages
HANGMAN_STAGES = [
    # Stage 0 - Initial
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    # Stage 1 - Head
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    # Stage 2 - Body
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    # Stage 3 - Left arm
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    # Stage 4 - Right arm
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    # Stage 5 - Left leg
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    # Stage 6 - Right leg (Game Over)
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Word list
WORD_LIST = [
    "python", "javascript", "programming", "computer", "algorithm",
    "function", "variable", "database", "software", "hardware",
    "network", "security", "developer", "debugging", "interface",
    "keyboard", "monitor", "internet", "browser", "application",
    "technology", "innovation", "digital", "artificial", "intelligence",
    "machine", "learning", "cloud", "server", "client",
    "framework", "library", "repository", "version", "control"
]

class HangmanGame:
    """Main Hangman game class"""

    def __init__(self):
        self.word = random.choice(WORD_LIST).upper()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = len(HANGMAN_STAGES) - 1

    def display_game_state(self):
        """Display the current state of the game"""
        print("\n" + "="*50)
        print(HANGMAN_STAGES[self.wrong_guesses])
        print("="*50)

        # Display the word with guessed letters
        display_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word}")
        print(f"\nGuessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        print("="*50)

    def is_word_guessed(self):
        """Check if the entire word has been guessed"""
        return all(letter in self.guessed_letters for letter in self.word)

    def is_game_over(self):
        """Check if the game is over (won or lost)"""
        return self.is_word_guessed() or self.wrong_guesses >= self.max_wrong_guesses

    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.upper()

        if letter in self.guessed_letters:
            print(f"\n⚠️  You already guessed '{letter}'. Try a different letter.")
            return False

        self.guessed_letters.add(letter)

        if letter in self.word:
            print(f"\n✓ Good guess! '{letter}' is in the word.")
            return True
        else:
            self.wrong_guesses += 1
            print(f"\n✗ Sorry! '{letter}' is not in the word.")
            return False

    def play(self):
        """Main game loop"""
        print("\n" + "="*50)
        print("🎮 WELCOME TO HANGMAN! 🎮")
        print("="*50)
        print("\nGuess the word one letter at a time.")
        print("You can make up to 6 wrong guesses before the game is over.")
        print("\nType 'quit' to exit the game at any time.\n")

        while not self.is_game_over():
            self.display_game_state()

            guess = input("\nEnter a letter: ").strip()

            if guess.lower() == 'quit':
                print("\n👋 Thanks for playing! Goodbye!")
                sys.exit(0)

            if len(guess) != 1 or not guess.isalpha():
                print("\n⚠️  Please enter a single letter.")
                continue

            self.make_guess(guess)

        # Game over - display final state
        self.display_game_state()

        if self.is_word_guessed():
            print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"The word was: {self.word}")
        else:
            print("\n💀 GAME OVER! YOU LOST! 💀")
            print(f"The word was: {self.word}")

        print("\n" + "="*50)

def main():
    """Main entry point for the game"""
    while True:
        game = HangmanGame()
        game.play()

        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
        sys.exit(0)
