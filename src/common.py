def read_choice(choices: list[str]) -> str:
    choice = None

    while choice not in choices:
        choice = input("Pick one of {choices}: ".format(choices=", ".join(choices)))

    return choice


def read_integer(prompt: str) -> int | None:
    string = input(prompt)

    try:
        return int(string)
    except:
        return None
