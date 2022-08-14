
import GreenHouseController
import requests
import json

tokensdict = {}
LoggedIN = False
ID = {}

def Registration(email = "ducky@ducky.com" , pw = "ducky", username = "ducky"): # available from the controller only for test purposes

    email = str(email)
    pw = str(pw) #to be sure it is handled as a string
    username = str(username)
    jsondict = {}
    jsondict["email"] = email
    jsondict["password"] = pw
    jsondict["username"] = username
    try:
        signup = requests.post('http://localhost:5000/users' ,
                              headers= {'Content-Type': 'application/json'},
                              json = jsondict)
        print("Message from the server:")
        print(signup.json())
        print()
    except requests.exceptions.RequestException as error:
        print("duck94859")
        return ("connection failure: ",error)

def LogIN(email = "ducky@ducky.com" , pw = "ducky"): #keyword arguments set for test purposes
    global LoggedIN
    global tokensdict
    email = str(email)
    pw = str(pw) #to be sure it is handled as a string
    jsondict = {}
    jsondict["email"] = email
    jsondict["password"] = pw
    try:
        login = requests.post('http://localhost:5000/token' ,
                              headers= {'Content-Type': 'application/json'},
                              json = jsondict)

    except requests.exceptions.RequestException as error:

        LoggedIN = False
        
        return ("connection failure: ",error)
    
    except Exception as error:
        print("duck123234", error)
    
    
    tokens = str(login.json()) #make sure server's answer a string
    tokens = tokens.replace("\'", "\"") #replace() to be a valid json format > the sersver's answer
    tokens = json.loads(tokens)  #going to be a python variable(from string to dict)

    if 'message' in tokens:
        print(">>>>>> ", tokens["message"] ," <<<<<<<")
    else:
        LoggedIN = True
    print("duck432423")
    tokensdict = tokens
    print("LogIN" ,login)

def GetID():    
    global ID
    headers = {'Authorization': 'Bearer ' + tokensdict["access_token"]}
    try:
        userdict = requests.get('http://localhost:5000/me' ,                              
                              headers = headers)
        
        
        ID = userdict.json() #makes a dictionary.
    except requests.exceptions.RequestException as error:
        print("duck94679")
        return ("connection failure: ",error) 
    except Exception as error: print("BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", error)
    print("GetID" ,userdict)
    
def ModifyUserDB(): # available from the controller only for test purposes
# variables must be in syncron in the sent data and over there. if not then nothing happens.
    
    headers = {'Authorization': 'Bearer ' + tokensdict["access_token"], 'Content-Type': 'application/json'}
    userdict = {}
    userdict["seedingDate"] = "2022-09-11 00:03:15.12345"
    userdict["postCode"] = "123123"
    userdict["energyPlan"] = 5


    
    
    try:
        userdict = requests.put('http://localhost:5000/me' ,  #why this variable name?                            
                              headers = headers ,
                              json = userdict )
        

    except requests.exceptions.RequestException as error:
        print("duck90979")
        return ("connection failure: ",error) 
    except: print("quack123234")
    
    print("ModifyUserDB", userdict)
    
def SendRecords(): #/greenHouseS 

    headers = {'Authorization': 'Bearer ' + tokensdict["access_token"], 'Content-Type': 'application/json'}
    ghdict = {}

    ghdict["bookedForSale"] = True
    ghdict["recordDateTime"] = '2021-01-11 11:03:15.12345'
    ghdict["LightRelay"] = True
    ghdict["LightCurrent"] = True
    ghdict["FanRelay"] = True
    ghdict["FanCurrent"] = True
    ghdict["OutsideTemp"] = 456
    ghdict["InsideTemp"] = 345
    ghdict["Lightsensor"] = True
    ghdict["AirheaterRelay"] = True
    ghdict["AirHeaterCurrent"] = True
    ghdict["WaterPumpCurrent"] = True
    ghdict["WaterHeaterRelay"] = True
    ghdict["WaterHeaterCurrent"] = True
    ghdict["WaterTemp"] = 234
    ghdict["AirPumpCurrent"] = True

    

    
    try:
        details = requests.post('http://localhost:5000/greenHouseS' ,                              
                              headers = headers ,
                              json = ghdict )

    except requests.exceptions.RequestException as error:
        print("duck44979")
        return ("connection failure: ",error) 
    except Exception as error:
        print("quack123564", error)

    print("SendRecords:", details)

#Registration()
LogIN()
GetID()

ModifyUserDB()
#
SendRecords()

