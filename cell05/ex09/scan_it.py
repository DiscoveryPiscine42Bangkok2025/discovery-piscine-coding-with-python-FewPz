import re
import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    pattern = args[0]
    sentence = args[1]
    matches = re.findall(pattern, sentence)
    print(len(matches))