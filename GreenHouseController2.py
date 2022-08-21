
from random import randint
from numpy import sin

energyPlan = 0




def Switches(GH,energyPlan = energyPlan):
    if GH["InsideTemp"] < 20: 
        GH["AirheaterRelay"] = True
        GH["AirHeaterCurrent"] = True 
    else:
        GH["AirheaterRelay"] = False
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
        
        if initialTemp > 30: initialTemp -= 2
        if initialTemp < 5: initialTemp += 2 #to deal with the evil randint.
            
        givenhour = hour * (24/180) #(whole hour as degree)
        temperature = sin(givenhour) * steepness * 10 + (initialTemp + randint(-2,2) + (1/0.99999)) #aganist the floatdrift of temperature
        if hour > 6 and hour < 20: #fixed daytime
            if randint(0,3) < 2:
                sunshine = True
            else: sunshine = False
        else: sunshine = False
        
        weather[hour+1] = [temperature,sunshine] 
    #weather[24] = weather[1]    #this makes the days too same
    weather[24][0] = int(weather[24][0]) #this alsi makes the days the too same. initialtemp should be hacked with randint, however at least does not let the glass melt on day 1000, because of float shift.
    
    return weather #keys: 1-24 are hours and in list temperature[0] and sunshine[1] as values.
    
def GreenHouseInit():#according to plan!!!(figure of collection of variables)
    weather = WeatherGenerator()

    initialtemp = weather[1][0]

    GH = {"LightRelay" : False, "LightCurrent" : False,    
          "FanRelay" : False, "FanCurrent" : False,    
          "OutsideTemp" : initialtemp, #float, Outside temperature
          "InsideTemp" : initialtemp, #float, Inside temperature
          "Lightsensor" : False,
          "AirheaterRelay" : False, "AirHeaterCurrent" : False, 
          "WaterPumpCurrent" : True, 
          "WaterHeaterRelay" : False, "WaterHeaterCurrent" : False, 
          "WaterTemp" : 0, 
          "AirPumpCurrent" : True, 
          }
    GH["WaterTemp"] = GH["InsideTemp"] - randint(1,4)

    
    GH =  Switches(GH)   
    
    return GH, weather
    

def GreenHouseRun(days): #should return dict where keys are days+hours  and every values are the consecvent hour's data.
    GH = GreenHouseInit() #tuple

    weather = GH[1] 
    GH = GH[0]

 
    datadays = {}
    datahours = {}
    
    for day in range(days):
        
        for hour in range(24):
       
            if weather[hour + 1][1] == True: #if the weather sunny then inside temp increases by 2
                GH["InsideTemp"] += 2
            if GH["InsideTemp"] < GH["OutsideTemp"]: 
                GH["InsideTemp"] += ( GH["OutsideTemp"] - GH["InsideTemp"]) / 3
            if GH["WaterHeaterRelay"] == True:
                GH["WaterTemp"] += 1 
            if GH["WaterTemp"] < GH["InsideTemp"]:
                GH["WaterTemp"] += ( GH["InsideTemp"] - GH["WaterTemp"] ) / 3
                
            GH["weather"] =  weather[1 + hour].copy()  #adding current weather to GH as list
            datahours[hour+1] = Switches(GH).copy()  #adding gh data
          
            GH["OutsideTemp"] = weather[1 + hour][0] 
               

        weather = WeatherGenerator(weather[24][0])
        datadays[day] = datahours.copy()
        
        
        
    return datadays

if __name__ == "__main__":
    x = GreenHouseRun(2)
    
    
    print(x)
    for key in x:
        print(key)
        for key2 in x[key]:
            print(key2)
            print(x[key][key2])


