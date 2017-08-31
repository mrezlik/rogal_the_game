import os
from character import Character, Enemy, Player
from winlosescreen import win, lose
from controls import getch

def fight(player, y, x, inv):
	
	os.system('clear')
	
	if [y, x] == [12, 7]:
		monster = Enemy('Mutated Rat', 20, 1, 100)
	elif [y, x] == [1, 27]:
		monster = Enemy('Mutated Rat', 20, 1, 100)
	elif [y, x] == [4, 64]:
		monster = Enemy('Mutated Rat', 20, 1, 100)
	elif [y, x] == [8, 13]:
		monster = Enemy('Robot', 80, 5, 200)
	elif [y, x] == [8, 56]:
		monster = Enemy('Robot', 80, 5, 200)
	elif [y, x] == [4, 67]:
		monster = Enemy('Robot', 80, 5, 200)
	elif [y, x] == [1, 23]:
		monster = Enemy('Robot', 80, 5, 200)
	else:
		monster = Enemy('Alien', 50, 15, 150)
	
	print(player.name, 'have encounter the', monster.name, end='')
	print(', fight is inevitable!')
	
	for key in inv.items():
		if not key[0] == 'First aid kit' :
			player.use_item(key[0])
		
	char = None
	player.sneak_attack(monster)
	if monster.hp <= 0:
		print(player.name, 'killed the', monster.name, end='')
		print('!')
		player.bio_heal()
		print('Your HP:', player.current_hp)
		print(player.name, 'gain', monster.exp, 'experience points!\n\n\n')
		player.enemies_killed += 1
		player.exp += monster.exp
		player.check_level()
		if '|' not in player.strongest_monster_killed:
			player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
		else:
			if monster.exp > int(player.strongest_monster_killed[-5:]):
				player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
		
		for key in inv.items():
			player.unequip_item(key[0])
				
		print('\n\n\nFight is over, for now...')
		print('Press c to continue')
		char = None
		while not char == 'c':
			char = getch()
		return None
	turn_counter = 0
	while True:
		
		turn_counter += 1
		print('\nTurn', turn_counter, 'Your HP:', player.current_hp)
		print(player.name, 'attack the', monster.name, 'for', player.damage, 'damage!')
		monster.hp -= player.damage

		if monster.hp <= 0:
			print(player.name, 'killed the', monster.name, end='')
			print('!')
			player.bio_heal()
			print('Your HP:', player.current_hp)
			print(player.name, 'gain', monster.exp, 'experience points!\n\n\n')
			player.enemies_killed += 1
			player.exp += monster.exp
			player.check_level()
			if '|' not in player.strongest_monster_killed:
				player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			else:
				if monster.exp > int(player.strongest_monster_killed[-5:]):
					player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			for key in inv.items():
				player.unequip_item(key)
			print('\n\n\nFight is over, for now...')
			print('Press c to continue')
			while not char == 'c':
				char = getch()
			
			return None
		
		print(monster.name, 'attack', player.name, 'for', monster.damage, 'damage!')
		player.current_hp -= monster.damage

		if player.current_hp <= 0:
			print(monster.name, 'killed', player.name, 'U succ!\n\n\n')
			print('Press c to continue')
			player.alive = False
			while not char == 'c':
				char = getch()
			return None


def main():

	player = Player('Stefan')

	rat_1 = Enemy('Mutated Rat', 20, 1, 100)
	rat_2 = Enemy('Mutated Rat', 20, 1, 100)
	rat_3 = Enemy('Mutated Rat', 20, 1, 100)
	rat_4 = Enemy('Mutated Rat', 20, 1, 100)
	rat_5 = Enemy('Mutated Rat', 20, 1, 100)
	alien_1 = Enemy('Alien', 50, 15, 150)
	alien_2 = Enemy('Alien', 50, 15, 150)
	alien_3 = Enemy('Alien', 50, 15, 150)
	robot_1 = Enemy('Robot', 80, 5, 200)
	robot_2 = Enemy('Robot', 80, 5, 200)
	robot_3 = Enemy('Robot', 80, 5, 200)
	star = Enemy('Death Star', 100000, 99999, 999)

	enemies = [rat_1, rat_2, alien_1, alien_2, robot_1, star]

	for encounter in enemies:
		fight(player, encounter)
		if not player.alive:
			lose()
			print('Game Over Man!')
			print('Your strongest prey was:', player.strongest_monster_killed)
			quit()
	win()
	print('You have won The Game with', player.exp, 'experience points!')



if __name__ == '__main__':
	main()
