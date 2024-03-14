import sys
import os


try:
    names = open("names.txt").readlines()
except FileExistsError as e:
    print(f"str(e).")
    sys.exit(1)
    # TODO: usar um retry

try:
    print(names[0])
except:
    print("Missing name in the list")
    sys.exit(1)