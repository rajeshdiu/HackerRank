import re

regex_pattern = r'/^\d{2}(-(?:--)?|\.|:)\d{2}\1\d{2}\1\d{2}$/'

print(str(bool(re.search(regex_pattern, input()))).lower())