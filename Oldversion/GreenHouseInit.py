"""This snipet creates an initial 
current state of an imagined greenhouse with auqaponics"""

import json


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
    dump = json.dumps(GH)
    f = open("greenhouse.txt", "w")
    f.write(dump)
    f.close()


from datetime import datetime 
CurrentDateTime = datetime.now()
CurrentHour = int(CurrentDateTime.strftime("%H")) # stores current hour as INT
