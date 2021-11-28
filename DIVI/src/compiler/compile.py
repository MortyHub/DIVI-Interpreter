TOKENS = [
	"shell.log('", "')"
]

def write(INPUT):
	for i in TOKENS:
		if i in INPUT:
			if i == TOKENS[0]:
				memory = INPUT.split("'")
				print(memory[1])