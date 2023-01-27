#!/usr/bin/env python3
import re


text = "ISBN 123-4-567-89012-3"

match = re.search(r"ISBN (\d{3}-\d-\d{3}-\d{5}-\d)", text)

if match:
    print(match.group(1))  # 123-4-567-89012-3
else:
    print("No match found")