from random import randint
import sys
import os
import winlosescreen

cities = ["ANTIMATTER", "ASTEROID", "DWARF", "LODESTAR", "METEOR"]

letters_not_in_word = []
word_to_guess = []
lives = 6
selected_city = ''
player_tries = 0

def select_city():
    i = randint(0, len(cities) - 1)
    return cities[i]

def create_word_to_guess():
    global word_to_guess
    word_to_guess = []
    for i in range(0, len(selected_city)):
        word_to_guess.append("_")


def set_initial_values():
    global letters_not_in_word
    global selected_city
    global word_to_guess
    global lives
    global player_tries
    letters_not_in_word = []
    lives = 6
    selected_city = select_city()
    create_word_to_guess()
    player_tries = 0

def add_letter_to_list(letter_to_add):
    if letter_to_add not in letters_not_in_word:
        letters_not_in_word.append(letter_to_add)
        letters_not_in_word.sort()

def incorrect_guess(penalty):
    global lives
    lives -= 1
    return "Wrong answer! Muhahaha!"

def check_if_letter_is_in_word(letter):
    letter_was_in_word = False
    for i in range(0, len(selected_city)):
        if letter == selected_city[i]:
            word_to_guess[i] = letter
            letter_was_in_word = True
    return letter_was_in_word


def handle_input(player_input):
    global player_tries
    message = ""
    player_tries += 1
    if len(player_input) == 1:
        if player_input in selected_city and player_input.isalpha():
            if player_input in word_to_guess:
                message = "You already tried this letter!"
            else:
                if check_if_letter_is_in_word(player_input):
                    message = "Your guess is right!"
        else:
            message = incorrect_guess(1)
            if player_input.isalpha():
                add_letter_to_list(player_input)
    else:
        if player_input == selected_city:
            print("Oh no! You win! Fuuuuuuuuuck!")
            return False
        else:
            message = incorrect_guess(2)
    return message

def check_if_all_letters_guessed():
    if "".join(word_to_guess) == selected_city:
        print("Oh no! You win! Fuuuuuuuuuck!")
        return False

def wait_for_input():
    check_if_all_letters_guessed()
    player_input = input().upper()
    return handle_input(player_input)

def print_status(message):
    print('\033[91m' + '--------------------------------------' + '\x1b[0m')
    print("Please enter a letter, or try to guess a word!")
    print('--------------------------------------')
    print("You have {} lives left".format(lives))
    print("--------------------------------------")
    print("Letters not in word:")
    print(letters_not_in_word)
    print("--------------------------------------")
    print("Letters in word:")
    print(word_to_guess)
    print('\033[91m' + '--------------------------------------' + '\x1b[0m')
    print(message)

def start_game(player):
    print("\nI'm the big boss! I want to kil you! But I want to give you chance to win! You must guess what word I'm thinking!\n")
    set_initial_values()
    cos = True
    while cos:
        print_status("")
        while lives > 0:
            print_status(wait_for_input())
        if lives < 1:
            player.alive = False
            return None
