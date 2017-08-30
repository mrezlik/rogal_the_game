def clear():
	hall_file = open('hall_of_fame.txt', 'w')
	hall_file.close()	


def write_result(time, exp):
	try:
		hall_file = open('hall_of_fame.txt', 'r+')
	except FileNotFoundError:
		hall_file = open('hall_of_fame.txt', 'w')
		hall_file.close()
		hall_file = open('hall_of_fame.txt', 'r+')
	lines = hall_file.readlines()

	result = "# " + str(time) + 'seconds | Experience gained:' + exp +'\n'
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
		
