regex_pattern = r"...\....\....\....$"

import re
import sys

Test_String = input("Input String : ")

match = re.match(regex_pattern, Test_String) is not None

print(str(match).lower())