#!/bin/bash

cat lista listb listc listd liste listf listg listh listj listk listl > wordlist.txt

DICTFN="wordlist.txt"
NUMBERZ="1 2 3 4 5 6"
NUMDICE=5
WORDLIST=""
DICEARRAY=""

# TODO allow dynamic number of dice (up to a point, max size of dictfile)

# This is a way to generate a user-defined diceware passphrase list, instead of
# the one found at http://world.std.com/~reinhold/diceware.html

function printUsage()
{
  echo "Usage: $0 -f dictionaryToRead -d numberOfDice"
}

while getopts “f:d:h” OPTION
do
	case $OPTION in
	f)
		DICTFN=$OPTARG
        ;;
	d)
		NUMDICE=5
		# NUMDICE=$OPTARG
		# Not being applied ATM, logic isn't in place for this to work
	;;
	h)
		printUsage
		exit 1
	;;
	*)
		printUsage
		exit 127
	;;
     esac
done

NUMTOPULL=$(echo "6 ^ $NUMDICE" | bc)

if [ -f $DICTFN ]
	then
		export WORDLIST=$(cat $DICTFN | sort | head -n $NUMTOPULL | tr '[A-Z]' '[a-z]')
	else
		echo "Not a valid file"
fi

WORDARRAY=($WORDLIST)
WORDARRAYLN=${#WORDARRAY[@]}

# Lines commented out from original script because I don't know what purpose they serve...
#if [ $WORDARRAYLN -lt $NUMTOPULL ]
#	then
#		echo "$DICTFN is only $WORDARRAYLN lines long, need at least $NUMTOPULL lines."
#		exit 1
#fi

for number0 in $(echo $NUMBERZ); do
	for number1 in $(echo $NUMBERZ); do
		for number2 in $(echo $NUMBERZ); do
			for number3 in $(echo $NUMBERZ); do
				for number4 in $(echo $NUMBERZ); do
					DICELIST+=$(echo "${number0}${number1}${number2}${number3}${number4} ") ;
				done
			done
		done
	done
done

DICEARRAY=($DICELIST)

for (( i = 0 ; i < $NUMTOPULL ; i++ ))
do
	echo "${DICEARRAY[$i]} ${WORDARRAY[$i]}" >> diceware_wordlist.txt
done

exit 0
