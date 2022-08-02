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


def WeatherGenerator(): #elevation+(24/180 sin (x)) * steepness 
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
                print("duck",hour)
            else: sunshine = False
        else: sunshine = False
        
        weather[hour+1] = [temperature,sunshine] 
        
    return weather
        
"""                           ### TEST OK ### returns with keys as hours and values as list: temperature and sunshine
                        x = WeatherGenerator()
                        for key in x:
                            print(key,x[key]) """







































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