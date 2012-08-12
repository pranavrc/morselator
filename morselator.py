#!/usr/bin/env python

"""
Morse Code to Text and Text to Morse Code converter.
Pranav Ravichandran <me@onloop.net>
"""

import sys

''' Key Value mappings.'''
keysAndValues = {'1':".----",
		 '2':"..---",
		 '3':"...--",
		 '4':"....-",
		 '5':".....",
		 '6':"-....",
		 '7':"--...",
		 '8':"---..",
		 '9':"----.",
		 '0':"-----",
		 'a':".-",
		 'b':"-...",
		 'c':"-.-.",
		 'd':"-..",
		 'e':".",
		 'f':"..-.",
		 'g':"--.",
		 'h':"....",
		 'i':"..",
		 'j':".---",
		 'k':"-.-",
		 'l':".-..",
		 'm':"--",
		 'n':"-.",
		 'o':"---",
		 'p':".--.",
		 'q':"--.-",
		 'r':".-.",
		 's':"...",
		 't':"-",
		 'u':"..-",
		 'v':"...-",
		 'w':".--",
		 'x':"-..-",
		 'y':"-.--",
		 'z':"--..",
		 #punctuations
		 ',':"--..--",
		 '.':".-.-.-",
		 '?':"..--..",
		 ';':"-.-.-",
		 ':':"---...",
		 '/':"-..-.",
		 '-':"-....-",
		 "'":".----.",
		 '(':"-.--.",
		 ')':"-.--.-",
		 '!':"-.-.--",
		 '&':".-...",
		 '=':"-...-",
		 '+':".-.-.",
		 '_':"..--.-",
		 '"':".-..-.",
		 '$':"...-..-",
		 '@':".--.-.",
		 #whitespace
		 ' ':"|",
		}

def textToMorse(morse):
	''' Text to Morse Code Converter method. '''
	try:
		return str(keysAndValues[morse])
	except KeyError:
		print "\n" + morse + " is an invalid key."
		sys.exit()

def morseToText(text):
	''' Morse Code to Text Converter method. '''
	try:
		return [key for key, value in keysAndValues.iteritems() if value == text][0]
	except IndexError:
		print "\n" + text + " is an invalid key."
		sys.exit()

if __name__ == "__main__":
	try:
		''' Command Line arguments. '''
		if int(sys.argv[1]) == 1:
			for eachKey in str(sys.argv[2]):
				print(textToMorse(eachKey.lower())),
		elif int(sys.argv[1]) == 2:
			listOfKeys = str(sys.argv[2]).split()
			for eachKey in listOfKeys:
				sys.stdout.write(morseToText(eachKey.lower()))
		else:
				print 'Usage: "python morselator.py <mode> <string>" Modes: Text to Morse - 1, Morse to Text - 2',

	except IndexError:
		''' Non Command Line. '''
		while True:
			try:
				mode = int(raw_input("For Text to Morse, enter 1, and for Morse to Text, enter 2: "))
				break
			except ValueError:
				print 'Invalid option.'

		key = str(raw_input("Enter string to be converted: "))
		
		if mode == 1:
			for eachKey in str(key):
				print(textToMorse(eachKey.lower())),
		elif mode == 2:
			listOfKeys = str(key).split()
			for eachKey in listOfKeys:
				sys.stdout.write(morseToText(eachKey.lower()))

	print
