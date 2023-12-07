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

msg = {
  "en_US": "Hello, World!",
  "pt_BR": "Olá, Mundo!",
  "it_IT": "Ciao, Mundo!",
  "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
