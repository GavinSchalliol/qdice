# First, get rid of the existing diceware wordlist
f1 = open('dw_wordlist.txt', 'w')
f1.write("")
f1.close()

file = open('wordlist.txt', 'r')
lines = file.readlines()
file.close()

f1 = open('dw_wordlist.txt', 'a')

global a
global b
global c
global d
global e
global f
u = 1
v = 1
w = 1
x = 1
y = 1
z = 1
index = 0

def printNumber(q1,q2,q3,q4,q5):
	q1 = str(q1)
	q2 = str(q2)
	q3 = str(q3)
	q4 = str(q4)
	q5 = str(q5)
	number = q1 + q2 + q3 + q4 + q5
	f1.write(number + " " + lines[index] + '\n')

while (v < 7):
	a = v
	while (w < 7):
		b = w
		while (x < 7):
			c = x
			while (y < 7):
				d = y
				while (z < 7):
					e = z
					printNumber(a,b,c,d,e)
					z += 1
					index += 1
				y += 1
				z = 1
			x += 1
			y = 1
		w += 1
		x = 1
	v += 1
	w = 1

f1.close()
