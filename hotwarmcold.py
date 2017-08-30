import random

def generate_answer():
	answer = []
	for x in range(3):
		while True:
			number = random.randint(0,9)
			if number not in answer:
				break
		answer.append(number)
	return answer


def check_answer(answer,guess):
	hint = []
	for x in range(3):
		if answer[x] == int(guess[x]):
			hint.insert(0, "hot")
		elif int(guess[x]) in answer:
			hint.append("warm")
	if len(hint) == 0:
		hint.append("cold")
	return hint


def print_hint(hint):
	for x in hint:
		if x == "cold":
			print('\033[94m' + "cold")
		elif x == "warm":
			print('\033[93m' + "warm")
		else:
			print('\033[91m' + "hot")
	print('\033[00m', end='')


def main():
	answer = generate_answer()
	guess_count = 10
	while True:
		
		print(answer, guess_count)
		guess = input("What is the number?")
		hint = check_answer(answer, guess)
		print_hint(hint)
		
		if hint == ["hot", "hot", "hot"]:
			print("good job")
			break
		
		guess_count -= 1
		if guess_count == 0:
			print("loser!")
			print(round(end_time, 2))
			break
		
	
if __name__ == '__main__':
	main()
