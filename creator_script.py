# directory creator
# v 0.1
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

def openParameterFile(fileName):
    file = open('r+',fileName)
    return file

def parseFile(file):
    path = file.readline()
    for eachLine in file:
        # iterate over each line
        chars = eachLine.split(" ")
        directory = ""
        for eachPart in chars:
            # iterate over each part of the line separated by spaces
            if eachPart[0] == "!":
                # what follows is a parent directory
                directoryName = eachPart[1:]
                try:
                    os.mkdir(path+"\\"+directoryName)
                except OSError:
                    print("error")

            if eachPart == "?":
                # close the parent directory
                directoryName = ""
                return
            if eachPart == "&":
                # iterate to create new directories
                return
            if eachPart != " ":
                # directory name
                return
