#!/usr/bin/env python3.8

import os # this module helps with delete,rename,move file and much more
          #whid module provides a layer of abstraction Python and the OS
          #the scrip can run in any OS supported by Python but we need pay atencion
          #to the path that can be different across different operanting systems
          # as windowns cd ~\users..... linux cd ~/users... (one use \ other use /)
          #when using absolute path in our code we nned to make sure we can provide
          #alternatives  for the pçlataforms we want to support

os.chdir("base_files") #change directories, its inportant change here bbecause the


def create():
    file_name = input("\nType the file name:")
    if os.path.exists(file_name):#if file exists the funcition will return True
        print("\nFile already exists")
        main()
    else:
        with open(file_name, "w") as file:
            file.write(
            "This file was create by open funcion with write-only mode\n"
            "Because theres no File with name. If has the contents of the file was overwriten"
            )
        print("\nThe file {} was created\n".format(file_name))



# using with block to open a file, as it doesnt exist it will be created, and then
#write some stuff that will be delete with os module function remove

def delete():
    delete = input("\nWant delete the file?(y/n): ")
    if delete =="y":
        try:
            name = input("\nType file name: ")
            os.remove(name)#function will delete the file
            print("\nThe file was deleted")
        except:
            print("\nFile was not delete")
            main()

def rename():
    ask = input("\nWant rename the file?(y/n): ")
    if ask =="y":
        try:
            name = input("\nType the file name: ")
            rename = input("\nType the new file name: ")
            os.rename(name, rename)#function will rename the file
            print("\nThe file was renamed by {}".format(rename))
        except:
            print("\nFile dele_me was not renamed")
            main()

def info_file():
    try:
        name = input("\nType the file name: ")
        size = os.path.getsize(name)#function return file size
        timestamp = os.path.getmtime(name)#funcion return a Unix timestamp it represents the number of seconds since january 1st, 1970
        import datetime # this module has a function that makes timestamp more readable
        time = datetime.datetime.fromtimestamp(timestamp)
        print(
        "\nThe file info is: \n"
        "size = {}\n"
        "timestamp = {}\n"
        "time = {}\n".format(size,timestamp,time)
        )
    except:
        print("\nFile doesnt exist")
        main()



def main():

    while True:

        choose = input(
        "\nType 1 for create a file\n"
        "\nType 2 to delete the file\n"
        "\nType 3 to rename the file\n"
        "\nType 4 for check file info\n"
        "\nType 5 for to exit\n"
        "\n"
        )
        try:
            choose = int(choose)
        except:
            choose = -1

        if choose == 1:
            create()

        elif choose == 2:
            delete()

        elif choose == 3:
            rename()
        elif choose == 4:
            info_file()
        elif choose == 5:
            quit()
        else:
            print("Not a number")


main()
