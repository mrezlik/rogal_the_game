class Character:
	
	alive = True
	
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage


class Player(Character):
	
	exp = 0
	strongest_monster_killed = 'You did not killed anything!'
	level = 0
	next_level = 100
	
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	def check_level(self):
		if self.exp >= self.next_level:
			self.levelup()
			self.check_level()
			
	def levelup(self):
		self.level += 1
		self.next_level += (self.level + 1) * 100
		self.hp += 25
		self.damage += 5


class Enemy(Character):

	def __init__(self, name, hp, damage, exp):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.exp = exp


def main():
	player = Player('Zdzisiek', 100, 15)
	print(player.name, player.hp, player.damage, player.alive, player.exp, player.level, player.next_level)
	player.exp += 800
	player.check_level()
	print(player.name, player.hp, player.damage, player.alive, player.exp, player.level, player.next_level)
	player.exp += 200
	player.check_level()
	print(player.name, player.hp, player.damage, player.alive, player.exp, player.level, player.next_level)

	
if __name__ == '__main__':
	main()
