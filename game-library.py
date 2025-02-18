from src import common
from src import guess_the_number
from src import rock_paper_scissors
from src import dice_roll
from src import whos_that_pokemon


class Game:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __str__(self):
        return self.name

    def run(self):
        return self.func()


def get_game_info() -> list[Game]:
    return [
        Game("Rock, Paper, Scissors", rock_paper_scissors.run_game),
        Game("Guess the Number", guess_the_number.run_game),
        Game("Roll the Dice", dice_roll.run_game),
        Game("Who's that Pokemon", whos_that_pokemon.run_game),
    ]

#TODO rewrite as selectable prompt
def build_user_prompt(games: list[Game]) -> str:
    lines = []
    lines.append(f"There are {len(games)} games in the library:\n")

    for index, game in enumerate(games, 1):
        lines.append(f"  {index}) {game}")

    lines.append("\nEnter the number of the game you want to play:")
    lines.append("> ")

    return "\n".join(lines)


def get_selected_game(prompt: str, games: list[Game]) -> Game:
    while True:
        game_int = common.read_integer(prompt)

        if game_int == None:
            print("Game selection is not valid (not a number)")
        elif game_int <= 0:
            print("Game selection is not valid (too low)")
        elif game_int > len(games):
            print("Game selection is not valid (too high)")
        else:
            return games[game_int - 1]


def play_again() -> bool:
    value: str = input("Do you want to play again? (y/n) ")
    again: bool = value.lower() in ["y", "yes"]

    return again


def main():
    active = True
    games  = get_game_info()
    prompt = build_user_prompt(games)

    while active:
        game = get_selected_game(prompt, games)
        game.run()

        if not play_again():
            active = False


if __name__ == "__main__":
    main()
