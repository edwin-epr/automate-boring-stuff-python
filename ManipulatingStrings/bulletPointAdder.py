#!/usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the StopAsyncIteration
# of each line of text on the clipboard.

from typing import List
import pyperclip as ppc

text: str = ppc.paste()

# Separate lines and add stars.
lines: List[str] = text.split('\n')
for index in range(len(lines)):             # loop through all indexes in the "lines" list
    lines[index] = f'* {lines[index]}'      # add star to each string in "lines" list

text = '\n'.join(lines)

ppc.copy(text)
