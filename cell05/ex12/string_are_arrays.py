import sys

args = sys.argv[1:]
WORD = "z"

if len(args) < 1:
    print("none")
else:
    count = 0
    for char in args[0]:
        if char == WORD:
            count += 1
    if count > 0:
        print(f"{WORD * count}")
    else:
        print("none")