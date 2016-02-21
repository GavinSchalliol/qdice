import shutil
import os
import sys
from collections import deque
from config import inputFile, checkedFile, uncheckedFile

prompt = ">>"
toCheck = []

def checkEnvironment():
	if os.path.isfile(inputFile) == false:
		print "ERROR: can't find input file. Check to make sure it exists and is correctly named in `config.py`"
		sys.exit(1)
	if os.path.isfile(uncheckedFile) == false:
		shutil.copyfile(inputFile, uncheckedFile)
	print "Performing sanity checks...done"

def getUncheckedLines():
	f1 = open(uncheckedFile, 'r')
	uncheckedLines = f1.readlines()
	f1.close()

# Currently, this just takes the first ten entries from the uncheckedLines list, moves them to a buffer, prints them, and returns them. More to come!
def main():
	toCheck[0:9] = uncheckedLines[0:9]
	queue = deque(uncheckedLines)
	del uncheckedLines[0:9]
	print toCheck
	for i in toCheck:
		queue.appendleft(i)

checkEnvironment()
getUncheckedLines()
main()
