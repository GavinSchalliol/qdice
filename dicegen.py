import sys

# First, get rid of the existing diceware wordlist
f1 = open('dw_wordlist.txt', 'w')
f1.write("")
f1.close()

file = open('wordlist.txt', 'r')
lines = file.readlines()
file.close()
if len(lines) < 7776:
	print "ERROR: incorrect number of lines in wordlist file."
	print "A complete wordlist must contain at least 7776 lines, and the current wordlist contains " + str(len(lines)) + " lines."
	sys.exit(1)

f1 = open('dw_wordlist.txt', 'a')

a = 1
b = 1
c = 1
d = 1
e = 1
index = 0

def printNumber(q1,q2,q3,q4,q5):
	q1 = str(q1)
	q2 = str(q2)
	q3 = str(q3)
	q4 = str(q4)
	q5 = str(q5)
	number = q1 + q2 + q3 + q4 + q5
	f1.write(number + " " + lines[index])

while (a < 7):
	while (b < 7):
		while (c < 7):
			while (d < 7):
				while (e < 7):
					printNumber(a,b,c,d,e)
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

f1.close()
