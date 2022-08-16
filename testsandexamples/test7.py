from random import randint
x = 3
ct = 0
cf = 0
    
for i in range(100000):
    y = randint(0,x)
    z = y - 1
    
    if z > 0:
        ct += 1
    else:
        cf += 1    
    
print("true:" , ct)
print("false", cf)

#x in range 1-10
#not too sophisticated but works