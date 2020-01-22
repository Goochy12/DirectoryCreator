# directory creator
# v 1.0
# script to create directories
# format
"""
each directory on a line will go into the parent folder
! - represents a parent directory. Any line under this will be a child
    uses: !ParentFolder
? - represents the closing of a parent directory (go back up 1 directory)
& - represents an iteration of numbers
    uses: & X 0 12 - will iterate from 0 to 12 folders starting with X - X0..X12
$ - represents a space " "
    uses: Year$1 == Year 1
- - used to separate iterations
"""

import os

path = ""
recentDir = ""


def getPath():
    global path
    global recentDir
    print("Please enter a path:")
    print("Hint: press 1 for previous path or 2 for newest directory")
    pathSelection = input("Path: ")
    if pathSelection == '1':
        return path
    elif pathSelection == '2':
        path = path + "\\" + recentDir
        return path
    return pathSelection


def getDirName():
    global recentDir
    recentDir = input("Please enter name of folder: ")
    return recentDir


def getDirDetails():
    global path
    path = getPath()
    name = getDirName()

    return [path, name]


def makeDir(folder, path, name, single):
    try:
        os.mkdir(folder)
        os.system("cls")
        print("Successfully created " + name + " folder in directory: " + path)
        print()
    except OSError:
        print("Error creating directory.")


def createDir():
    global path
    dirDetails = getDirDetails()
    path = dirDetails[0]
    name = dirDetails[1]

    folder = path + "\\" + name
    try:
        os.mkdir(folder)
        os.system("cls")
        print("Successfully created " + name + ", \'" + name + "\' folder in directory: " + path)
        print()
    except OSError:
        print("Error creating directory.")


def createIterDir():
    global path
    dirDetails = getDirDetails()
    path = dirDetails[0]
    name = dirDetails[1]

    start = int(input("Please enter starting value: "))
    end = int(input("Please enter ending value: "))
    while start > end:
        start = int(input("Please enter a valid starting value: "))
        end = int(input("Please enter a valid ending value: "))

    iterateDir(start,end,name, path)

    return

def iterateDir(start, end, name, path):
    for i in range(start, end + 1):
        folder = path + "\\" + name + str(i)
        try:
            os.mkdir(folder)
            print("\nSuccessfully created " + str(start) + " to " + str(
                end) + ", \'" + name + "\' folders in directory: " + path + "\n")
        except OSError:
            print("Error creating directory.")
    return


def runScript():
    scriptPath = input("Please enter the path to the script: ")

    with open(scriptPath) as file:
        path = file.readline()
        path = path.strip("\n")
        line = file.readline()
        line = line.strip("\n")

        while line:
            parts = line.split(" ")
            for eachPart in parts:
                # iterate over each part of the line separated by spaces
                if eachPart[0] == "!":
                    # what follows is a parent directory

                    directoryName = eachPart[1:]

                    directoryName = directoryName.replace("$", " ")

                    try:
                        path = path + "\\" + directoryName
                        os.mkdir(path)
                    except OSError:
                        print("error")

                elif eachPart == "?":
                    # close the parent directory
                    path = path.split("\\")
                    path.pop()
                    path = "\\".join(path)

                elif eachPart[0] == "&":
                    # iterate to create new directories
                    params = eachPart[1:].split("-")

                    name = params[0]
                    name = name.replace("$", " ")

                    start = int(params[1])
                    end = int(params[2])

                    iterateDir(start, end, name, path)

            line = file.readline()
            line = line.strip("\n")

# D:\UserData\Documents\repositries\DirectoryCreator\testScript.txt

    return

def openParameterFile(scriptPath):
    file = open(scriptPath, 'r+')
    return file.readlines()


def run():
    os.system("cls")

    print("Welcome to directory creator!")
    selection = ""

    while selection != 4:
        print("Please select one of the following options:")
        print("\t1. Create single directory.")
        print("\t2. Create iteration of directories.")
        print("\t3. Use a pre defined script.")
        print("\t4. Exit.")

        selection = int(input("Option: "))

        while selection < 1 or selection > 4:
            print("Please make a valid selection.")
            selection = int(input())

        if selection == 1:
            createDir()
        elif selection == 2:
            createIterDir()
        elif selection == 3:
            runScript()


if __name__ == '__main__':
    run()
