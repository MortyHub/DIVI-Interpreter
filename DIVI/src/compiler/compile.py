import os

TOKENS = [
	"shell.log('", "')", "update()", "shell.stop()", "multiline()", "help('"
]
HELP = [
	'shell.log', 'Will print whatever into the console', 'update', 'Will update your shell to the latest version', 'shell.stop', 'Will exit the shell', 'multiline', 'Activates Multiline mode where you can input multiple commands and it will run those commands after typing end'
]
MULTI = []

def Mult(inc):
	for i in range(len(inc)):
		write(inc[i])


def write(INPUT):
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
				


def error(er):
	print(colored(235, 94, 94, 'Error: ' + er))

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)