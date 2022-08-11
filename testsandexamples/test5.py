import json

d1 = {"as d" : 3}
d2 = {'as d' : 4}

x=json.dumps(d2)
print(x, type(x))
x = json.loads(x)
print(x, type(x))

