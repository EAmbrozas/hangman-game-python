# Modules
import random

# Welcome message from welcome.py
from welcome import welcome

# Category list from category.py
from category import RETRO_GAMES, CAR_BRANDS, FOODS, ANIMALS

# Difficulty levels from difficulty.py
from difficulty import EASY, MEDIUM, HARD


def choose_category():
    """
    Let's the user to choose word cetegory to play
    with and return a random word from their choice.
    """
    print("""
Choose category to play with from the list bellow:
[1] Retro Games
[2] Car Brands
[3] Foods
[4] Animals
""")

    while True:
        chosen_category = input("Category: ")
        if chosen_category in {"1", "2", "3", "4"}:

            global word

            if chosen_category == "1":
                category = RETRO_GAMES
                word = random.choice(category)
                return word

            if chosen_category == "2":
                category = CAR_BRANDS
                word = random.choice(category)
                return word

            if chosen_category == "3":
                category = FOODS
                word = random.choice(category)
                return word

            if chosen_category == "4":
                category = ANIMALS
                word = random.choice(category)
                return word

        else:
            choose_category()


def choose_difficulty():
    """
    Let's the user to choose difficulty level
    to play with that returns amount of game lives.
    """
    print("""
Choose difficulty level from the list bellow:
[E] Easy for 10 lives
[M] Medium for 8 lives
[H] Hard for 6 lives
""")
    while True:
        chosen_difficulty = input("Difficulty: ")
        if chosen_difficulty in {"e", "m", "h"}:

            global lives

            if chosen_difficulty == "e":
                difficulty = EASY
                lives = len(difficulty) - 1
                return lives

            if chosen_difficulty == "m":
                difficulty = MEDIUM
                lives = len(difficulty) - 1
                return lives

            if chosen_difficulty == "h":
                difficulty = HARD
                lives = len(difficulty) - 1
                return lives

        else:
            choose_difficulty()


def game():
    """
    Main game loop
    """
    # Dashes for each letter in a word
    current_guess = "_" * len(word)
    # Wrong guess counter
    wrong_guess = 0

    print(word)
    print(current_guess)
    print(lives)


def main():
    """
    Run game functions
    """
    welcome()
    choose_category()
    choose_difficulty()
    game()


main()
