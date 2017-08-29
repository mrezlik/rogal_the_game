def fight(player = {'HP': 100, 'Damage': 15, 'Monsters killed': ''}, monster = {'HP': 50, 'Damage': 15, 'Name': 'Alien'}):
	print('You have encounter the', monster['Name'], ' fight is inevitable!')
	while True:
		print('Player attack the', monster['Name'], 'for', player['Damage'], 'damage!')
		monster['HP'] -= player['Damage']
		if monster['HP'] < 1:
			print('You killed the', monster['Name'], 'you monster!')
			player['Monsters killed'] += monster['Name']
			return player
		print(monster['Name'], 'attack you for', monster['Damage'], 'damage!')
		player['HP'] -= monster['Damage']
		if player['HP'] < 1:
			print(monster['Name'], 'killed you, you succ!')
			return None
			

def main():
	player = {'HP': 100, 'Damage': 15, 'Monsters killed': ''}
	
	mutated_rat_enemy = {'HP': 20, 'Damage': 1, 'Name': 'Mutated rat'}
	alien_enemy = {'HP': 50, 'Damage': 15, 'Name': 'Alien'}
	robot_enemy = {'HP': 80, 'Damage': 5, 'Name': 'Robot'}
	death_star_enemy = {'HP': 100000, 'Damage': 99999, 'Name': 'Death Star'}
	
	enemies = [mutated_rat_enemy, alien_enemy, robot_enemy, death_star_enemy]
		
	for encounter in enemies:
		print('Your HP:', player['HP'])
		player = fight(player, encounter)
		if not player:
			print('Game Over Man!')
			quit()
	print("You've won The Game!")


if __name__ == '__main__':
    main()
