import random
from game_inventory import print_table, add_to_inventory
from battle import fight


def create_board(name):
    with open(name, 'r') as f:
        board = f.readlines()
    print(board)
    mapa = []
    for height in range(len(board)):
        mapa.append([])
        for width in range(len(board[height])-1):
            mapa[height].append(board[height][width])
    return mapa


def print_board(board):
    for y in board:
        for x in y:
            print(x, end="")
        print("")


def take_item(inv):
    loots = [["Lightsaber", "weapon", 10, 1], ["Shield", "deffence item", 10, 1], ["First aid kit", "medicine", 4, 1]]
    loot = random.randint(0, len(loots)-1)
    return add_to_inventory(inv, loots[loot])


def colision(player, inv, board, command=None, board_width=86, board_height=21):
	if command == 'w':
		if player.coordinate_y == 1:
			pass
		else:
			if board[player.coordinate_y - 1][player.coordinate_x] == 'X':
				pass
			elif board[player.coordinate_y - 1][player.coordinate_x] == '#':
				inv = take_item(inv)
				board[player.coordinate_y -1][player.coordinate_x] = ' '
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
				inv = take_item(inv)
				board[player.coordinate_y][player.coordinate_x - 1] = ' '
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
				inv = take_item(inv)
				board[player.coordinate_y + 1][player.coordinate_x] = ' '
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
				inv = take_item(inv)
				board[player.coordinate_y][player.coordinate_x + 1] = ' '
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
	return board, inv

