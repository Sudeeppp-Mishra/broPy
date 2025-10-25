# Python file detection

import os # this module provides a way to python programs to interact with the OS

file_path = "fileStuffs" # This is relative path
# we can also work with absolute paths

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That's a directory")
        
else:
    print("That location doesn't exists")