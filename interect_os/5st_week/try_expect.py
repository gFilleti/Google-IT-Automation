#!/usr/bin/env python3.8

def character_frequency(filename):
    """count the frequency of wach character in the given file"""
    #Frist try to open the filen

    try:
        f = open(filename)
    except OSError:
        return None

    #Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters

def main():

    file = input("Type file name: ")
    result = character_frequency(file)
    print(result)
main()
