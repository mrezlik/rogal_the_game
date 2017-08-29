from character import Character, Enemy, Player

def fight(player, monster):
	
	print('You have encounter the', monster.name, 'fight is inevitable!')
	
	while True:
		
		print('Your HP:', player.hp)
		print('Player attack the', monster.name, 'for', player.damage, 'damage!')
		monster.hp -= player.damage
		
		if monster.hp < 1:
			
			print('You killed the', monster.name, 'you monster!\n')
			player.exp += monster.exp
			
			if '|' not in player.strongest_monster_killed:
				player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			else:
				if monster.exp > int(player.strongest_monster_killed[-5:]):
					player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			
			return player
			
		print(monster.name, 'attack you for', monster.damage, 'damage!')
		player.hp -= monster.damage
		
		if player.hp < 1:
			print(monster.name, 'killed you, u succ!\n')
			player.alive = False
			return player
			

def main():
	
	player = Player('Player', 100, 15)
	
	rat = Enemy('Mutated Rat', 20, 1, 100)
	alien = Enemy('Alien', 50, 15, 150)
	robot = Enemy('Robot', 80, 5, 200)
	star = Enemy('Death Star', 100000, 99999, 999)
	
	enemies = [rat, rat, alien, alien, robot]
		
	for encounter in enemies:
		player = fight(player, encounter)
		if not player.alive:
			print('Game Over Man!')
			print('Your strongest prey was:', player.strongest_monster_killed)
			quit()
	print('You have won The Game with', player.exp, 'experience points!')
	


if __name__ == '__main__':
    main()
