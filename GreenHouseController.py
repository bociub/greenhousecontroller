import json
from random import randint, random
from numpy import sin



#labelling
CurrentDate = 1
CurrentHour = 1
Lastsync = 1

def Clock(): #artifical clock 1min = 1 hour
    pass

def SyncWithCloud():
    """
    If last sync is not the previous hour(minute in simulation):
    Fetch last sync and sync hour by hour to the current hour.
    
    """
    
    pass

def Switches(GH):
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
        
        
    return GH



def WeatherGenerator(): #elevation+(24/180 sin (x)) * steepness ###temperature follows the pattern of a sin wave
    initialTemp = randint(5,25) # initial temperature
    steepness = randint(4,8) / 10 #random steepness
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
        
    dump = json.dumps(weather)
    file = open("weather.txt", "w") 
    file.write(dump)
    file.close()
    
        
"""                           ### TEST OK ### returns with keys as hours and values as list: temperature and sunshine
                        x = WeatherGenerator()
                        for key in x:
                            print(key,x[key]) """

def GreenHouseInit():#according to plan!!!(figure of collection of variables)
    
    WeatherGenerator()
    file = open("weather.txt", "r") 
    weather = json.load(file) #getting back the weather data from the file.
    file.close()
    
    initialtemp = (weather["1"][0])
     
    
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
          "hour" : 1,
          "AllSunshine" : 0
          }
    GH["WaterTemp"] = GH["InsideTemp"] - randint(1,4)
    
    if initialtemp >= 27: #Switching off in GreenHouseRun
        GH["FanRelay"] = True
        GH["FanCurrent"] = True
    GH =  Switches(GH)   
        
        
    dump = json.dumps(GH)
    file = open("greenhousecurrent.txt", "w")
    file.write(dump)
    file.close()

"""GreenHouseInit()  ###TEST OK###
GreenHouseInit()
file = open("greenhousecurrent.txt", "r") 
weather = json.load(file) #getting back the weather data from the file.
file.close()
for key in weather:
    print(key,weather[key])
    """


def GreenHouseUpdate(hour):
    #GreenHouseInit()
    try:
        file = open("greenhousecurrent.txt", "r") 
        GHLast = json.load(file) #getting back the weather data from the file.
        file.close()
        
        file = open("weather.txt", "r") 
        DailyWeather = json.load(file) #getting back the weather data from the file.
        file.close() 
    except:
        print("missing initial data : greenhousecurrent.txt or weather.txt")
    
    
    GHNew = GHLast.copy() #to be comperable
    
    LastRecordedHour = GHLast["hour"]
    
    hour = str(hour + 1) 
    CurrentWeather = DailyWeather[hour] ###LISTLISTLIST
    
    GHNew["OutsideTemp"] = CurrentWeather[0]
    
    GHNew["LightSensor"] = CurrentWeather[1]
    
    GHNew["hour"] = GHLast["hour"] + 1
    
    if GHNew["LightSensor"] == True:
        GHNew["AllSunshine"] += 1

    if CurrentWeather[1] == True:
        GHNew["InsideTemp"] += 3
        
    if GHNew["InsideTemp"] < GHNew["OutsideTemp"] and GHNew["FanRelay"] != True:
       GHNew["InsideTemp"] += ( GHNew["OutsideTemp"] - GHNew["InsideTemp"]) / 3
                  
    if GHLast["WaterHeaterRelay"] == True:
        GHNew["WaterTemp"] += 3  
        
    if GHNew["WaterTemp"] < GHNew["InsideTemp"]:
        GHNew["WaterTemp"] += ( GHNew["InsideTemp"] - GHNew["WaterTemp"] ) / 3
        
        

    GHNew = Switches(GHNew)
    
    dump = json.dumps(GHNew)
    file = open("greenhousecurrent.txt", "w")
    file.write(dump)
    file.close()



""" TEST LOOKS OK -> go to sleep
GreenHouseInit()
file = open("greenhousecurrent.txt", "r") 
weather = json.load(file) #getting back the weather data from the file.
file.close()
for key in weather:
    print(key,weather[key])

GreenHouseUpdate(3)
file = open("greenhousecurrent.txt", "r") 
weather = json.load(file) #getting back the weather data from the file.
file.close()
for key in weather:
    print(key,weather[key])
"""


def GreenHouseRun():
    pass


    










"""def WeatherGeneratorOLD():#A single day's weather generator
    sunlight = False
    temperature = randint(0,27)
    Weather = {}
    for i in range(24): #i means a given hour   
             
        if i < 6 or i > 20:
            x = randint(0,3)
            if x < 2:
                sunlight = False
        else: sunlight = True  
          
        if i < 6 or i > 20:
            temperature -= randint(0,1)
            if sunlight == True:
                temperature += 2
                print("duck")
        else: temperature -= randint(0,1)                
        Weather[i+1] = [temperature,sunlight]   
        
    return Weather
        
        
Weather = WeatherGeneratorOLD()
for key in Weather:
    print(key,Weather[key])            
            
            
     #   Weather.i = [temperature,sunlight]
        #dumptofile"""