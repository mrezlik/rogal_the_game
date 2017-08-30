class Character:
	
	alive = True
	
	def __init__(self, name):
		self.name = name


class Player(Character):
	
	exp = 0
	strongest_monster_killed = 'You did not killed anything!'
	level = 1
	next_level = 100
	weapon_bonus = 1
	
	def __init__(self, name):
		self.name = name
		self.choose_specialisation()
	
	def check_level(self):
		if self.exp >= self.next_level:
			self.levelup()
			print(self.name, 'just leveled up!', self.name, 'gain', self.hp_grow, 'hitpoints and', self.damage_grow, 'damage!', self.name, end='')
			print("'s current level is", self.level,'\n\n\n')
			self.check_level()
			
	def levelup(self):
		self.level += 1
		self.next_level += (self.level) * 100
		self.max_hp += self.hp_grow
		self.current_hp += self.hp_grow
		self.damage += self.damage_grow
		
	def choose_specialisation(self):
		while True:
			choice = input('Choose your character specialisation (1, 2 or 3):\n1) Soldier: high hitpoints, low dmg, special skill: Weapon Specialist - double damage bonuses from using range weapons\n2) Adept: medium hitpoints, medium damage, special skill: Biotic Regeneration - after every combat regen 20% of max hitpoints, double regeneration from medicaments\n3) Engineer: low hitpoints, high damage, special skill: Cloaking Field - attack twice in first round of combat\n')
			if choice == '1' or choice == '2' or choice == '3':
				break
			else:
				print('Choose 1, 2 or 3!')
		if choice == '1':
			self.specialisation = 'Soldier'
			self.max_hp = 150
			self.current_hp = self.max_hp
			self.hp_grow = 38
			self.damage = 5
			self.damage_grow = 3
			self.weapon_specialist = True
			self.biotic_regeneration = False
			self.cloaking_field = False
		if choice == '2':
			self.specialisation = 'Adept'
			self.max_hp = 100
			self.current_hp = self.max_hp
			self.hp_grow = 25
			self.damage = 10
			self.damage_grow = 5
			self.weapon_specialist = False
			self.biotic_regeneration = True
			self.cloaking_field = False
		if choice == '3':
			self.specialisation = 'Engineer'
			self.max_hp = 50
			self.current_hp = self.max_hp
			self.hp_grow = 13
			self.damage = 15
			self.damage_grow = 8
			self.weapon_specialist = False
			self.biotic_regeneration = False
			self.cloaking_field = True
			
			
	def bio_heal(self):
		if self.biotic_regeneration == True:
			print(self.name, end='')
			print('s biotic powers recover back some hitpoints!')
			self.current_hp += int(self.max_hp * 0.2)
			if self.current_hp > self.max_hp:
				self.current_hp = self.max_hp
			
			
	def sneak_attack(self, monster):
		if self.cloaking_field == True:
			print('Cloaking field activated!', self.name, 'attack the', monster.name, 'for', self.damage, 'damage!')
			monster.hp -= self.damage


class Enemy(Character):

	def __init__(self, name, hp, damage, exp):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.exp = exp


def main():
	print(73 * 0.2, int(73 * 0.2))
	player = Player('Zdzisiek')
	print(player.name, player.max_hp, player.damage, player.alive, player.specialisation, player.exp, player.level, player.next_level)
	player.exp += 800
	player.check_level()
	print(player.name, player.max_hp, player.damage, player.alive, player.specialisation, player.exp, player.level, player.next_level)
	player.exp += 200
	player.check_level()
	print(player.name, player.max_hp, player.damage, player.alive, player.specialisation, player.exp, player.level, player.next_level)

	
if __name__ == '__main__':
	main()
