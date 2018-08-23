#!/usr/bin/env python3

import unicodedata
from subprocess import getoutput
from googletrans import Translator

def translate(data):
    trans = Translator()
    detected = trans.detect(data)
    if detected.confidence < 1:
        return "can't detect, maybe " + detected.lang
    if detected.lang == "ja":
        output = trans.translate(data, dest='en').text
    else:
        output = trans.translate(data, dest='ja').text
    return output

if __name__ == '__main__':
    while True:
        data = input("> ")
        output = translate(data)
        print(output)
        #getoutput("say {0}".format(output))
