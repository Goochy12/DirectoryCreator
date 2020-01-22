import os

path = ""

def getPath():
    global path
    pathSelection = input("Please enter a path (or 1 for previous path): ")
    if pathSelection == '1':
        return path
    return pathSelection

def getDirName():
    name = input("Please enter name of folders: ")
    return name

def getDirDetails():
    global path
    path = getPath()
    name = getDirName()

    return [path, name]


def createDir():
    global path
    dirDetails = getDirDetails()
    path = dirDetails[0]
    name = dirDetails[1]

    path = path + "\\" + name
    os.mkdir(path)

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

    path = path + "\\" + name

    for i in range(start,end+1):
        folder = path + str(i)
        try:
            os.mkdir(folder)
        except OSError:
            print("Error creating directory.")

    return

def run():
    print("Welcome to directory creator!")
    selection = ""
    while selection != 4:
        print("Please select one of the following options:")
        print("\t1. Create single directory.")
        print("\t2. Create iteration of directories.")
        print("\t3. Use a pre defined script.")
        print("\t4. Exit.")
        selection = int(input("Option: "))
        while selection < 1 or selection > 3:
            print("Please make a valid selection.")
            selection = int(input())
        if selection == 1:
            createDir()
        elif selection == 2:
            createIterDir()
        elif selection == 3:
            return
        print()


if __name__ == '__main__':
    run()
