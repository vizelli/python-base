#!/usr/bin/python
"""Hello World Multi Líguas.

Dependendo da língua configurada no ambiente o programa exibe
a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Alan Willer Vizelli"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

# Aqui aplicamos a condicional

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
