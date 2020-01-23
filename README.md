# DirectoryCreator
Simple script to streamline the creation of folders

## User Installation
### Windows
1. Download the 'dist' folder.
2. Run dirCre1.0_windows.exe

### Linux
Currently unavailanle

### MacOS
Currently unavailable

## Running the program
! - Used at the start of a directory. Any following directory will be created inside of this directory unless a '?' is used.

    eg: !ParentFolder
    
? - Represents the closing of a parent directory (go back up 1 directory)

    eg: !ParentFolder !ChildFolder ? !SecondChild ? ?
    
& - Command to start an iteration of numbers appended to the end of a folder name

    eg: &Folder-0-12 => will iterate from 0 to 12 folders starting with Folder0 and ending at Folder12.
    
    Use a '-' to separate starting and ending iterations.
    
$ - Represents a space " "

    eg: My$Pictures == My Pictures
    
### Example
    !Test$Folder$1

    &Week-1-12 !New$Folder ? ?

    !TestFolder2 ?
