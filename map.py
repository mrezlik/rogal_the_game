def create_board(width, height):
	board = []
	board.append([])
	for i in range(width):
		board[0].append('X')
	for y in range(1, height - 1):
		board.append([])
		board[y].append('X')
		for x in range(1, width - 1):
			board[y].append(' ')
		board[y].append('X')
	board.append([])
	for i in range(width):
		board[height - 1].append('X')
	return board


def print_board(board):
	for y in board:
		for x in y:
			print(x, end='')
		print('')


def change_map(board, player_coordinate_y, player_coordinate_x, command = None, board_width = 80, board_height = 20):
	if command == 'w':
		if player_coordinate_y == 0:
			pass
		else:
			board[player_coordinate_y - 1][player_coordinate_x] = '@'
			board[player_coordinate_y][player_coordinate_x] = ' '
	elif command == 'a':
		if player_coordinate_x == 0:
			pass
		else:
			board[player_coordinate_y][player_coordinate_x - 1] = '@'
			board[player_coordinate_y][player_coordinate_x] = ' '
	elif command == 's':
		if player_coordinate_y == board_height - 1:
			pass
		else:
			board[player_coordinate_y + 1][player_coordinate_x] = '@'
			board[player_coordinate_y][player_coordinate_x] = ' '
	elif command == 'd':
		if player_coordinate_x == board_width - 1:
			pass
		else:
			board[player_coordinate_y][player_coordinate_x + 1] = '@'
			board[player_coordinate_y][player_coordinate_x] = ' '
	return board


def change_player_position(player_coordinate_y, player_coordinate_x, command = None, board_width = 80, board_height = 20):	
	if command == 'w':
		if player_coordinate_y == 0:
			pass
		else:
			player_coordinate_y = player_coordinate_y - 1
	elif command == 'a':
		if player_coordinate_x == 0:
			pass
		else:
			player_coordinate_x = player_coordinate_x - 1
	elif command == 's':
		if player_coordinate_y == board_height - 1:
			pass
		else:
			player_coordinate_y = player_coordinate_y + 1
	elif command == 'd':
		if player_coordinate_x == board_width - 1:
			pass
		else:
			player_coordinate_x = player_coordinate_x + 1
	return (player_coordinate_y, player_coordinate_x)


'''def main():
	width = int(input("Width: "))
	height = int(input("Height: "))
	print('')
	map_one = create_board(width, height)
	print_board(map_one)
main()'''
