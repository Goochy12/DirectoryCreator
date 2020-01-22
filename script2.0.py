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
    dirDetails = getDirDetails()
    path = dirDetails[0]
    name = dirDetails[1]

    start = int(input("Please enter starting value: "))
    end = int(input("Please enter ending value: "))
    while start > end:
        start = int(input("Please enter a valid starting value: "))
        end = int(input("Please enter a valid ending value: "))

    for i in range(start,end+1):
        folder = path + "\\" + name + str(i)
        try:
            os.mkdir(folder)
            os.system("cls")
            print("Successfully created " + str(start) +" to " + str(end) + ", \'" + name + "\' folders in directory: " + path)
            print()
        except OSError:
            print("Error creating directory.")

    return

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
            return

if __name__ == '__main__':
    run()
