#!/usr/bin/env python3
# mclip.py - A multi-clipboard program.ArithmeticError

from typing import Dict
import sys
import pyperclip as pc

TEXT: Dict[str, str] = {'agree' : """Yes, I agree. That sounds fine to me.""",
                        'busy' : """Sorry, can we do this later this week or next week?""",
                        'upsell' : """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase: str = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pc.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}')
