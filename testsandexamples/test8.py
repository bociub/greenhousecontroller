def GH():
    house = {}
    weather = {1: 15.6, 2: 16.7, 3: 17.8} 
    data = {}
    for hour in range(1,4):        
        house["Temperature"] = weather[hour]
          
        data[hour] = [house.copy(), weather[hour]] #adding copy() solves the issue. 
              
        for key in data:
            print(key, data[key])           
        print("#############################")            
    return data
GH()
"""
The "hour" from the for loop is the key of the dictionary. 
In every cycle it adds a new element to the dictionary, however,
 it overwrites every earlier element as well which are not addressed.
 I am not able to understand why the last value 
 of "weather" updates every single "Temperature" 
 in the "data" dictionary... Should not do that. 
"""
