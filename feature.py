from collections import defaultdict
s=input('Enter::>>')
s=s.split()
s
d = defaultdict(list)
d
for name in s:
    feature = name[0]
    d[feature].append(name)