from game_inventory import print_table, add_to_inventory


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
    inv = {"dagger": 100}
    print_table(inv)


def change_map(board, player_coordinate_y, player_coordinate_x, command=None, board_width=86, board_height=21):
    if command == 'w':
        if player_coordinate_y == 1:
            pass
        else:
            if board[player_coordinate_y-1][player_coordinate_x] == 'X':
                board[player_coordinate_y-1][player_coordinate_x] = 'X'
            else:
                board[player_coordinate_y - 1][player_coordinate_x] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    elif command == 'a':
        if player_coordinate_x == 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x] == 'X':
                board[player_coordinate_y][player_coordinate_x] = 'X'
            else:
                board[player_coordinate_y][player_coordinate_x] = '@'
                board[player_coordinate_y][player_coordinate_x+1] = ' '
    elif command == 's':
        if player_coordinate_y == board_height - 1:
            pass
        else:
            if board[player_coordinate_y+1][player_coordinate_x] == 'X':
                board[player_coordinate_y+1][player_coordinate_x] = 'X'
            else:
                board[player_coordinate_y + 1][player_coordinate_x] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    elif command == 'd':
        if player_coordinate_x == board_width - 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x+1] == 'X':
                board[player_coordinate_y][player_coordinate_x+1] = 'X'
            else:
                board[player_coordinate_y][player_coordinate_x+1] = '@'
                board[player_coordinate_y][player_coordinate_x] = ' '
    return board


def change_player_position(board, player_coordinate_y, player_coordinate_x, command=None, board_width=86, board_height=21):
    if command == 'w':
        if player_coordinate_y == 1:
            pass
        else:
            if board[player_coordinate_y-1][player_coordinate_x] == 'X':
                pass
            else:
                player_coordinate_y = player_coordinate_y - 1
    elif command == 'a':
        if player_coordinate_x == 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x-1] == 'X':
                pass
            else:
                player_coordinate_x = player_coordinate_x - 1
    elif command == 's':
        if player_coordinate_y == board_height - 1:
            pass
        else:
            if board[player_coordinate_y+1][player_coordinate_x] == 'X':
                pass
            else:
                player_coordinate_y = player_coordinate_y + 1
    elif command == 'd':
        if player_coordinate_x == board_width - 1:
            pass
        else:
            if board[player_coordinate_y][player_coordinate_x+1] == 'X':
                pass
            else:
                player_coordinate_x = player_coordinate_x + 1
    return (player_coordinate_y, player_coordinate_x)


def main():
    map_one = create_board()


if __name__ == '__main__':
    main()
