#!/usr/bin/env python3
import re

text = "[Verse 1] some lyrics"

match = re.search(r"\[Verse (\d)\] (.*)", text)

if match:
    print(match.group(1))  # 1
    print(match.group(2))  # some lyrics
else:
    print("No match found")