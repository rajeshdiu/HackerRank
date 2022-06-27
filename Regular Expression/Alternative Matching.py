import re

regex_pattern = r'^(Mr?s|[MDE]r)\.[a-zA-Z]+$'

print(str(bool(re.search(regex_pattern, input()))).lower())