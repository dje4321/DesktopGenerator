#!/usr/bin/python3
import os, time, subprocess, sys
argv = sys.argv
os.system('clear') # Clear the screen for input

def findArgv(argv,condidtion): # Find the position of something in argv and returns the position
    try:
        for x in range(0,len(argv)):
            for i in range(0,len(condidtion)):
                if argv[x] == condidtion[i]:
                    return x
    except Exception as e:
        sys.stderr.write("findArgv()\n{}".format(e))
        sys.exit()

def checkArgv(argv,condidition): # Will check to see if a argument has been passed
    try:
        for x in range(0,len(argv)):
            for i in range(0,len(condidition)):
                if argv[x] == condidition[i]:
                    return True
        return False
    except Exception as e:
        sys.stderr.write("checkArgv()\n{}".format(e))
        sys.exit()

def pathConv(path):
	try:
		if os.system("which realpath") == 0: # Test if realpath exsists on the system due to a bug with abspath()
			return subprocess.getoutput("realpath {}".format(path))
		else: # If realpath does not exsist then we fallback to the buggy abspath()
			return os.path.abspath(path) # Need to find a elegant solution to the abspath() bug
	except Exception as e:
		sys.stderr.write("pathConv()\n{}".format(e))
		sys.exit()

def getInput(string,Default=None,Lower=False,Upper=False): # Function to get input from user
	try:
		while True: # Run forever for incase of no input
			output = input(string)
			if Lower == True or Upper == True: # See if we need to adjust the return some
				if Lower == True:
					output = output.lower() # Set output to lowercase
				if Upper == True:
					output = output.upper() # Set output to UPPERCASE
			if output != '': # See if input was not empty
				os.system('clear')
				return output # Return input
			elif Default != None: # See if we need to return anything
				os.system('clear')
				return Default
			else:
				os.system('clear')
	except Exception as e:
		sys.stderr.write("getInput()\n{}".format(e))
		sys.exit()

def getFile(string,Default=None):
    while True:
        output = pathConv(getInput("Output Destination [./output.desktop]:",Default="./output.desktop"))
        if os.path.isfile(output) != True:
            os.system("clear")
            return output
        else:
            os.system("clear")
            ("File already exsists")
            time.sleep(2)
            os.system("clear")

#########################################################################################################################################

if checkArgv(argv,["-h","--help"]) == True: # Check for help
	print(
    """{}
	-h --help			Prints this help message
	-o --output			Specifys where to save the file
	-t --terminal       Enable opening with a terminal
	-i --icon           Sets what icon to use. XDG or path""".format(argv[0]))
	sys.exit()

desktopFile = "[Desktop Entry]\n"

if checkArgv(argv,["-o","--output"]) == True:
    output = argv[findArgv(argv,["-o","--output"]) + 1]
else:
    output = getFile("Output Destination [./output.desktop]:",Default="./output.desktop") # Output file destination

desktopFile += "Name={}\n".format(getInput("Name:"))                                        # App Name
desktopFile += "Comment={}\n".format(getInput("Comment:"))                                  # App Comment
desktopFile += "Exec={}\n".format(getInput("Executable Path:"))                             # App executable
if checkArgv(argv,["-t","--terminal"]) == True:
    desktopFile += "Terminal=true\n"
else:
    desktopFile += "Terminal={}\n".format(getInput("Terminal [true/False]:", Default="false",Lower=True))

desktopFile += "Type={}\n".format(getInput("Type [Application]:", Default="Application"))
if checkArgv(argv,["-o","--output"]) == True:
    desktopFile += "Icon={}\n".format(argv[findArgv(argv,["-i","--icon"]) + 1])
else:
    desktopFile += "Icon={}\n".format(getInput("Icon [emblem-default-symbolic.svg]:", Default="emblem-default-symbolic.svg"))

desktopFile += "Categories={}\n".format(getInput("Category [Utility;]:", Default="Utility;"))

file = open(output,'w')
file.write(desktopFile)
file.close()
