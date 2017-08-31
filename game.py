import os
import time
from controls import getch
from map import create_board, print_board, change_player_position, colision
from introduction import print_logo, story
from battle import fight
from hall_of_fame import write_result, print_hall, clear
from character import Character, Enemy, Player
from game_inventory import print_table
from bossfight import bossfight
from winlosescreen import win, lose

def main():
	os.system('clear')
	print_logo()
	time.sleep(1)
	story()
	x = None
	while not x:
		x = getch()
	os.system('clear')
	player = Player(input('Name your hero:'))
	current_map = create_board('map_1.txt')
	player_position = (9, 44)
	inv = {"gold": ["coin", 10, 1]}
	while not(x == 'q'):
		x = None
		os.system('clear')
		print_board(current_map)
		print_table(inv)
		x = getch()
		return_from_colision = colision(player, inv, current_map, player_position[0], player_position[1], x)
		current_map = return_from_colision[0]
		inv = return_from_colision[1]
		player_position = change_player_position(current_map, player_position[0], player_position[1], x)


if __name__ == '__main__':
	main()
