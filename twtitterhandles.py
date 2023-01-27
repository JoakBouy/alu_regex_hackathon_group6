#!/usr/bin/env python3
import re

text = "@username"

match = re.search(r"@([A-Za-z0-9]+)", text)

if match:
    print(match.group(1))  # username
else:
    print("No match found")