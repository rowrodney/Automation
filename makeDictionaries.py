data = { 'red' : 1, 'green' : 2, 'blue' : 3 }

def makedict(**kwargs):
    return kwargs
data = makedict(red=1, green=2, blue=3)
print(data)

def dodict(*args, **kwds):
    d = {}
    for k, v in args: d[k] = v
    d.update(kwds)
    return d
tada = dodict(yellow=2, green=4, *data.items())
print(tada)
