#!/usr/bin/env python3
import base64
from string import ascii_letters


def rotate(s, amt):
    for pos in (ascii_letters.index(c) for c in s):
        base = (pos // 26) * 26
        yield ascii_letters[base + ((pos + amt) % 26)]


def decipher(key: str) -> str:
    *_, cipher = key.split('_')

    s = base64.b64decode(cipher).decode()
    for i in range(0, 26):
        yield ''.join(rotate(s, i))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print(f'usage: {sys.argv[0]} <email> <api_key>')
        sys.exit(0)

    email, key = sys.argv[-2:]

    possibilities = list(decipher(key))
    for i, p in enumerate(possibilities):
        print(f'{i}) {p}')
    chosen = int(input('Which input looks good? '))

    # I could use the json module, but one less import...
    print(f'{"email": "{email}", "api_key": "API_KEY_{possibilities[chosen]}"}')
