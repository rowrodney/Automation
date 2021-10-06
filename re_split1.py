line = ' asdf; fdjkd, fekkeke, foo '
import re
re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
values=fields[::2]
delimiters=fields[1::2] + ['']
re.split(r'(?:,|;|\s)\s*', line)

