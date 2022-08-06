test = 3
def duck(): #>>>one global / block!

    global test
    test = 4
    print(test)
    
print(test)    
duck()
print(test)