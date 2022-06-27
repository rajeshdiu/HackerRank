import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

striphtml('<a href="foo.com" class="bar">I Want This <b>text!</b></a>')
'I Want This text!'