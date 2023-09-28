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
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        line = line.lower() #convert word to lowercase and remove punctuation
        line = line.strip() # get rid of newline characters
        splitLine = re.split("[ \t" + string.punctuation + " ]", line) # split line on whitespace and punctuation
        #run through the line and update Word Counts
        for word in splitLine:
            #if the word is in the dictionary, increment it's count, otherwise, add it to the dictionary
            if word in wordCounts:
                wordCounts[word]+=1
            else:
                wordCounts[word] = 1
    inputFile.close()

wordCounts.pop('') #Remove empty strings from wordCounts

with open(outputFname, 'w') as outputFile:
    for key in sorted(wordCounts.keys()):
        outputFile.write(key + " " + str(wordCounts[key]) + "\n")
    outputFile.close()