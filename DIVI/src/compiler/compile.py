import os
import random
TOKENS = [
	"shell.log('", "')", "update()", "shell.stop()", "multiline()", "help('", "shell.tok('", ".setTok('", "shell.thru(", "shell.log(", "shell.create('", '.setShell()', "shell.current()"
]
HELP = [
	'shell.log', 'Will print whatever into the console', 'update', 'Will update your shell to the latest version', 'shell.stop', 'Will exit the shell', 'multiline', 'Activates Multiline mode where you can input multiple commands and it will run those commands after typing end', 'shell.tok()', 'finds Token of defined shell', '.setTok()', 'Sets token of choice', 'shell.thru', 'random function seperated by ,', 'shell.create', 'creates a Virtual shell, good for running virtual machines', 'shell', 'a virtual runtime ran by the software, multiple can be ran at once', 'shell.current', 'Shows current shell'
]

LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SHELLS = ['main']
SHELL_TOK = ['MJQPrcbjignpZdQ']
global CURRENTSH
MULTI = []
VARIABLES = []
shell = 'main'
def Mult(inc):
	for i in range(len(inc)):
		write(inc[i])


def write(INPUT):
	global shell
	for i in TOKENS:
		if i in INPUT:

			if i == TOKENS[0]:
				memory = INPUT.split("'")
				print(memory[1])

			elif i == TOKENS[2]:
				print('Will only work with git installed:\n\nWindows: https://gitforwindows.org\n\nMac: $ brew install git in Command Line\n\nLinux: sudo apt-get install git In Shell\n')
				os.system('git clone https://github.com/MortyHub/DIVI-Interpreter')

			elif i == TOKENS[3]:
				exit()

			elif i == TOKENS[4]:
				print("Type: end, to end the the script")
				line = 1
				y = True
				while y == True:
					inpu = input(str(line) + ' >> ')
					line += 1
					if inpu == 'end':
						y = False
						Mult(MULTI)
					else:
						MULTI.append(inpu)

			elif i == TOKENS[5]:
				hel = INPUT.split("'")
				curr = 0
				for x in HELP:
					curr += 1
					if x == hel[1]:
						print(HELP[curr])

			elif i == TOKENS[6]:
					shel = INPUT.split("'")
					curre = 0
					for y in SHELLS:
						if y == shel[1]:
							print(SHELL_TOK[curre])
						curre += 1

			elif i == TOKENS[7]:
				inputy = INPUT.split("'")
				y = inputy[0].split('.')
				if y[0] in SHELLS:
					setb = SHELLS.index(y[0])
					SHELL_TOK[setb] = inputy[1]

			elif i == TOKENS[8]:
				inpr = INPUT.split("(")
				imp = inpr[1].split(")")
				ike = imp[0].split(",")
				print(random.randrange(int(ike[0]), int(ike[1])))
			elif i == TOKENS[10]:
				n = INPUT.split('shell.create(')
				q = n[1].split(')')
				jojo = q[0].split(',')
				moomoo = jojo[0].split("'")
				mooooo = jojo[1].split("'")
				SHELLS.append(moomoo[1])
				SHELL_TOK.append(mooooo[1])
			elif i == TOKENS[11]:
				ff = INPUT.split(".setShell()")
				shell = ff[0]
			elif i == TOKENS[12]:
				print(shell)

				
				
				



	
