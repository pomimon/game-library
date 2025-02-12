import os
import random

PARENT_DIR = os.path.dirname(__file__)
ASSET_PATH = os.path.join(PARENT_DIR, "pokemon")
IMAGE_PATH = os.path.join(ASSET_PATH, "art")
NAMES_PATH = os.path.join(ASSET_PATH, "names.txt")

IMAGE_SET: dict[str, str] = {}
NAMES: list[str] = []

MAX_ATTEMPTS: int = 3

def preload_assets():
  for file_name in os.listdir(IMAGE_PATH):
    file_path = os.path.join(IMAGE_PATH, file_name)

    with open(file_path, "r") as file:
      IMAGE_SET[file_name] = file.read()

  with open(NAMES_PATH, "r") as file:
    for line in file:
      NAMES.append(line.strip())


def random_pokemon() -> tuple[str, str]:
  keys = list(IMAGE_SET.keys())
  key  = random.choice(keys)

  pokemon_image = IMAGE_SET[key]
  pokemon_index = int(key.rstrip(".txt"))
  pokemon_name  = NAMES[pokemon_index - 1]

  return (pokemon_name, pokemon_image)


def check_user_guess(name: str, max_attempts: int) -> bool:
  """
  Repeatedly asks the user to guess the name of the provided pokemon;
  returns a boolean indicating whether the user guessed correctly

  :param str name: The name of the pokemon
  :param int max_attempts: Maximum number of user attempts
  """
  attempts = 0

  while True:
    guess = input("Who's that Pokemon? >>  ")
    attempts += 1

    if guess.lower() == name.lower():
      return True
    elif attempts == max_attempts:
      break
    else:
      continue

  return False


def run_game():
  preload_assets()

  count = 0
  failed = None

  while True:
    (name, image) = random_pokemon()

    print(image)

    if check_user_guess(name, MAX_ATTEMPTS):
      count += 1
    else:
      failed = name
      break

  print("Sometimes you can't catch them all")
  print(f"You Guessed {count} Pokemon Correctly!")
  print(f"You Failed to Guess {failed}")

