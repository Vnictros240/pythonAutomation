#!/usr/bin/python3

# Functions for using Automation

def spam():
	eggs = 'spam and eggs'
	print(eggs)

def bacon():
	eggs = 'bacon and eggs'
	print(eggs)
	print("Now we call the spam() in the next line: \n")
	spam()
	print("\n\nNow we call the print(spam()) in the next line: \n")
	print(spam())
	
bacon()