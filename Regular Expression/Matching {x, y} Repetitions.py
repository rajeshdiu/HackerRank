# You have a test string . Your task is to match the string hackerrank. This is case sensitive.

Regex_Pattern = r"^\\d{1,2}[a-zA-Z]{3,}\\.{0,3}$"

import re

Test_String = input("Input String : ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))