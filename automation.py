#!/usr/bin/python3

# Functions for using Automation
# import time
# import os
# import pandas
import json

# Phone Number Validation
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[8].isdecimal():
            return False
    return True

def findPhoneNumber(message):
    for num in range(len(message)):
        phoneChunk = message[num:num+12]
        if isPhoneNumber(phoneChunk):
            print("Phone number found: ", + phoneChunk)


def fileChecker():
    while True:
        if os.path.exists("files/vegatables.txt"):
            with open("files/vegatables.txt") as file:
                print(file.read())
        else:
            print("File does not exist.")
        time.sleep(10)

def avgTemps():
        if os.path.exists("temps_today.csv"):
            data = pandas.read_csv("temps_today.csv")
            print(data.mean()["st1"])
            return data
        else:
            print("File does not exist. \nPlease double check the word you're trying to lookup. \n\n")
        time.sleep(10)

# Creating an English Dictionary
# requires 'import json'
# requires ' from difflib import get_close_matches'

data - json.load(open("data.json"))

def translate(word):
    word = word.lower().strip()
    if word in data[word]:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        ynAnswer = input("Did you mean %s instead? \n  - Enter 'Y' if YES, or 'N' if NO." % get_close_matches(word, data.keys())[0])
        ynAnswer = ynAnswer.upper().strip()
        if ynAnswer = "Y":
            return data[get_close_matches(word, data.keys())[0]]
    else:
        return "Word doesn't exist."

def englishDictionary():

    word = input("Enter a word: ")
    print()
