# Welcome message from welcome.py
from welcome import welcome

# Category list from category.py
from category import RETRO_GAMES, CAR_BRANDS, FOODS, ANIMALS

# Difficulty levels from difficulty.py
from difficulty import EASY, MEDIUM, HARD


def choose_category():
    """
    Let's the user to choose word cetegory
    to play with and return their choice.
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
            if chosen_category == "1":
                category = RETRO_GAMES
                print(category)
                return category

            if chosen_category == "2":
                category = CAR_BRANDS
                print(category)
                return category

            if chosen_category == "3":
                category = FOODS
                print(category)
                return category

            if chosen_category == "4":
                category = ANIMALS
                print(category)
                return category

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
            if chosen_difficulty == "e":
                difficulty = EASY
                print(len(difficulty))
                return difficulty

            if chosen_difficulty == "m":
                difficulty = MEDIUM
                print(len(difficulty))
                return difficulty

            if chosen_difficulty == "h":
                difficulty = HARD
                print(len(difficulty))
                return difficulty

        else:
            choose_difficulty()


def main():
    """
    Run game functions
    """
    welcome()
    choose_category()
    choose_difficulty()


main()
