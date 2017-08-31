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
    import random
    from game_inventory import add_to_inventory
    
    loots = [["Lightsaber", "weapon", 10, 1], ["Shield", "deffence item", 10, 1], ["First aid kit", "medicine", 4, 1]]
    loot = random.randint(0, len(loots)-1)
    return add_to_inventory(inv, loots[loot]), loots[loot][0]



