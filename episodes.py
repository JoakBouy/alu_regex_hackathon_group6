#!/usr/bin/env python
import re

text = "The episode is called Power S01E01: Pilot"

match = re.search(r"Power S(\d{2})E(\d{2}): (.+)", text)

if match:
    print("Season:", match.group(1))  # 01
    print("Episode:", match.group(2))  # 01
    print("Title:", match.group(3))  # Pilot
else:
    print("No match found")
