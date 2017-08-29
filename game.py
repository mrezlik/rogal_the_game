import os
import time
from controls import getch
from map import create_board, print_board, change_player_position, change_map
from introduction import print_logo, story
from battle import fight
from hall_of_fame import write result, print_hall

def main():
	os.system('clear')
	print_logo()
	time.sleep(3)
	story()
	time.sleep(5)
	map_one = create_board(80, 20)
	player_position = (9, 44)
	x = None
	map_one[player_position[0]][player_position[1]] = '@'
	while not(x == 'q'):
		x = None
		os.system('clear')
		print_board(map_one)
		x = getch()
		print(x)
		map_one = change_map(map_one, player_position[0], player_position[1], x)
		player_position = change_player_position(player_position[0], player_position[1], x)
		time.sleep(0.01)

if __name__ == '__main__':
    main()
