# Hangman Game

A classic word-guessing game implemented in Python where players try to guess a hidden word letter by letter before running out of attempts.

## Features

- **ASCII Art Visualization**: Visual representation of the hangman that updates with each wrong guess
- **35+ Word Dictionary**: Tech-themed words related to programming and computers
- **User-Friendly Interface**: Clear display of game state, guessed letters, and remaining attempts
- **Input Validation**: Handles invalid inputs gracefully
- **Replay Option**: Play multiple rounds without restarting the program

## How to Play

1. The game randomly selects a word from its dictionary
2. You see blank spaces representing each letter in the word
3. Guess one letter at a time
4. If your guess is correct, the letter appears in its position(s)
5. If your guess is wrong, a part of the hangman is drawn
6. You have 6 wrong guesses before the game ends
7. Win by guessing all letters before the hangman is complete!

## Requirements

- Python 3.x

## Installation

Clone this repository or download the `hangman.py` file:

```bash
git clone <repository-url>
cd Test
```

## Running the Game

Make the script executable (optional):

```bash
chmod +x hangman.py
```

Run the game:

```bash
python3 hangman.py
```

Or if you made it executable:

```bash
./hangman.py
```

## Game Controls

- **Enter a letter**: Type a single letter and press Enter to make a guess
- **Type 'quit'**: Exit the game at any time
- **Ctrl+C**: Alternative way to exit the game

## Example Gameplay

```
==================================================
🎮 WELCOME TO HANGMAN! 🎮
==================================================

Guess the word one letter at a time.
You can make up to 6 wrong guesses before the game is over.

==================================================

       ------
       |    |
       |
       |
       |
       |
    --------

==================================================

Word: _ _ _ _ _ _ _

Guessed letters: None
Wrong guesses: 0/6
==================================================

Enter a letter: e

✓ Good guess! 'E' is in the word.
```

## Word Categories

The game includes tech-themed words such as:
- Programming languages (Python, JavaScript)
- Computer science concepts (Algorithm, Database)
- Technology terms (Cloud, Server, Network)
- And more!

## Project Structure

```
.
├── hangman.py    # Main game file
└── README.md     # This file
```

## Customization

You can easily customize the game by modifying the `WORD_LIST` in `hangman.py`:

```python
WORD_LIST = [
    "your", "custom", "words", "here"
]
```

## License

This is a simple educational project - feel free to use and modify as you wish!

## Contributing

Feel free to fork this project and add your own improvements:
- Add difficulty levels
- Include hint system
- Add more word categories
- Implement multiplayer mode
- Add score tracking

Enjoy playing Hangman! 🎮
