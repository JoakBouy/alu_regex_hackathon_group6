#!usr/bin/env python3
import re

text = "The movie is called Uncharted (2022)"

match = re.search(r"Title \((\d{4})\)", text)

if match:
    print(match.group(1))  # 2022
else:
    print("No match found")

