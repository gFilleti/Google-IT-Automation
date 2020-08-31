#!/usr/bin/env python3.8
import re #importing regular expressions

print('\n----------------------------------Regular Expressions------------------------------------\n')

#grep its a bash  powerfull tool for aplaying regular expressions (shortened as regexes)\n
#grep(get regular expression) will print what it find with regular expressions of a file\n
#but the same principle will be use in python re, by using the Reserverd characters:\n
'''site for checking rege https://regex101.com/'''
print('''
Metacharacters:

Metacharacters are characters with a special meaning.\n

Character 	Description \n

[] 	        A set of characters\n
            Example - find all lower case characters alphabetically between "a" and "m") :
            re.findall("[a-m]", "The rain in Spain" => ['h', 'e', 'a', 'i', 'i', 'a', 'i']\n

\ 	        Signals a special sequence (can also be used to escape special characters)\n
            Example - \d Find all digit characters:
            re.findall("\d", "That will be 59 dollars") => ['5', '9'] \n

            other use for \ is as escapes any special character, which means it can use a reserved caractrer as it was a common character
            \$ => $ or \.com => .com without \ the regex would see $ or . as special charactes
            some special caracters wont work with \, as '\n (new line) '\t (tab) etc.

. 	        Any character (except newline character)\n
            Example - search for a sequence that starts with "he", followed by two (any) characters, and an "o":
            re.findall("he..o", "hello world") => ['hello']\n

^       	Starts with\n
            Example - retrun string if the string starts with 'hello':
            re.findall("^hello", "hello world") => ['hello']\\n

$       	Ends with\n
            Example - returns the string if the string ends with 'world':
            re.findall("world$", "hello world") => ['world']\n

*       	Zero or more occurrences\n
            Example - returns list strings if the string contains "ai" followed by 0 or more "x" characters:
            re.findall("aix*", "The rain in Spain falls mainly in the plain!") => ['ai', 'ai', 'ai', 'ai']
            (theres no aix in the string, but with * will return the nearest matches in this case ai)\n


+       	One or more occurrences\n
            Example - if the string contains "ai" followed by 1 or more "x" characters:
            re.findall("aix*", "The rain in Spain falls mainly in the plain!") => []
            (theres no aix in the string, + need ate least one complete match)\n
            re.findall("ain*", "The rain in Spain falls mainly in the plain!") => ['ain', 'ain', 'ain', 'ain']

.* or .+     Both Repetitions are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible.

?            The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional.
             For example, home-?brew matches either 'homebrew' or 'home-brew'.
             non-greedy qualifiers *?, +?, ??, or {m,n}?, which match as little text as possible.

{}       	Exactly the specified number of occurrences\n
            Example - if the string contains "a" followed by exactly two "l" characters:
            re.findall("al{2}", "The rain in Spain falls mainly in the plain!") => ['all']

|       	Either or\n
            Example - if the string contains either "falls" or "stays":
            re.findall("falls|stays", "The rain in Spain falls mainly in the plain!") => ['falls']\n

()      	Capture and group\n
            will return only the string in parentheses
''')

print('''
Special Sequences:\n

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning\n

character 	Description 	                                                                                                       Example
\A 	        Returns a match if the specified characters are at the beginning of the string 	                                      "\AThe" \n

'\b 	    Returns a match where the specified characters are at the beginning or at the end of a word                           r"'\bain" \n
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")                          r"ain'\b" \n

\B 	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word        r"ain\B" \n
            (the "r" in the beginning is making sure that the string is being treated as a "raw string") 	                      r"\Bain" \n

\d 	        Returns a match where the string contains digits (numbers from 0-9) 	                                              "\d" \n

\D 	        Returns a match where the string DOES NOT contain digits 	                                                          "\D" \n

\s 	        Returns a match where the string contains a white space character 	                                                  "\s" \n

\S 	        Returns a match where the string DOES NOT contain a white space character                                             "\S" \n

\w 	        Returns a match where the string contains any word characters
            (characters from a to Z, digits from 0-9, and the underscore _ character)                                             "\w" \n

\W 	        Returns a match where the string DOES NOT contain any word characters                                                 "\W" \n

\Z 	        Returns a match if the specified characters are at the end of the string                                              "Spain\Z" \n
''')


print('''
Sets

A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set 	            Description 	a+
[arn] 	            Returns a match where one of the specified characters (a, r, or n) are present

[a-n] 	            Returns a match for any lower case character, alphabetically between a and n

[^arn]          	Returns a match for any character EXCEPT a, r, and n

[0123] 	            Returns a match where any of the specified digits (0, 1, 2, or 3) are present

[0-9] 	            Returns a match for any digit between 0 and 9

[0-5][0-9] 	        Returns a match for any two-digit numbers from 00 and 59

[a-zA-Z] 	        Returns a match for any character alphabetically between a and z, lower case OR upper case

[+] 	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
''')



print('\n----------------------------------Re.Search------------------------------------\n')

with open('text.txt') as file:
    regex = input("Type the pattern to be search for- ")

    for line in file:
        line_split = line.split()
        for word in line_split:
            result = re.search(r'{}'.format(regex), word)# the r in the frist parameter indicated rawstring which means that the python interpreter
            if result == None:                           #shouldn't try to interpret any special characters, and pass the  string to the function as is
                continue                                 #Using r (raw) should always be used in regular expressions in Python, for theres no use a special
            print(result)                                #character for the text as it was a defined regular expression and messs around the result

