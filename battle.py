from character import Character, Enemy, Player
from winlosescreen import win, lose

def fight(player, monster):

	print('You have encounter the', monster.name, 'fight is inevitable!')

	while True:

		print('Your HP:', player.current_hp)
		print('Player attack the', monster.name, 'for', player.damage, 'damage!')
		monster.hp -= player.damage

		if monster.hp <= 0:

			print('You killed the', monster.name, 'you monster!\nYou gain', monster.exp, 'experience points!\n\n\n')
			player.exp += monster.exp
			player.check_level()

			if '|' not in player.strongest_monster_killed:
				player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			else:
				if monster.exp > int(player.strongest_monster_killed[-5:]):
					player.strongest_monster_killed = monster.name + '|' + ' ' * (5 - len(str(monster.exp))) + str(monster.exp)
			
			return None

		print(monster.name, 'attack you for', monster.damage, 'damage!')
		player.current_hp -= monster.damage

		if player.current_hp <= 0:
			print(monster.name, 'killed you, u succ!\n\n\n')
			player.alive = False
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

	enemies = [rat_1, rat_2, alien_1, alien_2, robot_1]

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
