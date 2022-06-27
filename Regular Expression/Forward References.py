
Regex_Pattern = r'^tac(tac(tic)?)*$'

import re
from tkinter.tix import Tree

Test_String = input("Input String :")

if re.findall(Regex_Pattern, Test_String)==True:
    print("True")
else:
    print("False")
