#!/usr/bin/env python3

import unicodedata
from subprocess import getoutput
from googletrans import Translator
import signal
import sys
import subprocess

class Translate:

    def translate(self, data):
        trans = Translator()
        detected = trans.detect(data)
        if detected.confidence < 1:
            return "can't detect, maybe " + detected.lang
        if detected.lang == "ja":
            output = trans.translate(data, dest='en').text
        else:
            output = trans.translate(data, dest='ja').text
        return output

def handler(signal, frame):
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handler)
    while True:
        data = input("> ")
        if data == ':clear':
            subprocess.call('clear')
            continue
        t = Translate()
        output = t.translate(data)
        print(output)

if __name__ == '__main__':
    main()
