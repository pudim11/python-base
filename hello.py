
"""
Hello World multi linguas.


"""
__version__ = "0.1.3"
__author__ = "Moisés Filipe"

import os
import sys


arguments = {
    "lang" : None,
    "count" : 1,
}
for arg in sys.argv[1:]:
    # TODO: tratar valueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    # TODO: usar repetiçãof
    else:
        current_language = input(
            "Choose a language:"
        )

current_language = current_language[:5]

msg ={
    "en_US": "Hello, World",
    "pt_BR": "Olá, mundo",
    "it_IT" : "Ciao, modo",
}


print(msg[current_language] * int(arguments["count"]))

