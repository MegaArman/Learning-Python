from datetime import datetime

""" PYTHON VS JAVA: Most important take away: Python uses indents and colons (:) instead of braces { } likes Java. Python doesn't use semi-colons.
"Functions" are python's methods."""
""" In this program a trick to display the current date is used. A method involving string processing is used."""


import string #imports are lower cased.

#Started 9/19/14
#Date and time
now = datetime.now()
print ('%s/%s/%s' % (now.year, now.month, now.day)) #the %s gets replaces by % ()
#replace(String, string)

#print (String(now.year) + " " + String(now.month) + " " #String(now.day))

someNum = 50
print (str(someNum))


#-----------------------------------------------------
#Strings:
some_String = "wha"
print (len(some_String))
print (some_String.upper())
print (some_String.upper().lower())

#----------------------------------------------------
print("----------------------------")

def toPigLatin(word):
    
    length = len(word)
    keepGoing = "y"

    if (length > 1):
    

        firstChar = word[0]
   
        pigWord = (word.replace(word[0], " ") + firstChar + "ay") #notice how replace returns the original string with the character replaced
        # word = word[1: len(word)] + word[0] + "ay" # alternate slightly cleaner way
        print("Pig latin for " + word + " is " + pigWord)
    else:                                                       #SPACING MATTERS!!!!
        print("Empty")

#newstr = oldstr.replace("M", "")
                    
word = str(input("Type a word to translate to pig latin : "))
toPigLatin(word)
