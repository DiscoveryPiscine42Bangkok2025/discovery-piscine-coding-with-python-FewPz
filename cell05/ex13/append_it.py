import sys

args = sys.argv[1:]
WORD = "ism"

if len(args) < 1:
    print("none")
else:
    for arg in args:
        if WORD in arg:
            continue
        arg += WORD
        print(arg)