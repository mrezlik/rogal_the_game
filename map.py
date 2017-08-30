from game_inventory import print_table, add_to_inventory
import random


def create_board():
    with open('map.txt', 'r') as f:
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
    loots = [{"Laser gun": ["weapon", 10, 1]}, {"Lightsaber": ["weapon", 3, 1]}, {"Shield": ["armor", 4, 1]}]
    loot = random.randint(0, len(loots)-1)
    return add_to_inventory(inv, loots[loot])


def colision(inv, board, player_coordinate_y, player_coordinate_x, command=None, board_width=86, board_height=21):
    if command == 'w':
        if player_coordinate_y == 1:
            pass
        else:
            if board[player_coordinate_y - 1][player_coordinate_x] == 'X':
                pass
            elif board[player_coordinate_y - 1][player_coordinate_x] == '#':
                inv = take_item(inv)
            else:
                board[player_coordinate_y - 1][player_coordinate_x] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    elif command == 'a':
        if player_coordinate_x == 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x - 1] == 'X':
                pass
            elif board[player_coordinate_y][player_coordinate_x - 1] == '#':
                inv = take_item(inv)
            else:
                board[player_coordinate_y][player_coordinate_x - 1] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    elif command == 's':
        if player_coordinate_y == board_height - 1:
            pass
        else:
            if board[player_coordinate_y + 1][player_coordinate_x] == 'X':
                pass
            elif board[player_coordinate_y + 1][player_coordinate_x] == '#':
                inv = take_item(inv)
            else:
                board[player_coordinate_y + 1][player_coordinate_x] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    elif command == 'd':
        if player_coordinate_x == board_width - 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x + 1] == 'X':
                pass
            elif board[player_coordinate_y][player_coordinate_x + 1] == '#':
                inv = take_item(inv)
            else:
                board[player_coordinate_y][player_coordinate_x + 1] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    return board, inv


def change_player_position(board, player_coordinate_y, player_coordinate_x, command=None, board_width=86, board_height=21):
    if command == 'w':
        if player_coordinate_y == 1:
            pass
        else:
            if board[player_coordinate_y - 1][player_coordinate_x] == 'X':
                pass
            elif board[player_coordinate_y -1][player_coordinate_x] == '#':
                 board[player_coordinate_y -1][player_coordinate_x] = ' '
            else:
                player_coordinate_y = player_coordinate_y - 1
    elif command == 'a':
        if player_coordinate_x == 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x - 1] == 'X':
                pass
            elif board[player_coordinate_y][player_coordinate_x - 1] == '#':
                 board[player_coordinate_y][player_coordinate_x - 1] = ' '
            else:
                player_coordinate_x = player_coordinate_x - 1
    elif command == 's':
        if player_coordinate_y == board_height - 1:
            pass
        else:
            if board[player_coordinate_y + 1][player_coordinate_x] == 'X':
                pass
            elif board[player_coordinate_y + 1][player_coordinate_x] == '#':
                 board[player_coordinate_y + 1][player_coordinate_x] = ' '
            else:
                player_coordinate_y = player_coordinate_y + 1
    elif command == 'd':
        if player_coordinate_x == board_width - 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x + 1] == 'X':
                pass
            elif board[player_coordinate_y][player_coordinate_x + 1] == '#':
                 board[player_coordinate_y][player_coordinate_x + 1] = ' '
            else:
                player_coordinate_x = player_coordinate_x + 1
    return (player_coordinate_y, player_coordinate_x)
