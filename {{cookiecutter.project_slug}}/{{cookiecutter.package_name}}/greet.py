import sys


def greet(name: str, out=sys.stdout) -> None:
    out.write('Hello {}!\n'.format(name))
