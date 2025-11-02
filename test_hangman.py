#!/usr/bin/env python3
"""
Simple tests for the Hangman game
"""

import sys
from hangman import HangmanGame, HANGMAN_STAGES, WORD_LIST

def test_game_initialization():
    """Test that game initializes correctly"""
    game = HangmanGame()
    assert game.word in [w.upper() for w in WORD_LIST]
    assert game.wrong_guesses == 0
    assert len(game.guessed_letters) == 0
    print("✓ Game initialization test passed")

def test_correct_guess():
    """Test making a correct guess"""
    game = HangmanGame()
    # Get first letter of the word
    correct_letter = game.word[0]
    initial_wrong = game.wrong_guesses

    game.make_guess(correct_letter)

    assert correct_letter in game.guessed_letters
    assert game.wrong_guesses == initial_wrong  # Should not increase
    print("✓ Correct guess test passed")

def test_wrong_guess():
    """Test making a wrong guess"""
    game = HangmanGame()
    # Find a letter not in the word
    wrong_letter = None
    for letter in "ZQXJ":
        if letter not in game.word:
            wrong_letter = letter
            break

    if wrong_letter:
        initial_wrong = game.wrong_guesses
        game.make_guess(wrong_letter)

        assert wrong_letter in game.guessed_letters
        assert game.wrong_guesses == initial_wrong + 1
        print("✓ Wrong guess test passed")
    else:
        print("⊘ Wrong guess test skipped (couldn't find wrong letter)")

def test_duplicate_guess():
    """Test guessing the same letter twice"""
    game = HangmanGame()
    letter = game.word[0]

    game.make_guess(letter)
    initial_guessed = len(game.guessed_letters)
    initial_wrong = game.wrong_guesses

    game.make_guess(letter)  # Guess again

    assert len(game.guessed_letters) == initial_guessed
    assert game.wrong_guesses == initial_wrong
    print("✓ Duplicate guess test passed")

def test_word_guessed():
    """Test word completion detection"""
    game = HangmanGame()

    # Add all letters of the word to guessed letters
    for letter in game.word:
        game.guessed_letters.add(letter)

    assert game.is_word_guessed() == True
    print("✓ Word completion test passed")

def test_game_over_win():
    """Test winning condition"""
    game = HangmanGame()

    # Guess all letters in the word
    for letter in set(game.word):
        game.guessed_letters.add(letter)

    assert game.is_game_over() == True
    assert game.is_word_guessed() == True
    print("✓ Win condition test passed")

def test_game_over_lose():
    """Test losing condition"""
    game = HangmanGame()
    game.wrong_guesses = game.max_wrong_guesses

    assert game.is_game_over() == True
    print("✓ Lose condition test passed")

def test_hangman_stages():
    """Test that hangman stages are defined"""
    assert len(HANGMAN_STAGES) == 7
    assert all(isinstance(stage, str) for stage in HANGMAN_STAGES)
    print("✓ Hangman stages test passed")

def test_word_list():
    """Test that word list exists and has words"""
    assert len(WORD_LIST) > 0
    assert all(isinstance(word, str) for word in WORD_LIST)
    assert all(len(word) > 0 for word in WORD_LIST)
    print("✓ Word list test passed")

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Hangman Game Tests")
    print("="*50 + "\n")

    tests = [
        test_game_initialization,
        test_correct_guess,
        test_wrong_guess,
        test_duplicate_guess,
        test_word_guessed,
        test_game_over_win,
        test_game_over_lose,
        test_hangman_stages,
        test_word_list,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1

    print("\n" + "="*50)
    print(f"Tests completed: {passed} passed, {failed} failed")
    print("="*50 + "\n")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
