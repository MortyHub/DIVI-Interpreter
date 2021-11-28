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
				os.system('git clone https://github.com/MortyHub/DIVI-Interprater.git')
			elif i == TOKENS[3]:
				exit()
