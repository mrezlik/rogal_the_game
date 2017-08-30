import os
import time
from controls import getch
from map import create_board, print_board, change_player_position, colision
from introduction import print_logo, story
from battle import fight
from hall_of_fame import write_result, print_hall
from character import Character, Enemy, Player
from game_inventory import print_table


def main():
    os.system('clear')
    print_logo()
    time.sleep(0)
    story()
    time.sleep(0)
    map_one = create_board()
    player_position = (9, 44)
    x = None
    inventory = {"Gold": 0}
    while not(x == 'q'):
        x = None
        os.system('clear')
        print_board(map_one)
        print_table(inventory)
        x = getch()
        map_one = colision(map_one, player_position[0], player_position[1], x)
        player_position = change_player_position(map_one, player_position[0], player_position[1], x)


if __name__ == '__main__':
	main()