#the re.research funtion will return the string intereval(slice) in the string that was found the match pattern. Match is the substring result the match pattern
#re.search(r'aza', 'plaza') => span(2,5) match='aza', if we use the span numbe for slice the word plaza => 'plaza'[2:5] = aza
#exemples of diferrente match results of re.search(r'p.ng', penguin) = > span (0,4), match ='peng' or re.search(r'p.ng', clapping) span=(4,8), match='ping'
#In this code the None is been omitted. But when tre re.search returns None it means that no match was found.
print('\n----------------------------------Re.findall------------------------------------\n')

with open('text.txt') as file:

    regex = input("Type the regular expressions- ") # finding all number [0-9]+, for takin the org part of email ^From .*@([^ ]*)
    for line in file:                               # finding the email \S+@\S+
        result = re.findall(r'{}'.format(regex),line)
        if result == []:
            continue

        print(result)

#the re.findall function will return all the possible matches of a regular expression;

print('\n----------------------------------Exemple extracting PID(PROCESS ID) from log-----------------------------------\n')

def extract_pid():
    text = open('text.txt')
    read = text.read()
    regex = r"^Log:.*.\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex,read)
    print(result,"\n")
    text.close()
    if result is None:
        return ""
    return "result[0]: {}; result[1]: {}; result[2]: {};".format(result[0], result[1], result[2])

print(extract_pid())

print('\n----------------------------------Re.split-----------------------------------\n')
#works similary to the python string function split(), but instead of taking a string as a separator it uses regular expression as a separator
with open('text.txt') as file:

    regex = input("Type the regular expressions- ") # finding all number [0-9]+, for takin the org part of email ^From .*@([^ ]*)
    for line in file:                               # finding the email \S+@\S+
        result = re.split('{}'.format(regex),line)
        if result == []:
            continue

        print(result)

print('\n----------------------------------Re.sub----------------------------------\n')
#works similary to the python string method .replace that creates a new string, the re.sub its similiar but use regular expressions for matching
#and replecing.
def sub(text):
    print("original email: {}\n".format(text))
    replacer = input("type the replacemente for email: ") # finding all number [0-9]+, for takin the org part of email ^From .*@([^ ]*)
    regex =r"[\w.%+-]+@[\w.-]+"
    result = re.sub('{}'.format(regex), replacer, text)
    return result

text1 = "Received an email from gogopowerrogers@rangers.com"
print("\nNew email: {}".format(sub(text1)))

print('\n----------------------------------Re.sub2----------------------------------\n')
#we can use the sub to change order os a string with two regular rexpression in the frist parameter, r"([\w .-]*), ([\w .-]*)$"
# and use general notation of regex  like r'\2\1' 'in the secund parameter ( replace parameter of sub method)
# the replacer r"\2\1" will put frist the second  match ([\w .-]*)$ (\2) then the frist match ([\w .-]*) (\1)

name= "Lovelace, Ada"
print(name,"\n")
print("name using regex r'{}' in change parameter:".format(r'\2 \1'))
print(re.sub(r"([\w .-]*), ([\w .-]*)$", r"\2 \1", name),"\n")#the white space it literal, without it the print would be AdaLovelace

print("name using regex r'{}'' in change parameter:".format(r"\1 \2"))
print(re.sub(r"([\w .-]*), ([\w .-]*)$", r"\1 \2", name))

print('\n----------------------------------END------------------------------------\n')

#in all function above we can add a parameter to ignore upper cases, as tje re.IGONORECASE
#re.search(r'p.ng', "Pangaea", re.IGONORECASE) => span =(0,4), match='Pang'
''''

-> . dot mathces any characters. Using l.rts it will search all words which has a l an character and rts ( alerts, blurts, flirts)\n

-> ^ circunflex indicates the begining of the line. ^ its used to search a line begins with a pattern, exple: ^cat (begins with cat?)\n

-> $ dolarsign indicates the end of the line. $ its used to search a line ends with a pattern, exple: cat$ (ends with cat?)\n

-> [] sequere  braclets its used for determine Character Classes, its use to finde matches of a group or charactes, [group of character].
Which means that it let us list the characters(group) we want mach inside those brackests, for exemple:
[Pp] will search in the string uppercase P and lowercase p ; [a-z] will search in the string for any leater in lowercases;[0-9] for all digits;
[a-zA-Z0-9] will search for a group of character a to z in lowercase and uppercase, and seach for any number;
[.,:;?!] in this case will search for all the punctuation sybols between the square brackests.\n

-> [^] in this case it will search for ant matches that is not ate the group. Exemple [^a-zA-Z] this is same as not [a-zA-Z], so it will search for anything
besides lowercasse amd upper case aplhabet characters. So it will return punctuation sinbols, number, whitespaces etc, anything but letter;
[^ ], this will searh anything except whitespaces;\n

-> | pipeline can be uses for seach for two matches one or other: re.search(r'cats|dogs', 'I like both cats and dogs' ->"span(12, 15), match='cat'
if the both are found it will return the frist value; But it pipeline its used in re.findall function it will return the both macthes ['cat','dog'].\n

-> * search for repeated matches. Using with dot . it will search for any mathes greed. but by default it greed.
So it will take any caracter in relation to the matches, if is a lines i will return the line.
'''
