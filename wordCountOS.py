#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import string     # string library

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#dictionary for word counts
wordCounts = {}

# attempt to open input file
inputFile = os.open(textFname, os.O_RDONLY)
n = 10000 #specify number of bytes to read
docIn = os.read(inputFile, n).decode() #read n number of bytes from the input file
#convert the read information to lowercase, and remove whitespace
docIn = docIn.lower()
docIn = docIn.strip()
splitLine = re.split("[ \t" + string.punctuation + "\n" + "\r" + " ]", docIn) #split docIn based on whitespace, punctuation, newline, and \r
#run through the line and update Word Counts
for word in splitLine:
    #if the word is in the dictionary, increment it's count, otherwise, add it to the dictionary
    if word in wordCounts:
        wordCounts[word]+=1
    else:
        wordCounts[word] = 1
os.close(inputFile) #close the file
wordCounts.pop('') #Remove empty strings from wordCounts

outputFile = os.open(outputFname, os.O_WRONLY | os.O_CREAT)
for key in sorted(wordCounts.keys()):
        writeLine = str(key + " " + str(wordCounts[key]) + "\n")
        writeLine = writeLine.encode()
        os.write(outputFile, writeLine)
os.close(outputFile)
