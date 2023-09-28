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
readIn = os.read(inputFile, n) #Assign the file as a string
docIn = readIn.decode("utf-8","strict")

"""
    for line in inputFile:
        line = line.strip() # get rid of newline characters
        splitLine = re.split("[ \t]", line) # split line on whitespace and punctuation - DOES NOT SEPARATE DASHED DOUBLE WORDS
        #run through the line and update Word Counts
        for word in splitLine:
            word = word.lower().translate(str.maketrans('','', string.punctuation)) #convert word to lowercase and remove punctuation
            #word = word.lower()
            #if the word is in the dictionary, increment it's count, otherwise, add it to the dictionary
            if word in wordCounts:
                wordCounts[word]+=1
            else:
                wordCounts[word] = 1

inputFile.close()
wordCounts.pop('')
#print(wordCounts.items())
with open(outputFname, 'w') as outputFile:
    for key in sorted(wordCounts.keys()):
        outputFile.write(key + " " + str(wordCounts[key]) + "\n")
outputFile.close()
"""