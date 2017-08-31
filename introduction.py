def print_logo():
	logo = ["""
	███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ ██╗     ██╗██╗  ██╗███████╗
	██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗██║     ██║██║ ██╔╝██╔════╝
	███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝██║     ██║█████╔╝ █████╗
	╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗██║     ██║██╔═██╗ ██╔══╝
	███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║███████╗██║██║  ██╗███████╗
	╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
	"""]
	print(*logo)


def story():
	print("""It is the year 2100. Poland has become a world power.
	Out of distant planets there are strange messages about the
	presence of non-human civilization. We, as the best Polish citizen, are setting out on a
	"peaceful" mission to solve these problems. With the development of the situation,
	you notice that something is wrong. The alien are fighting very fiercely and
	apparently guarding something ... Is this the end of the present world coming?
	You need to find out what's going on and save the earth at all costs.
	Press any key to continue""")

def about():
	print(""" Hello in our game. Stellarlike was created by Marcin Stochlik and Marek Szewczyk. Use WSAD
	to move you character (@). To open inventory press "i", to continue press "c". If you want to quit just
	press "q".
	"#" are the items which you can take!
	"%" are your enemies. You must kill all of them to go on the next level
	"X" are a wall
	You are a "@" character

	Press c to continue! """)
