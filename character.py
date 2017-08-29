class Character:
	
	alive = True
	
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage


class Player(Character):
	
	exp = 0
	strongest_monster_killed = 'You did not killed anything!'
	
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage


class Enemy(Character):

	def __init__(self, name, hp, damage, exp):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.exp = exp


def main():
	player = Character('Player', 100, 15)
	print(player.name, player.hp, player.damage, player.alive)
	alien = Enemy('Alien', 50, 15, 100)
	print(alien.name, alien.hp, alien.damage, alien.alive, alien.exp)
	
if __name__ == '__main__':
	main()
