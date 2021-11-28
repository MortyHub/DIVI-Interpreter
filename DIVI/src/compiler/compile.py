import os

TOKENS = [
	"shell.log('", "')", "update()", "shell.stop()"
]

def write(INPUT):
	for i in TOKENS:
		if i in INPUT:
			if i == TOKENS[0]:
				memory = INPUT.split("'")
				print(memory[1])
			elif i == TOKENS[2]:
				print('Will only work with git installed:\nWindows: https://gitforwindows.org\nMac: $ brew install git in Command Line\nLinux: sudo apt-get install git In Shell')
				os.system('git clone https://github.com/MortyHub/DIVI-Interpreter')
			elif i == TOKENS[3]:
				exit()
