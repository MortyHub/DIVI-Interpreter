import os
import random
from DIVI.src.compiler.renderer import startHTML, render
import codecs
import time

TOKENS = [
    "shell.log('", "')", "update()", "shell.stop()", "multiline()", "help('",
    "shell.tok('", ".setTok('", "shell.thru(", "shell.log(", "shell.create('",
    '.setShell()', "shell.current()", "var.create('", ".private()",
    ".public()", "shell.publics()", "shell.privates()", "func", "({",
    "function('", "renderHTML(\"", "renderImage('", "setDefault('",
    "shell.open('", "Create.Object('", ".setSprite('", "display('",
    "ShellDat('", ".setDat('", "shell.site('", "if(", "=", ">", "<", "-", "+", "/",".request('"
]

HELP = [
    'shell.log', 'Will print whatever into the console', 'update',
    'Will update your shell to the latest version', 'shell.stop',
    'Will exit the shell', 'multiline',
    'Activates Multiline mode where you can input multiple commands and it will run those commands after typing end',
    'shell.tok()', 'finds Token of defined shell', '.setTok()',
    'Sets token of choice', 'shell.thru', 'random function seperated by ,',
    'shell.create',
    'creates a Virtual shell, good for running virtual machines', 'shell',
    'a virtual runtime ran by the software, multiple can be ran at once',
    'shell.current', 'Shows current shell', 'var.create',
    'This creates a variable ', '.public',
    'This sets a shell to be public so it can be accessed with URL or name',
    '.private',
    'This sets a shell to be public so it can only be accessed with the token',
    'func', 'a function', 'renderHTML',
    'Arguments will be rendered into a gui on screen, must be HTML',
    'shell.open',
    'This will open a divi script file of the directory of your choosings.', 'Create.Object', 'creates objects', '.setsprite', 'sets sprite of object', 'ShellDat', 'Displays the data of a shell', '.setDat', 'Sets data of shells'
]

LOWERCASE = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
UPPERCASE = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
SHELLS = ['main']
SHELL_TOK = ['MJQPrcbjignpZdQ']
PUBLIC_SHELLS = []
PRIVATE_SHELLS = ['main']
USER_FUNCTIONS = ['run']
global CURRENTSH
MULTI = []
VARIABLES = []
SHELLOPEN = []
VARIABLE_VAL = [
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', ''
]
FUNCTION_CMD = [
	'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', ''
]
shell = 'main'
DEFAULT = []
OPENED = []
OBJECTS = []
SHELLDATA = [
	'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', ''
]
OBJECT_SPRITE = [
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', ''
]

