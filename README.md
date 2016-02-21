# qdice
Have you ever generated a diceware passphrase and ended up with a word that you'd rather not use in a passphrase forever? In the spirit of being more aware of the language we use and its effect on other people, this project is an attempt to create a more inclusive, diverse, feminist, queer, and intersectional version of the diceware wordlist.

## I just want your wordlist.
```
$ git clone git@github.com:GavinSchalliol/qdice.git
$ cd qdice
$ python dicegen.py
$ cat dw_wordlist.txt
```

## Important files
Input and output files are determined by the `inputFile` and `outputFile` variables at the beginning of the `dicegen.py` script.
By default, they are:

* `wordlist.txt`: a list of words, separated by newlines. Must be at least 7776 lines, or the script will not run.

* `dw_wordlist.txt`: Once you've run `dicegen.py`, this file contains your diceware wordlist!
