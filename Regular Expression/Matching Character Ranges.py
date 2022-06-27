# You have a test string . Your task is to match the string hackerrank. This is case sensitive.

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

import re

Test_String = input("Input String : ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))