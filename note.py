"""
Bloco de notas



"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read","new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("invalid usage")
    print(f"you must specity subcomand {cmds}")
    sys.exit(1)



if arguments[0] not in cmds:
    print(f"Invalid comdan {arguments[0]}")

if arguments[0] == "read":
    #leitura
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag == arguments[1].lower():
            print(f"titulo: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    #criação nota
    title = arguments[1] # TODO: tratar execpition
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
        
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text)+ "\n")