
"""
Hello World multi linguas.


"""
__version__ = "0.0.1"
__author__ = "Moisés Filipe"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg ="Hello, World"


if current_language == "pt_BR":
    msg="Olá, mundo"
elif current_language == "it_IT": 
    msg="Ciao, Modo"


print(msg)

