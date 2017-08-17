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


'''def main():
	width = int(input("Width: "))
	height = int(input("Height: "))
	print('')
	map_one = create_board(width, height)
	print_board(map_one)
main()'''
