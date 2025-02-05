# ask how many dice you want to roll
# ascii dice image like cow?
# use common read_integer
# reroll
# parse errors

import random
from src import common

def run_game():

  # take one - gives a set amount of dice
  # dice_face = range(1, 7)
  # first_dice = random.choice(dice_face)
  # second_dice = random.choice(dice_face)

  # print(f" your dice is {first_dice} and {second_dice}")


  # take two - asks for input on how many dice is needed
  dice  = range(1, 7)
  count = common.read_integer("Enter the number of dice you need: ")
  rolls = []

  for i in range(count):
    rolls.append(random.choice(dice))

  print(f"Dice Rolls > {rolls}")



