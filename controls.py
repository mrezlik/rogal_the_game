def getch():
	import sys
	import termios
	import tty
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch


def movement(player, inv, board, command=None, board_width=86, board_height=21):
	import random
	from battle import fight
	from map import take_item
	
	feedback = ''
	if command == 'w':
		if player.coordinate_y == 1:
			pass
		else:
			if board[player.coordinate_y - 1][player.coordinate_x] == 'X':
				pass
			elif board[player.coordinate_y - 1][player.coordinate_x] == '#':
				result = take_item(inv)
				inv = result[0]
				board[player.coordinate_y -1][player.coordinate_x] = ' '
				feedback = 'You have picked up the ' + result[1]
			elif board[player.coordinate_y - 1][player.coordinate_x] == '%':
				fight(player, player.coordinate_y - 1, player.coordinate_x)
				if player.enemies_killed == 9:
					board = create_board('map_2.txt')
					player.coordinate_x = 64
					player.coordinate_y = 15
				board[player.coordinate_y -1][player.coordinate_x] = ' '
			else:
				board[player.coordinate_y - 1][player.coordinate_x] = '@'
				board[player.coordinate_y][player.coordinate_x] = ' '
				player.coordinate_y -= 1
	elif command == 'a':
		if player.coordinate_x == 1:
			pass
		else:
			if board[player.coordinate_y][player.coordinate_x - 1] == 'X':
				pass
			elif board[player.coordinate_y][player.coordinate_x - 1] == '#':
				result = take_item(inv)
				inv = result[0]
				board[player.coordinate_y][player.coordinate_x - 1] = ' '
				feedback = 'You have picked up the ' + result[1]
			elif board[player.coordinate_y][player.coordinate_x - 1] == '%':
				fight(player, player.coordinate_y, player.coordinate_x - 1)
				if player.enemies_killed == 9:
					board = create_board('map_2.txt')
					player.coordinate_x = 64
					player.coordinate_y = 15
				board[player.coordinate_y][player.coordinate_x - 1] = ' '
			else:
				board[player.coordinate_y][player.coordinate_x - 1] = '@'
				board[player.coordinate_y][player.coordinate_x] = ' '
				player.coordinate_x -= 1
	elif command == 's':
		if player.coordinate_y == board_height - 1:
			pass
		else:
			if board[player.coordinate_y + 1][player.coordinate_x] == 'X':
				pass
			elif board[player.coordinate_y + 1][player.coordinate_x] == '#':
				result = take_item(inv)
				inv = result[0]
				board[player.coordinate_y + 1][player.coordinate_x] = ' '
				feedback = 'You have picked up the ' + result[1]
			elif board[player.coordinate_y + 1][player.coordinate_x] == '%':
				fight(player, player.coordinate_y + 1, player.coordinate_x)
				if player.enemies_killed == 9:
					board = create_board('map_2.txt')
					player.coordinate_x = 64
					player.coordinate_y = 15
				board[player.coordinate_y + 1][player.coordinate_x] = ' '
			else:
				board[player.coordinate_y + 1][player.coordinate_x] = '@'
				board[player.coordinate_y][player.coordinate_x] = ' '
				player.coordinate_y += 1
	elif command == 'd':
		if player.coordinate_x == board_width - 1:
			pass
		else:
			if board[player.coordinate_y][player.coordinate_x + 1] == 'X':
				pass
			elif board[player.coordinate_y][player.coordinate_x + 1] == '#':
				result = take_item(inv)
				inv = result[0]
				board[player.coordinate_y][player.coordinate_x + 1] = ' '
				feedback = 'You have picked up the ' + result[1]
			elif board[player.coordinate_y][player.coordinate_x + 1] == '%':
				fight(player, player.coordinate_y, player.coordinate_x + 1)
				if player.enemies_killed == 9:
					board = create_board('map_2.txt')
					player.coordinate_x = 64
					player.coordinate_y = 15
				board[player.coordinate_y][player.coordinate_x + 1] = ' '
			else:
				board[player.coordinate_y][player.coordinate_x + 1] = '@'
				board[player.coordinate_y][player.coordinate_x] = ' '
				player.coordinate_x += 1
	return board, inv, feedback

