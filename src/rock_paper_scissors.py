import random


def read_choice(choices: list[str]) -> str:
    choice = None

    while choice not in choices:
        choice = input("Pick one of {choices}: ".format(choices=", ".join(choices)))

    return choice


def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("it's a tie")
    elif user_choice == "rock" and comp_choice == "paper":
        print("you lose, paper cover's rock")
    elif user_choice == "paper" and comp_choice == "rock":
        print("you won! paper cover's rock")

    elif user_choice == "scissors" and comp_choice == "paper":
        print("you won! scissors cut's paper")
    elif user_choice == "paper" and comp_choice == "scissors":
        print("you lose, scissors cut's paper")

    elif user_choice == "rock" and comp_choice == "scissors":
        print("you won! rock smashes scissors")
    elif user_choice == "scissors" and comp_choice == "rock":
        print("you lose! rock smashes scissors")


def run_game():
    print("Let's play rock, paper, scissors")

    options = ["rock", "paper", "scissors"]

    user_choice = read_choice(options)
    comp_choice = random.choice(options)

    print(f"you chose {user_choice}, computer chose {comp_choice}")

    determine_winner(user_choice, comp_choice)
