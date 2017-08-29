def clear():
	hall_file = open('hall_of_fame.txt', 'w')
	hall_file.close()	


def write_result(time, monsters_killed):
	try:
		hall_file = open('hall_of_fame.txt', 'r+')
	except FileNotFoundError:
		hall_file = open('hall_of_fame.txt', 'w')
		hall_file.close()
		hall_file = open('hall_of_fame.txt', 'r+')
	lines = hall_file.readlines()

	result = "# " + str(time) + 'seconds | Monsters killed:' + monsters_killed +'\n'
	hall_file.write(result)
	hall_file.close()
	
	
def print_hall():
	try:
		hall_file = open('hall_of_fame.txt', 'r')
	except FileNotFoundError:
		hall_file = open('hall_of_fame.txt', 'w')
		hall_file.close()
		hall_file = open('hall_of_fame.txt', 'r')
	lines = hall_file.readlines()
	hall_file.close()
	for x in lines:
		print(x, end="")
	print("")
	
	
def main():
	write_result(1, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(6, 'Mutated rat Robot')
	write_result(120, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(60, 'Mutated rat Robot')
	write_result(20, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(9, 'Mutated rat Robot')
	write_result(120, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(60, 'Mutated rat Robot')
	print_hall()
	write_result(120, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(60, 'Mutated rat Robot')
	write_result(10, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(60, 'Mutated rat Robot')
	write_result(12, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(7, 'Mutated rat Robot')
	write_result(120, 'Mutated rat Mutated rat Mutated rat Mutated rat Mutated rat')
	write_result(6, 'Mutated rat Robot')
	print_hall()
	clear()

if __name__ == '__main__':
	main()
	