with open("default.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        DEFAULT.append(stripped_line)


def Mult(inc):
    for i in range(len(inc)):
        if inc == []:
            break
        if ('func' in inc[i]):
            OLPI = inc[i].split('func ')
            OMNIM = OLPI[0].split('(')
            if OMNIM[0] in USER_FUNCTIONS:
                for i in range(len(inc)):
                    if inc[i] == '})':
                        FUNCTION_CMD.remove(FUNCTION_CMD[0])
                        goofy = inc.index("func " + OMNIM[0] + '({')
                        goofy1 = inc.index("})") + 1
                        inc[goofy:goofy1] = []
                        Mult(FUNCTION_CMD)
                    else:
                        FUNCTION_CMD.append(inc[i])
        else:
            write(inc[i])


def write(INPUT):
    global shell
    for i in TOKENS:
        if i in INPUT:

            if i == TOKENS[0]:
                memory = INPUT.split("'")
                print(memory[1])

            elif i == TOKENS[2]:
                print(
                    'Will only work with git installed:\n\nWindows: https://gitforwindows.org\n\nMac: $ brew install git in Command Line\n\nLinux: sudo apt-get install git In Shell\n'
                )
                os.system(
                    'git clone https://github.com/MortyHub/DIVI-Interpreter')

            elif i == TOKENS[3]:
                exit()

            elif i == TOKENS[4]:
                MULTI = []
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
                open('DIVI/src/compiler/Shells/' + moomoo[1] + '.divi', "a+")
                PRIVATE_SHELLS.append(moomoo[1])

            elif i == TOKENS[11]:
                ff = INPUT.split(".setShell()")
                shell = ff[0]

            elif i == TOKENS[12]:
                print(shell)

            elif i == TOKENS[13]:
                jomo = INPUT.split("(")
                INKE = jomo[1].split(")")
                IPEK = INKE[0].split("'")
                ICT = IPEK[2].split(', ')
                VARIABLES.append(IPEK[1])
                VARIABLE_VAL.append(ICT[1])

            elif i == TOKENS[14]:
                yml = INPUT.split(".private()")
                findy = PUBLIC_SHELLS.index(yml[0])
                del PUBLIC_SHELLS[findy]
                PRIVATE_SHELLS.append(yml[0])

            elif i == TOKENS[15]:
                xml = INPUT.split(".public()")
                moocoo = PRIVATE_SHELLS.index(xml[0])
                del PRIVATE_SHELLS[moocoo]
                PUBLIC_SHELLS.append(xml[0])

            elif i == TOKENS[16]:
                print(PUBLIC_SHELLS)

            elif i == TOKENS[17]:
                print(PRIVATE_SHELLS)

            elif i == TOKENS[18]:
                funcName = INPUT.split("func ")
                FuncName1 = funcName[1].split("(")
                print("Function: '" + FuncName1[0] +
                      "' Can only be used in multiline scripts")

            elif i == TOKENS[20]:
                GOFYU = INPUT.split("'")
                USER_FUNCTIONS.append(GOFYU[1])

            elif i == TOKENS[21]:
                HTMLM = INPUT.split(",")
                ARC = HTMLM[1].split("\"")
                LMOD = HTMLM[0].split("\"")
                print(LMOD[1])
                print(ARC[1])
                startHTML('self', LMOD[1], ARC[1])

            elif i == TOKENS[24]:
                MOTIFIS = INPUT.split("'")
                with open(MOTIFIS[1], "r") as script:
                    for i in script:
                        minifis = i.strip()
                        OPENED.append(minifis)
                    Mult(OPENED)

            elif i == TOKENS[25]:
                OBB = INPUT.split("'")
                OBJECTS.append(OBB[1])

            elif i == TOKENS[26]:
                MOMOA = INPUT.split(".")
                KAYMAY = MOMOA[1].split("'")
                OBJECT_SPRITE[OBJECTS.index(MOMOA[0])] = KAYMAY[1]

            elif i == TOKENS[27]:
                KOKOMO = INPUT.split("'")
                print(OBJECT_SPRITE.index(KOKOMO[1]))
                render(OBJECT_SPRITE.index(KOKOMO[1]))

            elif i == TOKENS[28]:
                OLIMA = INPUT.split("'")
                print(SHELLDATA[SHELLS.index(OLIMA[1])])
			
            elif i == TOKENS[29]:
                SUGMA = INPUT.split(".")
                MOCOMO = SUGMA[1].split("'")
                SHELLDATA[SHELLS.index(SUGMA[0])] = MOCOMO[1]

            elif i == TOKENS[30]:
                BALLCM = INPUT.split("'")
                if BALLCM[1] not in PUBLIC_SHELLS:
                    print('This shell is private')
                else:
                    with open("DIVI/src/compiler/Shells/" + BALLCM[1] + '.divi', "r") as a_file:
                        for i in SHELLOPEN:
                            SHELLOPEN[i] = ''
                        for line in a_file:
                            stripped = line.strip()
                            SHELLOPEN.append(stripped)
                    Mult(SHELLOPEN)

            elif i == TOKENS[36]:
                addition = INPUT.split('+')
                for i in range(2):
                    addition[i].replace(" ", "")	
                print(int(addition[0]) + int(addition[1])) 
			
            elif i == TOKENS[35]:
                subtractions = INPUT.split('-')
                for i in range(2):
                    subtractions[i].replace(" ", "")
                print(int(subtractions[0]) - int(subtractions[1]))
			
            elif i == TOKENS[37]:
                division = INPUT.split("/")
                for i in range(2):
                   division[i].replace(" ", "")
                print(int(division[0])/int(division[1]))
			
            elif i == TOKENS[38]:
                request = INPUT.split(".request('")
                req = request[1].split("')")
                if req[0] == 'script':
                    with open('DIVI/src/compiler/Shells/' + request[0] + '.divi') as r:
                        for p in r:
                            stripped = p.strip()
                            print(stripped)
                if req[0] == 'token':
                    print(SHELL_TOK[SHELLS.index(request[0])])
				

for i in range(len(DEFAULT)):
    write(DEFAULT[i])