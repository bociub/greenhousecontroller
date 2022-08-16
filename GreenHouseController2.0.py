import json
from random import randint, random
from numpy import sin

energyPlan = 0

def Switches(GH,energyPlan = energyPlan):
    if GH["InsideTemp"] < 20: 
        GH["AirHeaterRelay"] = True
        GH["AirHeaterCurrent"] = True 
    else:
        GH["AirHeaterRelay"] = False
        GH["AirHeaterCurrent"] = False
        
    if GH["WaterTemp"] < 15: 
        GH["WaterHeaterRelay"] = True
        GH["WaterHeaterCurrent"] = True
    else:
        GH["WaterHeaterRelay"] = False
        GH["WaterHeaterCurrent"] = False  
    if GH["InsideTemp"] >= 27:
        GH["FanRelay"] = True
        GH["FanCurrent"] = True
        GH["InsideTemp"] = GH["OutsideTemp"] 
     
    if (randint(0,energyPlan) - 1) > 0: #test7.py
        GH["LightRelay"] = True
        GH["LightCurrent"] = True
            
    return GH

def WeatherGenerator(initialTemp = randint(5,25)): #elevation+(24/180 sin (x)) * steepness ###temperature follows the pattern of a sin wave
                    #initialTemp random or if passed by keyword then the last hour of previous day(should be)
    steepness = randint(4,12) / 10 #random steepness
    sunshine = False
    weather = {}
    for hour in range(0,24):
        
        givenhour = hour * (24/180) #(whole hour as degree)
        temperature = sin(givenhour) * steepness * 10 + initialTemp # x^y parabola approach?
        
        if hour > 6 and hour < 20: #fixed daytime
            if randint(0,3) < 2:
                sunshine = True
            else: sunshine = False
        else: sunshine = False
        
        weather[hour+1] = [temperature,sunshine] 
        
    return weather #keys: 1-24 are hours and in list temperature[0] and sunshine[1] as values.
    
def GreenHouseInit():#according to plan!!!(figure of collection of variables)
    weather = WeatherGenerator()

    initialtemp = weather[1][0]
     
    GH = {"LightRelay" : False, "LightCurrent" : False,    
          "FanRelay" : False, "FanCurrent" : False,    
          "OutsideTemp" : initialtemp, #float, Outside temperature
          "InsideTemp" : initialtemp, #float, Inside temperature
          "LightSensor" : False,
          "AirHeaterRelay" : False, "AirHeaterCurrent" : False, 
          "WaterPumpCurrent" : True, 
          "WaterHeaterRelay" : False, "WaterHeaterCurrent" : False, 
          "WaterTemp" : 0, 
          "AirPumpCurrent" : True, 
          }
    GH["WaterTemp"] = GH["InsideTemp"] - randint(1,4)
    
    GH =  Switches(GH)   
    
    return GH, weather
    
def GreenHouseRun(days): #should return dict where days are ints and every value a dict with ebery hours' data + all days weather 
    GH = GreenHouseInit()
    weather = GH[1]
    GH = GH[0]
    data = {}
    for day in range(days):
        if weather[day + 1][1] == True: #if the weather sunny then inside temp increases by 3
            GH["InsideTemp"] += 3
        if GH["InsideTemp"] < GH["OutsideTemp"]: 
            GH["InsideTemp"] += ( GH["OutsideTemp"] - GH["InsideTemp"]) / 3
        if GH["WaterHeaterRelay"] == True:
            GH["WaterTemp"] += 1 
        if GH["WaterTemp"] < GH["InsideTemp"]:
            GH["WaterTemp"] += ( GH["InsideTemp"] - GH["WaterTemp"] ) / 3          
        data[day+1] = [Switches(GH), weather]
        weather = WeatherGenerator(weather[24][0])
    
    return data
y = 2
x = GreenHouseRun(y)

