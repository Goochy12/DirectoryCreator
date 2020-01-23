# directory creator
# v 1.0
# script to create directories
# format
"""
each directory on a line will go into the parent folder
! - Used at the start of a directory. Any following directory will be created
    inside of this directory unless a '?' is used.
    eg: !ParentFolder
? - Represents the closing of a parent directory (go back up 1 directory)
    eg: !ParentFolder !ChildFolder ? !SecondChild ? ?
& - Command to start an iteration of numbers appended to the end of a folder name
    eg: &Folder-0-12 => will iterate from 0 to 12 folders starting
    with Folder0 and ending at Folder12.
    Use a '-' to separate starting and ending iterations.
$ - Represents a space " "
    eg: My$Pictures == My Pictures
"""

import os  # needed to create directories

path = ""  # global path variable
recentDir = ""  # global variable for recently created directory name


def getPath():
    """
    Method to get the path for the new folder
    :return: the path
    """
    global path  # get the global path
    global recentDir  # get the global recently created directory
    pathSelection = ""
    while pathSelection == "":
        # iterate while a path has not been entered
        print()
        print("Please enter a path:")  # print path message
        if path != "" and recentDir != "":
            # check if a path and recent directory have been created
            print("Hint: press 1 for previous path or 2 for newest directory")
        pathSelection = input("Path: ")  # get user input
        if pathSelection == '1':
            # user wants to use a previously entered path
            if path != "":
                # return a previous path if one exists
                return path
        elif pathSelection == '2':
            # user wants to use the newset created directory
            if recentDir != "":
                # check if a recent directory exists
                path = path + "\\" + recentDir  # update the path
                return path  # return the path
        else:
            # else return the user created path
            return pathSelection
        pathSelection = ""  # reset user input


def getDirName():
    """
    Method to get the name of the new directory
    :return: recentDir - the name of the new directory
    """
    global recentDir  # get the global newest created directory name
    recentDir = input("Please enter name of folder: ")  # get user input
    return recentDir  # return the directory name


def getDirDetails():
    """
    Method to get the details of the new directory
    :return: List[path, name] - where path is the new path and name is the name of the directory
    """
    global path  # get the global path
    path = getPath()  # call the get path method
    name = getDirName()  # call the get name method

    return [path, name]  # return a list of path and name


def initDir():
    """
    Method to create a single directory
    :return: None
    """
    global path  # get the global path
    dirDetails = getDirDetails()  # get the directory path and name
    path = dirDetails[0]  # get the path
    name = dirDetails[1]  # get the name

    folderDir = path + "\\" + name  # get the new folder path
    createDir(folderDir, name, path)

    return


def createDir(folderDir, name, origPath):
    """
    Method to create a directory
    :param folderDir: the directory of the new folder
    :param name: name of the new folder
    :param origPath: the original path for the new folder
    :return: None
    """
    try:
        os.mkdir(folderDir)  # try to create the folder
        print()
        print("Successfully created " + name + ", \'" + name + "\' folder in directory: " + origPath)
        print()  # print a success message
    except OSError:
        print()
        print("Error creating directory.")  # print an error message
        print()


def initIterDir():
    """
    Method to get the information for a new directory iteration
    :return: None
    """
    global path  # get the global path
    dirDetails = getDirDetails()  # get the directory path and name
    path = dirDetails[0]  # get the path
    name = dirDetails[1]  # get the name

    start = 0
    end = -1

    while start > end:
        # iterate why the values are invalid
        start = int(input("Please enter starting value: "))  # get the starting value
        end = int(input("Please enter ending value: "))  # get the ending value

    createIterateDir(start, end, name, path)  # call the method to create directories

    return


def createIterateDir(start, end, name, path):
    """
    Method to create files through an iteration
    :param start: starting value
    :param end: ending value
    :param name: the name of the iteration folder
    :param path: the path for the new directories
    :return: None
    """
    for i in range(start, end + 1):
        # create each folder
        folder = path + "\\" + name + str(i)  # create the path
        try:
            os.mkdir(folder)  # try to make the folder
            print()
            print("\nSuccessfully created " + str(start) + " to " + str(
                end) + ", \'" + name + "\' folders in directory: " + path + "\n")
            print()
            # print success message
        except OSError:
            print()
            print("Error creating directory.")  # print error message
            print()
    return


def runScript():
    """
    Method to run create files from a script
    :return: None
    """
    scriptPath = input("Please enter the path to the script: ")  # get the script path

    with open(scriptPath) as file:
        # while the file is open
        path = file.readline().strip("\n")  # get the path - first line of script
        line = file.readline().strip("\n")  # get the second line of the script

        while line:
            # while the line is valid
            parts = line.split(" ")  # split each line by a space
            for eachPart in parts:
                # iterate over each part of the line separated by spaces
                if eachPart[0] == "!":
                    # what follows is a parent directory
                    directoryName = eachPart[1:]  # remove the '!'
                    directoryName = directoryName.replace("$", " ")  # replace '$' with spaces

                    folderDir = path + "\\" + directoryName  # create the new path
                    createDir(folderDir, directoryName, path)  # call method to create directories
                    path = path + "\\" + directoryName  # update the path


                elif eachPart == "?":
                    # close the parent directory
                    path = path.split("\\")  # split the path by '\'
                    path.pop()  # pop the last directory
                    path = "\\".join(path)  # rejoin the path

                elif eachPart[0] == "&":
                    # iterate to create new directories
                    params = eachPart[1:].split("-")  # split the part by '-' and remove the '&'

                    name = params[0]  # get the name of the folder
                    name = name.replace("$", " ")  # replace the '$' with spaces

                    start = int(params[1])  # get the starting iteration value
                    end = int(params[2])  # get the closing iteration value

                    if start <= end:
                        createIterateDir(start, end, name, path)  # call the method to create iterations

            line = file.readline().strip("\n")  # read the next line

    return


def run():
    """
    Main running method
    :return: None
    """
    os.system("cls")  # wipe the system screen

    print("Welcome to directory creator!")  # print welcome message
    selection = ""  # initialise user selection

    while selection != 4:
        # iterate while user does not quit
        print("Please select one of the following options:")  # instruction message
        print("\t1. Create single directory.")
        print("\t2. Create iteration of directories.")
        print("\t3. Use a pre defined script.")
        print("\t4. Exit.")

        selection = int(input("Option: "))  # get user input

        while selection < 1 or selection > 4:
            # while the selection is invalid
            print()
            print("Please make a valid selection.")
            selection = int(input())

        if selection == 1:
            initDir()  # create single directory
        elif selection == 2:
            initIterDir()  # create iteration directory
        elif selection == 3:
            runScript()  # create directories from script
        else:
            quit()


if __name__ == '__main__':
    run()  # run main program
