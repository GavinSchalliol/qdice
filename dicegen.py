import sys

inputFile = "wordlist.txt"
outputFile = "dw_wordlist.txt"

def printLine(q1,q2,q3,q4,q5,index):
	number = str(q1) + str(q2) + str(q3) + str(q4) + str(q5)
	f1.write(number + " " + lines[index])

def main(a,b,c,d,e,index):
	while (a < 7):
		while (b < 7):
			while (c < 7):
				while (d < 7):
					while (e < 7):
						printLine(a,b,c,d,e,index)
						e += 1
						index += 1
					d += 1
					e = 1
				c += 1
				d = 1
			b += 1
			c = 1
		a += 1
		b = 1

# First, get rid of the existing diceware wordlist
f1 = open(outputFile, 'w')
f1.write("")
f1.close()

# Open wordlist, read the lines into array `lines`.
file = open(inputFile, 'r')
lines = file.readlines()
file.close()

# If our wordlist has < 7776 lines, we're going to hit an `index out of range` error, so let's check that.
if len(lines) < 7776:
	print "ERROR: incorrect number of lines in " + inputFile
	print "A complete wordlist must contain at least 7776 lines, and the current input file " + inputFile + " contains " + str(len(lines)) + " lines."
	sys.exit(1)

# This is where stuff happens.
f1 = open(outputFile, 'a')
main(1,1,1,1,1,0)
f1.close()
