import os
from controls import getch
from map import create_board, print_board
from introduction import print_logo
import time

def main():
	print_logo()
	time.sleep(3)
	map_one = create_board(80, 20)
	x = None
	while not(x == 'q'):
		os.system('clear')
		print_board(map_one)
		x = getch()
		print(x)

if __name__ == '__main__':
    main()
