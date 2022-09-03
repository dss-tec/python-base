#!/usr/bin/env python3
""" Hello World Many Languages.

This program printing the Hello World message based on the LANG enviroment variable of system.

How to use:
    You need have the LANG variable configured on system. Case the LANG variable were unset,
the message will be showed in english.

Excute:
    ./hello.py
"""

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
