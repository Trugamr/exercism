import re


def abbreviate(words):
    words = re.compile(r'[a-z\']+', re.I).findall(words)
    return "".join([c[0].upper() for c in words])
