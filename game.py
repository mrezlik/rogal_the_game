from controls import getch

def main():
	x = None
	while not(x == 'q'):
		x = getch()
		print(x)

if __name__ == '__main__':
    main()
