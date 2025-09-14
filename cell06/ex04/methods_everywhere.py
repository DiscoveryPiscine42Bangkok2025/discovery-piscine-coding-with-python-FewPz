import sys

args = sys.argv[1:]

def shrink(i):
    print(i[:8])

def enlarge(i):
    print(i + 'Z' * (8 - len(i)))

if len(args) < 1:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)