dict = { 1 : [ 2 , 3 ]}
list = dict[1]
print(dict)
print(list)

import json

dump = json.dumps(dict)
load = json.loads(dump)

print(load)