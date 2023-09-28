#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import string

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#dictionary for word counts
wordCounts = {}

# attempt to open input file
#with open(textFname, 'r') as inputFile:
inputFile = os.open(textFname, os.O_RDONLY)
n = 50000
docIn = os.read(inputFile, n).decode() #Assign the file as a string
docIn = docIn.lower()
docIn = docIn.strip()

splitLine = re.split("[ \t" + string.punctuation + "\n" + "\r" + " ]", docIn)
#run through the line and update Word Counts
for word in splitLine:
    #print(word)
    #if the word is in the dictionary, increment it's count, otherwise, add it to the dictionary
    if word in wordCounts:
        wordCounts[word]+=1
    else:
        wordCounts[word] = 1
os.close(inputFile)
wordCounts.pop('') #Remove empty strings from wordCounts

#print(wordCounts.keys())

outputFile = os.open(outputFname, os.O_WRONLY | os.O_CREAT)
for key in sorted(wordCounts.keys()):
        writeLine = key + " " + str(wordCounts[key]) + "\n"
        writeLine = bytes(writeLine, "utf-8")
        os.write(outputFile, writeLine)
os.close(outputFile)
