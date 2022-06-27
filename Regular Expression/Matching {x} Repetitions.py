# You have a test string . Your task is to match the string hackerrank. This is case sensitive.

Regex_Pattern = r"^[a-zA-Z02468]{40}[\\s13579]{5}$"

import re

Test_String = input("Input String : ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))