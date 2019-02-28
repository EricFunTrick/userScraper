#!usr/bin/env python3

import re

ValidUserNamesRegex = r"@((?:[a-z][a-z]+))"

wordFound = []
pattern = re.compile(ValidUserNamesRegex)

try:
    with open('inputFile.txt', 'rt') as in_file:
        for lineNumber, line in enumerate(in_file):
            if pattern.search(line) is not None:
                wordFound = re.search(pattern, line)
                addingWords = wordFound.group()
                print(addingWords.lstrip('@'), file=open("extractedUserNames.txt", "a"))
                print(addingWords.lstrip('@'))


except FileNotFoundError:
    print("Log file not found.")

