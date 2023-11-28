import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.fox(f'Hello, {sys.argv[1]}')