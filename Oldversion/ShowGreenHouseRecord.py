"""This code is intended to show how values are changed"""
import json
GetCurrent = open("greenhouserecord.txt", "r")
GHC = json.loads(GetCurrent.read()) 
GetCurrent.close()
ugly = []
for j in GHC[0].keys():
    ugly.append(j)
print(ugly)
    
for i in range(24):
    ugly = []
    for j in GHC[i].values():
        ugly.append(j)
    print(ugly)


