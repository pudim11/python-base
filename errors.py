import sys
import os

if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("[ERROR] File names.txt not found")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("Missing name in the list")
    sys.exit(1)