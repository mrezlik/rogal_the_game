import time

def clear():
	hall_file = open('hall_of_fame.txt', 'w')
	hall_file.close()	


def write_result(player):
	try:
		hall_file = open('hall_of_fame.txt', 'r+')
	except FileNotFoundError:
		hall_file = open('hall_of_fame.txt', 'w')
		hall_file.close()
		hall_file = open('hall_of_fame.txt', 'r+')
	lines = hall_file.readlines()
	result = '# Name: ' + player.name + ' | Specialisation: ' + player.specialisation + ' | Experience gained: ' + str(player.exp) + ' points | Level: ' + str(player.level) + ' | Monsters slain: ' + str(player.enemies_killed) + ' | Time: ' + str(round(time.time() - player.start_time , 2)) + ' seconds\n'
	hall_file.write(result)
	hall_file.close()
	
	
def print_hall():
	try:
		hall_file = open('hall_of_fame.txt', 'r')
	except FileNotFoundError:
		print('No hall of fame file found!')
		quit()
	lines = hall_file.readlines()
	hall_file.close()
	for x in lines:
		print(x, end="")
		
