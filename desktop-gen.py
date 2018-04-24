#!/usr/bin/python3
import os, os.path, time, subprocess, sys
argv = sys.argv

os.system('clear') # Clear the screen for input

def findArgv(argv,condidtion): # Find the position of something in argv and returns the position
    try:
        for x in range(0,len(argv)):
            for i in range(0,len(condidtion)):
                if argv[x] == condidtion[i]:
                    return x
    except Exception as e:  
        print("findArgv()\n{}".format(e))
        sys.exit()

def checkArgv(argv,condidition): # Will check to see if a argument has been passed
    try:
        for x in range(0,len(argv)):
            for i in range(0,len(condidition)):
                if argv[x] == condidition[i]:
                    return True
        return False
    except Exception as e:  
        print("checkArgv()\n{}".format(e))
        sys.exit()

def pathConv(path):
	return os.path.abspath(path) # Works as a solution right now. Cant handle very complex indirect paths

def getInput(string,Default=None,Lower=False,Upper=False): # Function to get input from user
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

#########################################################################################################################################

if checkArgv(argv,["-h","--help"]) == True:
	print(
"""{}
    -h --help			Prints this help message
    -o --output			Specifys where to save the file""".format(argv[0]))
	sys.exit()

loop = True
while loop == True and checkArgv(argv,["-o","--output"]) != True:
    installPath = pathConv(getInput("Install path [./output.desktop]:",Default="./output.desktop")) # Get output of desktop file

    if os.path.isfile(installPath) == True:
        os.system("clear")
        print("Path already exsists")
        time.sleep(2)
        os.system("clear")
    else:
        loop = False
if checkArgv(argv,["-o","--output"]) == True:
	installPath = pathConv(argv[findArgv(argv,["-o","--output"]) + 1])

name = getInput("Name:") # Name of application
comment = getInput("Comment:") # Comment of application
execPath = pathConv(getInput("Exec:")) # Path to executable
terminal = getInput("Start with terminal? [true/False]:",Default="false",Lower=True) # See if it needs to be run with a terminal 
appType = getInput("Type [Application]:",Default='Application') # Type of application
icon = pathConv(getInput("Icon [emblem-default-symbolic.svg]:",Default="emblem-default-symbolic.svg")) # What icon to use
categories = getInput("Category, ';' separated [Utility;]:",Default="Utility;") # What catagory to use
executable = getInput("Mark as executable? [True/false]:",Default="True",Lower=True) # See if the .desktop file needs to be marked with the execuable function

output = open(installPath,'w') # Open .desktop file for writing

output.write('[Desktop Entry]' + '\n') # write first line to indicate its a desktop file
output.write('Name=' + name + '\n') # write name of application
output.write('Comment=' + comment + '\n') # write comment of application
output.write('Exec=' + execPath + '\n') # write path to executable
output.write('Terminal=' + terminal + '\n') # write whether or not we need to open with terminal
output.write('Type=' + appType + '\n') # write application type
output.write('Icon=' + icon + '\n') # write what icon to use
output.write('Categories=' + categories + '\n') # write what category to use for the application

output.close() # close the file

if executable == "true": # Check is we need to mark .desktop as executable
    os.system("chmod +x " + installPath)
