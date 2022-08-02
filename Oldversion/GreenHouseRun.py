"""This code creates a 24 hours state and updates currentstate of 
an imagined greenhouse with auqaponics and dumps as JSON into a text file"""
import json
from random import randint

#from datetime import datetime 
#CurrentDateTime = datetime.now()
#Hour = int(CurrentDateTime.strftime("%H")) # stores current hour as INT

#dumps into greenhouse.txt
def JDump(GH):
    dump = json.dumps(GH)
    f = open("greenhouse.txt", "w")
    f.write(dump)
    f.close()

#creates the initial state of the greenhouse.txt
def GreenHouseInit():
    GH = {"LightRelay" : 0, "LightCurrent" : 0,    # Zero means device is off or no signal
          "FanRelay" : 0, "FanCurrent" : 0,    # Zero means device is off or no signal
          "OutTemp" : 25, #INT, Outside temperature
          "InTemp" : 23, #INT, Inside temperature
          "LightSensor" : 1, # Zero means device is off or no signal
          "AirHeaterRelay" : 0, "AirHeaterCurrent" : 0, # Zero means device is off or no signal
          "WaterPumpCurrent" : 1, # Zero means device is off or no signal
          "WaterHeaterRelay" : 0, "WaterHeaterCurrent" : 0, # Zero means device is off or no signal
          "WaterTemp" : 20, #INT, Outside temperature
          "AirPumpCurrent" : 1 # Zero means device is off or no signal
          }
    
    JDump(GH)

    
#Loads the current state from greenhouse.txt.
def CurrentState ():
    GetCurrent = open("greenhouse.txt", "r")
    GreenHouseCurrent = json.loads(GetCurrent.read()) 
    GetCurrent.close()
    return GreenHouseCurrent


#Modifies the values in current state of greenhouse.txt for next dump (into greenhouserecord.txt
#Current sensors and  light sensor are not set yet
def ModifyCurrentState (Hour):
    CS = CurrentState()
    Hour = int(Hour)
    if Hour > 5 and Hour < 17:
        CS["OutTemp"] += randint(0,1)
        CS["InTemp"] += randint(0,1)
        CS["LightSensor"] = 1

    else:
        CS["OutTemp"] -= randint(0,1)
        CS["InTemp"] -= randint(0,1)
        CS["LightSensor"] = 0

    if CS["InTemp"] > 27: CS["FanRelay"] = 1
    else: CS["FanRelay"] = 0
    
    if CS["InTemp"] < CS["WaterTemp"] and CS["InTemp"] < 20: CS["AirHeaterRelay"] = 1
    else: CS["AirHeaterRelay"] = 0
    
    if CS["WaterTemp"] < 23 and CS["WaterTemp"] < 15: CS["WaterHeaterRelay"] = 1
    else: CS["WaterHeaterRelay"] = 0
 
    JDump(CS)



 #creates a list with 24 elements. each element is a representation of a current state in a given hour.     
def AppendRecord():
    #checks if current exist opens if exist if not then runs greenhouseinit
    try:
        GetCurrent = open("greenhouse.txt", "r")
        GetCurrent.close()
    except:
        GreenHouseInit()
        
    HourlyRecord = []
    for i in range(24):
        HourlyRecord.append(CurrentState())        
        ModifyCurrentState(i)
    dump = json.dumps(HourlyRecord)
    f = open("greenhouserecord.txt", "w")
    f.write(dump)
    f.close()
    
AppendRecord()


 
