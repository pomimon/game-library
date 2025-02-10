import os
import random

PARENT_DIR = os.path.dirname(__file__)
ASSET_PATH = os.path.join(PARENT_DIR, "pokemon")
IMAGE_PATH = os.path.join(ASSET_PATH, "art")
NAMES_PATH = os.path.join(ASSET_PATH, "names.txt")

IMAGE_SET = {}
NAMES = []


def preload_assets():
  for file_name in os.listdir(IMAGE_PATH):
    file_path = os.path.join(IMAGE_PATH, file_name)

    with open(file_path, "r") as file:
      IMAGE_SET[file_name] = file.read()

  with open(NAMES_PATH, "r") as file:
    for line in file:
      NAMES.append(line.strip())


def random_pokemon() -> (str, str):
  keys = list(IMAGE_SET.keys())
  key  = random.choice(keys)


  pokemon_image = IMAGE_SET[key]
  pokemon_index = int(key.rstrip(".txt"))
  pokemon_name  = NAMES[pokemon_index - 1]

  return (pokemon_name, pokemon_image)


def run_game():
  preload_assets()

  count = 0
  failed = None

  while True:
    (name, image) = random_pokemon()

    print(image)

    guess = input("Who's that Pokemon? >>  ")

    if guess.lower() != name.lower():
      failed = name
      break

    count += 1

  print(f"You Guessed {count} Pokemon Correctly!")
  print(f"You Failed to Guess {failed}")
