def fight(player = [100, 15], monster = [50, 5, 'Alien']):
	print('You have encounter the', monster[2], ' fight is inevitable!')
	while True:
		print('Player attack the', monster[2], 'for', player[1], 'damage!')
		monster[0] -= player[1]
		if monster[0] < 1:
			print('You killed the', monster[2], 'you monster!')
			return player
		print(monster[2], 'attack you for', monster[1], 'damage!')
		player[0] -= monster[1]
		if player[0] < 1:
			print(monster[2], 'killed you, you succ!')
			return None
			

def main():
	player = [100, 15]
	
	mutated_rat_enemy = [20, 1, 'Mutated rat']
	alien_enemy = [50, 15, 'Alien']
	robot_enemy = [80, 5, 'Robot']
	death_star_enemy = [100000, 99999, 'Death Star']
	
	enemies = [mutated_rat_enemy, alien_enemy, robot_enemy, death_star_enemy]
		
	for encounter in enemies:
		print('Your HP:', player[0])
		player = fight(player, encounter)
		if not player:
			print('Game Over Man!')
			quit()
	print("You've won The Game!")


if __name__ == '__main__':
    main()
