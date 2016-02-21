import shutil
import os
import sys
from collections import deque
from config import inputFile, checkedFile, uncheckedFile

prompt = ">>"
uncheckedLines = []

def checkEnvironment():
	if os.path.isfile(inputFile) == 0:
		print "ERROR: can't find input file. Check to make sure it exists and is correctly named in `config.py`"
		sys.exit(1)
	if os.path.isfile(uncheckedFile) == 0:
		shutil.copyfile(inputFile, uncheckedFile)
	print "Performing sanity checks...done"

def getUncheckedLines():
	f1 = open(uncheckedFile, 'r')
	uncheckedLines = f1.readlines()
	f1.close()
	return uncheckedLines

# Currently, this just takes the first ten entries from the uncheckedLines list, moves them to a buffer, prints them, and returns them. More to come!
def main():
	toCheck = []
	uncheckedLines = getUncheckedLines()
	toCheck[0:10] = uncheckedLines[0:10]
	toCheck = map(lambda s: s.strip(), toCheck)
	for i in toCheck:
		print "[" + str(toCheck.index(i)) + "] " + i

checkEnvironment()
main()
