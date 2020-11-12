import os
import sys
import re
from msvcrt import getch
import json

dir = str(input('Listen dir (PATH TO FOLDER):'))

def createRegex(json):	
	return [re.sub('\s+', '\\\s+', ''.join(json["replacement"]['symbols'])), '|'.join(json["replacement"]['words'])]

for filename in os.listdir(dir):
    with open('config.json') as f:
        try:
            regexTemplate = createRegex(json.load(f))
            newName = re.sub('[{0}]+|({1})'.format(regexTemplate[0], regexTemplate[1]), '', filename)
            print("Rename {} => {}".format(filename, newName))
            os.rename(dir + filename, dir + newName)
          
        except Exception as e:
            raise e
        
print("Successfull")        
key = getch()
if key==b'\r':
    sys.exit(0)