# Python Project

## Tech Stack
 - python 3.12
 - pytest
 - pylint
 - mypy
 - black
 - flake8
 - poetry

## Common Commands
- `make init`
    - build the project
- `make verify`
    - run tests
- `make run`
    - run `main.py`



Wordle Engine Kata

Let’s build an engine for the game Wordle. The engine should provide the core functionality to play the game.
Core Requirements

    Guess the Word
        The user has six attempts to guess the secret 5-letter word.

    Input Validation
        Each guess must be exactly 5 letters long.
        If the input is invalid (e.g., not 5 letters):
            Do not count it as an attempt.
            Inform the user the input is invalid.

    Feedback on Guesses
        After each guess, the engine should provide feedback for each letter:
            G (Green): Letter is correct and in the correct position.
            Y (Yellow): Letter is in the word but in the wrong position.
            - (Gray): Letter is not in the word.

    End of Game
        If the user guesses the word correctly within six attempts:
            Declare victory and end the game.
        If the user fails to guess the word after six attempts:
            Reveal the solution.

Examples of Feedback

If the secret word is PLANE:

    Guessing WORLD returns: ---Y-
    Guessing PANEL returns: GYYYY
    Guessing PLANE returns: GGGGG

Possible Enhancements

    Tracking Guesses
        Track all previous guesses and their feedback so the user can review them.

    Game Statistics
        Track and display statistics at the end of each game:
            Total number of games played.
            Win percentage.
            Current win streak.
            Longest win streak.

    Allow Custom Word Lengths
        Add support for words longer or shorter than 5 letters (e.g., 6-letter or 4-letter games).

    Hard Mode
        Introduce a stricter "hard mode" where:
            Players must use all G (Green) and Y (Yellow) letters from previous guesses in all subsequent guesses.

    Randomized Target Word
        Allow the engine to generate a random word for the target (can be a placeholder for now, such as picking a word from a pre-defined list).
