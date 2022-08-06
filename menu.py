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
tokensdict = {}

LoggedIN = False

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
        print("duck123234")
        return ("connection failure: ",error)
    
    tokens = str(login.json()) #make sure server's answer a string
    tokens = tokens.replace("\'", "\"") #replace() to be a valid json format > the sersver's answer
    tokens = json.loads(tokens)  #going to be a python variable

    LoggedIN = True
    print("duck432423")
    tokensdict = tokens

    #access_token = tokens["access_token"]
    #refresh_token = tokens["refresh_token"]


def Registration(email = "ducky1@ducky.com" , pw = "ducky1", username = "ducky1"):
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
    
def LogOut():
    global LoggedIN
    global tokensdict
    LoggedIN = False
    tokensdict = {}

#def LoggedIN():
#    pass
#    #cheks if the user logged into the server and returns with true or false
    
def ReportAnHour():
    pass

def read_user_choice(): #stolen function from edube.org.
    ok = False
    while not ok:
        answer = input("Enter your choice (0..4): ")
        ok = answer in ['0', '1', '2', '3', '4']
        if ok:
            return answer
        print("Bad choice!")  
def LogINSub():
    print("#" * 20) 
    print("#      Log In      #")
    print("#" * 20)
    email = input("email: ")
    pw = input("password: ")   
    LogIN(email=email, pw=pw)
    
def RegSub():
    print("#" * 20) 
    print("#   Registration   #")
    print("#" * 20)
    username = input("Username: ")
    email = input("email: ")
    pw = input("password: ")
    Registration(username=username, email=email, pw=pw)
    
    
def MainMenu():
    #global LoggedIN

    
    
    print("#" * 20) 
    print("#    MAIN MENU     #")
    print("#" * 20)
    if LoggedIN == False: 
        print("1: Log in to the cloud") 
        print("2: Register a greenhouse")
    else: 
        print("3: Log out from the cloud") 
        print("4: Report a specific hour to the server") 
        print("5: Show a specific hour's data") 
    print("6: reinitializing the greenhouse and the weather") 
    print("7: Generateing a new 24 hour periods data") 
    choice = read_user_choice()
    if choice == '1':
        LogINSub()
        MainMenu()
    elif choice == '2':
        RegSub()
        MainMenu()
    elif choice == '3':
        LogOut()
        MainMenu()
    else:
        print("bye")
  
MainMenu()



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