import os
import random
from hotwarmcold import game, generate_answer, check_answer, print_hint

def main():
	answer = generate_answer()
	guess_count = 10
	os.system('clear')
	print('')
	with open('boss.txt', 'r') as f:
        	art = f.readlines()
	for y in art:
		for x in y:
			print(x, end="")
	print('')
	while True:
		guess_count = game(answer, guess_count)
		if guess_count == 0:
			break

if __name__ == '__main__':
	main()
