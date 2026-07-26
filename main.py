#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Garante que o diretório atual está no path para imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from cli.commands import app
from cli.menu import interactive_menu

if __name__ == "__main__":
    # Se não houver argumentos, abre o menu interativo
    if len(sys.argv) == 1:
        interactive_menu()
    else:
        # Caso contrário, delega para o Typer
        app()
