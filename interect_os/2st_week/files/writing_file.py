#!/usr/bin/env python3.8
import os

os.chdir("base_files")
path = "novel.txt"

with open(path, "w") as file:# A File object can be opened in several different modes
                                    #A mode is similar to a file permition
                                    #it governs what can be done with the opened filesecon
                                    #by default the open function uses the "r" modes(read only)
                                    #we need pass a second argument like "w" mode(write only)
                                    #if the file doesn't exist the Python will create it.
                                    #if the file exist, then its current contents will be overwritten
                                    #by what we decide to write
                                    #It's important to remember that when openning a file in write only modes
                                    #you can't read its contents, if you ty to the intepreter raises an error
                                    #you can use other modes like:
                                    #"a" mode for appending content in the end of an existing files
                                    # "r+" read-write mode with can both read contantes and overwrite it

    file.write("The file contants was overwritten by this text  right here.\n"
                "because it was opened by open function with write-only mode\n"
                "as soom the file is opened the old contents will be deleted\n"
                "write mode its good for creating report, but see if the file alredy exists")
    
