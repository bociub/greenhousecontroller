import json
from random import randint, random
from numpy import sin



#labelling
CurrentDate = 1
CurrentHour = 1
Lastsync = 1

def SyncronWithCloud():
    """
    If last sync is not the previous hour(minute in simulation):
    Fetch last sync and sync hour by hour to the current hour.
    
    """
    
    pass


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

def GreenHouseInit():
    
    WeatherGenerator()
    file = open("weather.txt", "r") 
    weather = json.load(file) #getting back the weather data from the file.
    file.close()
    
    initialtemp = (weather["1"][0])
    
    GH = {"LightRelay" : 0, "LightCurrent" : 0,    # Zero means device is off or no signal
          "FanRelay" : 0, "FanCurrent" : 0,    # Zero means device is off or no signal
          "OutTemp" : initialtemp, #INT, Outside temperature
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



GreenHouseInit()

































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