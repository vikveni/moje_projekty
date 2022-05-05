

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Viktor Veniger
email: viktorveniger@gmail.com
discord: VikVeni#8755
"""
import random
secret_number = []
guess_count = 0
separator = "-" * 47


def introduction():
    print("Hi there!",
          separator,
          "I've generated a random 4 digit number for you. ",
          "Let's play a bulls and cows game.",
          separator,
          sep= "\n"
          )


def random_secret_number():
    for i in range(4):
        number = random.randrange(0,9)
        secret_number.append(number)
    if len(secret_number) > len(set(secret_number)) or secret_number[0] == 0:
        secret_number.clear()
        random_secret_number()

def wrong_choice(choice):
    if choice.isalpha() or choice[0] == 0 or choice[::] == choice[::]:
        print("Wrong input!")

def bulls_cows():
    global choice
    bulls = 0
    cows = 0
    choice = input("Enter a number: ")
    if choice.isalpha() or choice[0] == 0 or len(choice) != 4:
        print("Wrong input! It can not be letters, starts with 0, duplicity numbers or longer than 4.")
        quit()
    guess = []
    for i in range(4):
        guess.append(int(choice[i]))
        for x in range(4):
            if guess[i] == secret_number[x]:
                cows += 1
    for z in range(4):
        if guess[z] == secret_number[z]:
            bulls += 1
    print(f"{bulls} bulls, {cows} cows")
    print(f"{guess}, {secret_number}")
    print(separator)
    bulls_cows()

    if guess == secret_number:
        print(f"Congratualtions you are the winner, the number was {secret_number}")


def game_player():
    introduction()
    random_secret_number()
    bulls_cows()
game_player()


