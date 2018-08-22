#!/usr/bin/env python3

import unicodedata
from subprocess import getoutput
from googletrans import Translator

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def translate(data):
    trans = Translator()
    if japanese:
        output = trans.translate(data, dest='en').text
    else:
        output = trans.translate(data, dest='ja').text
    return output

if __name__ == '__main__':
    while True:
        data = input("> ")
        japanese = is_japanese(data)
        output = translate(data)
        print(output)
        getoutput("say {0}".format(output))
