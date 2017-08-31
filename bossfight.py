import os
import random
from hotwarmcold import game, generate_answer, check_answer, print_hint
from winlosescreen import win
from controls import getch

def bossfight(player):
	answer = generate_answer()
	guess_count = 10
	os.system('clear')
	print('You killed all enemies, their boss wants you dead, defeat him i battle of wits... Hot Warm Cold game begins!\nPress any key to continue')
	x = None
	while not x:
		x = getch()
	os.system('clear')
	with open('boss.txt', 'r') as f:
        	art = f.readlines()
	for y in art:
		for x in y:
			print(x, end="")
	print('')
	while True:
		guess_count = game(answer, guess_count)
		if guess_count == 0 or guess_count == 100:
			player.alive = False
			break
	if not guess_count == 0:
		win(player)


def main():
	bossfight()
	
	
if __name__ == '__main__':
	main()
