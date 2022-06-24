# import textwrap

# def wrap(string, max_width):
#     return 
    
# string=str(input())
# max_width=int(input())

# print(textwrap.fill(string,max_width))

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)