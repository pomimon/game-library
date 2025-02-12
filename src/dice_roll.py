# ask how many dice you want to roll
# ascii dice image like cow?
# use common read_integer
# reroll
# parse errors

import random
from src import common

DICE_1 = (
  "┌─────────┐\n"
  "│         │\n"
  "│    ●    │\n"
  "│         │\n"
  "└─────────┘"
)

DICE_2 = (
  "┌─────────┐\n"
  "│  ●      │\n"
  "│         │\n"
  "│      ●  │\n"
  "└─────────┘"
)

DICE_3 = (
  "┌─────────┐\n"
  "│  ●      │\n"
  "│    ●    │\n"
  "│      ●  │\n"
  "└─────────┘"
)

DICE_4 = (
  "┌─────────┐\n"
  "│  ●   ●  │\n"
  "│         │\n"
  "│  ●   ●  │\n"
  "└─────────┘"
)

DICE_5 = (
  "┌─────────┐\n"
  "│  ●   ●  │\n"
  "│    ●    │\n"
  "│  ●   ●  │\n"
  "└─────────┘"
)

DICE_6 = (
  "┌─────────┐\n"
  "│  ●   ●  │\n"
  "│  ●   ●  │\n"
  "│  ●   ●  │\n"
  "└─────────┘"
)


DICE_ART: dict[int, str] = {
  1: DICE_1,
  2: DICE_2,
  3: DICE_3,
  4: DICE_4,
  5: DICE_5,
  6: DICE_6,
}

def run_game():

  # take one - gives a set amount of dice
  # dice_face = range(1, 7)
  # first_dice = random.choice(dice_face)
  # second_dice = random.choice(dice_face)

  # print(f" your dice is {first_dice} and {second_dice}")


  # take two - asks for input on how many dice is needed
  dice  = range(1, 7)
  count = common.read_integer("Enter the number of dice you need: ")
  rolls: list[int] = []

  if count is None:
    return

  for i in range(0, count):
    rolls.append(random.choice(dice))

  print(f"Dice Rolls > {rolls}")

  for index in range(0, len(rolls)):
    print(DICE_ART[rolls[index]])
