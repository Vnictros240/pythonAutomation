#!/usr/bin/python3

# Functions for using Automation


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





