from art import logo
from game_data import data
from random import randint


def get_random():
    number = randint(0, len(data) - 1)
    first_element = data[number]

    return print(
        f" Name:  {first_element['name']}  description: {first_element['description']}  country: {first_element['country']}  ")


def game():
    print(logo)


if __name__ == "__main__":
    game()
    get_random()
