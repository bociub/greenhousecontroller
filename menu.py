import GreenHouseController
import requests
import json

"""
first test user:
    username: ducky
    pw:ducky
    email: ducky@ducky.com
    user id : 6
    """
access_token = 0
refresh_token = 0

def LogIN(email = "ducky@ducky.com" , pw = "ducky"): #keyword arguments set for test purposes
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
        print("connection failure: ",error)
    
    tokens = str(login.json()) #set the tokens as string
    tokens = tokens.replace("\'", "\"") #replace() to be a valid json format > the sersver's answer
    tokens = json.loads(tokens)  #going to be a python variable
    return tokens

    #access_token = tokens["access_token"]
    #refresh_token = tokens["refresh_token"]

print( LogIN(), type(LogIN()), LogIN()  )

def LogOut():
    pass

def LoggedIN():
    pass
    #cheks if the user logged into the server and returns with true or false
    
def ReportAnHour():
    pass


def MainMenu():
    print("#" * 20) 
    print("#    MAIN MENU     #")
    print("#" * 20)
    if LoggedIN() == False: 
        print("1: Log in to the cloud") 
        print("2: Register a greenhouse")
    else: 
        print("1: Log out from the cloud") 
        print("2: Report a specific hour to the server") 
    print("3: Show a specific hour's data") 
    print("4: reinitializing the greenhouse and the weather") 
    print("5: Generateing a new 24 hour periods data") 
       




"""
while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
"""