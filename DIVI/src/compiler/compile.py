import os

TOKENS = [
	"shell.log('", "')", "update()"
]

def write(INPUT):
	for i in TOKENS:
		if i in INPUT:
			if i == TOKENS[0]:
				memory = INPUT.split("'")
				print(memory[1])
			if i == TOKENS[1]:
				os.system('git clone https://github.com/MortyHub/DIVI-Interprater.git')
