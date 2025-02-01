from src import common
import random

def cow(phrase: str) -> str:
    return f"""
 __________________
< {phrase} >
 ------------------
\\   ^__^
 \\  (oo)\\_______
    (__)\\       )\\/\\
        ||----w |
        ||     ||
"""

def run_game():
    print("Let's play a guessing game")

    difficulties_data: dict[str, dict[str, int | list[int]]] = {
      "easy": {
        "attempts": 10,
        "range": [1, 20],
      },
      "normal": {
        "attempts": 7,
        "range": [1, 50],
      },
      "hard": {
        "attempts": 5,
        "range": [1, 100],
      },
    }

    difficulties = list(difficulties_data.keys())

    chosen_difficulty = common.read_choice(difficulties)

    difficulty_data = difficulties_data[chosen_difficulty]

    range_start, range_end = difficulty_data["range"]

    random_number = random.randint(range_start, range_end)
    max_attempts = difficulty_data['attempts']

    print(f"Pick a number between {range_start} and {range_end} in {max_attempts} attempts")

    attempt = 0

    while True:
        user_int = common.read_integer("Enter your guess: ")

        if user_int is None:
            print("Your guess is not valid")
        elif user_int < random_number:
            print("Your guess is too low")
        elif user_int > random_number:
            print("Your guess is too high")
        else:
            print(cow("you won the game!"))
            break

        attempt += 1

        if attempt == max_attempts:
            print(cow(f"The number was {random_number} >\n< you lost, try again"))
            break
        else:
            print("You have {remaining} attempts".format(remaining=max_attempts-attempt))
