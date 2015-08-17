# qdice
A project to create a more feminist/queer/intersectional version of the diceware wordlist.

## I just want your wordlist.
```
$ git clone git@github.com:GavinSchalliol/qdice.git
$ cd qdice
$ ./dicegen.sh
$ nano diceware_wordlist.txt
```

## How do I help?
The easiest way is to choose one of the `list*` files, look through it manually, and mark words for deletion.

Alternatively, this project still needs more infrastructure work:
* list generator should detect & exclude marked words
* easier interface to find & replace marked words
* more human-readable filenaming system
* bug fixes
* anything else you can think of!

## What are these files?
* `dicegen.sh`: This is the script that concatenates the `list*` files and assigns each of them a diceware roll. Largely adapted from [here][https://gist.github.com/zxjinn/4463806] by @zxjinn.

* `list*`: These are the word lists used to generate the diceware wordlist, split into smaller sublists for easier editing.

* `wordlist.txt`: The original wordlist. Probably doesn't need to be here, actually.
