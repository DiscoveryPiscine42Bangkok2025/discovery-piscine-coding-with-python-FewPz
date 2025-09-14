import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    word = args[0]
    match = input("What was the parameter? ")
    if word == match:
        print("Good job!")
    else:
        print("Nope, sorry...")