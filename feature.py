from collections import defaultdict
#s=input('Enter::>>')
s=s.split()
s
d = defaultdict(list)
d
for name in s:
    feature = name[0]
    d[feature].append(name)
    
for i in d['e']:
    if '.' in i:
        print(i.split('.')[0].upper(),end=',')

for i in d['F']:
    if 'FSI' in i:
        print(i.split(':')[2],end=',')
