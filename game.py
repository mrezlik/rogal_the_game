import os
import time
from controls import getch, movement
from map import create_board, print_board
from introduction import print_logo, story, about, help_controls
from battle import fight
from hall_of_fame import write_result, print_hall, clear
from character import Character, Enemy, Player
from game_inventory import print_table
from bossfight import bossfight
from winlosescreen import win, lose

def new_game():
	story()
	x = None
	while not x:
		x = getch()
	os.system('clear')
	player = Player(input('Name your hero:'))
	current_map = create_board('map_1.txt')
	inv = {}
	feedback = ''
	while not(x == 'q'):
		if not player.alive:
			lose(player)
		x = None
		os.system('clear')
		print_board(current_map)
		print(feedback)
		x = getch()
		movement_return = movement(player, inv, current_map, x)
		if x == "i":
			print_table(inv)
			x = None
			while not x:
				x = getch()
		if x == "h":
			help_controls()
			x = None
			while not x == 'c':
				x = getch()
		if x == "m":
			if 'First aid kit' in inv:
				player.use_item('First aid kit')
			else:
				print('You do not own the first aid kit')
			x = None
			while not x == 'c':
				x = getch()
		current_map = movement_return[0]
		inv = movement_return[1]
		feedback = movement_return[2]


def main():
	os.system('clear')
	print_logo()
	x = None
	about()
	while not x == '1' and not x == '2':
		x = getch()
	if x == '1':
		new_game()
	elif x == '2':
		os.system('clear')
		print_hall()
		quit()


if __name__ == '__main__':
	main()
