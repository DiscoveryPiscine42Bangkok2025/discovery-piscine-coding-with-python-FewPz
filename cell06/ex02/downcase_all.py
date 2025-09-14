import sys

args = sys.argv[1:]

def downcase_all(args):
    if len(args) < 1:
        print("none")
    else:
        print("\n".join([arg.lower() for arg in args]))

downcase_all(args)