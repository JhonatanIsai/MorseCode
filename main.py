import sys
import time
from art import *


morseDict = {"A":".-",
             "B":"-...",
             "C":"-.-.",
             "D":"-..",
             "E":".",
             "F":"..-.",
             "G":"--.",
             "H":"....",
             "I":"..",
             "J":".---",
             "K":"-.-",
             "L":".-..",
             "M":"--",
             "N":"-.",
             "O":"---",
             "P":".--.",
             "Q":"--.-",
             "R":".-.",
             "S":"...",
             "T":"-",
             "U":"..-",
             "V":"...-",
             "W":".--",
             "X":"-..-",
             "Y":"-.--",
             "Z":"--..",
             ".":".-.-.-",
             ",":"--..--",
             "?":"..--..",
             "/":"-..-.",
             "@":".--.-.",
             "1":".----",
             "2":"..---",
             "3":"...--",
             "4":"....-",
             "5":".....",
             "6":"-....",
             "7":"--...",
             "8":"---..",
             "9":"----.",
             "0":"-----",
             " ":" "}

def main():
    myart = text2art("Main Menu")
    print(myart)

    
    print("Morse Code Translator")
    print("[A] From alphabet to morse")
    print("[M] From morse to alphabet")
    print("[H] Help")
    print("[Q] Exit         [S] Main")



    choice = input("Enter command:")
    switch(choice)



#Converts word to list
def convertString(string):
    wordList = []
    wordList[:0] = string
    return wordList

def toMorse():
    myart = text2art("To Morse")
    print(myart)

    returnString = []
    text2art("To Morse")
    print("Enter a word or string to translate to morse code.")
    word = input("Type here:").upper()
    wordList = convertString(word)
    print(wordList) # testing

    for lett in wordList:
        for key in morseDict:
            if (lett  == key):
                value = morseDict.get(lett);
                returnString.append(value)

    print("Translation:" + str(returnString)) # get rid of parentesis

    goAgain = input("Do you want to try again? : N/Y")
    goAgain = goAgain.upper()
    if(goAgain == "Y"):
        toMorse()
    elif(goAgain == "N"):
        main()
    else:
        print("Wrong Input. re directed to main menu...")
        time.sleep(1)


def toAlphabet():
    myart = text2art("To Alpha")
    print(myart)
    returnList = []
    text2art("To Text")
    print("Separate each letter by a comma.")
    #test = ('-.-.', '.-', '-.-', '.', ' ', '--', '.')
    test = input("Enter text:")
    for code in test:
        for let in morseDict:
            if(code == morseDict.get(let)):
                returnList.append(let)

    returnList = str(returnList).replace("'","").replace("[","").replace("]","")

    print(returnList)

def switch(choice):
    switcher = {
        "A": toMorse(),
        "M": toAlphabet(),
        "H": help(),
        "Q":quit(),
        "S":main()
    }
    return switcher.get(choice)

def quit():
    sys.exit("Goodbye")

def help():
    text2art("Help Page")
    print()

def tunrToArt():
    word = text2art(" *hello")
    print(word)


main()