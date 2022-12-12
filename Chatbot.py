import time
import webbrowser
import pwinput

 
def fastfood():
  global FoodChoice 
  FoodChoice = "fastfood"
  locations()
  budget()
  conclusion()
  

def indian():
  global FoodChoice
  FoodChoice = "indian"
  locations()
  budget()
  conclusion()


def pizza():
  global FoodChoice
  FoodChoice = "pizza"
  locations()
  budget()
  conclusion()


def chinese():
  global FoodChoice
  FoodChoice = "chinese"
  locations()
  budget()
  conclusion()


def locations():
  time.sleep(1.5) # pauses the program for a set amount of time
  print("\n============================================")
  print("= << WHERE WOULD YOU LIKE TO EAT TODAY? >> =")
  print("=============================================")
  print("=                                           =")
  print("=            1)- Portsmouth.               =")
  print("=                                          =")
  print("=            2)- Havant.                   =")
  print("=                                          =")
  print("=            3)- Waterloovile.             =")
  print("=                                          =")
  print("=            4)- Purbrook.                 =")
  print("=                                           =")
  print("============================================")
  global LocationChoice
  LocationChoice = input(f"\n>> Enter option: ")
  LocationChoiceInputs = ["1","2","3","4"] # vaild options from 1-4
  while LocationChoice not in LocationChoiceInputs: # check input is valid from 1-4
      print("Unknown input\n")
      LocationChoice = input(">>")
  LocationChoiceOptions = {"1": "Portsmouth","2": "Havant","3": "Waterloovile","4": "Purbrook"} # get the names of the options
  LocationChoice = LocationChoiceOptions[LocationChoice]
  

  

def budget():
  time.sleep(1.5) # pauses the program for a set amount of time
  print("\n=============================================")
  print("= << WHAT WOULD YOU LIKE TO SPEND TODAY? >> =")
  print("=============================================")
  print("=                                           =")
  print("=               1)- 10-15$.                 =")
  print("=                                           =")
  print("=               2)- 20-25$.                 =")
  print("=                                           =")
  print("=               3)- 30-35$.                 =")
  print("=                                           =")
  print("=               4)- 40-100$.                =")
  print("=                                           =")
  print("=============================================")
  global BudgetChoice
  BudgetChoice = input(f"\n>> Enter option: ")
  BudgetChoiceInputs = ["1","2","3","4"] # vaild options from 1-4
  while BudgetChoice not in BudgetChoiceInputs: # check input is valid from 1-4
      print("Unknown input\n")
      BudgetChoice = input(">>")
  BudgetChoiceOptions = {"1": "10-15$","2": "20-25$","3": "30-35$","4": "40-100$"} # get the names of the options
  BudgetChoice = BudgetChoiceOptions[BudgetChoice]




def conclusion():
  budgetChoice = BudgetChoice.replace("$", "")
  RestaurantFound = False
  searchfile = open("Restaurants.txt", "r") # open the file for reading
  for line in searchfile: # for every line in the file
    if f"{FoodChoice} {LocationChoice} {budgetChoice}" in line: # search the file for a restaurant matching the inputs
      RestaurantFound = True
      data = line.split() # split the line into a list of words
      restaurantName = data[3] # get the restaurant name
      restaurantWebsite = data[4] # get the restaurant website
      restaurantName = restaurantName.replace("_", " ")
      time.sleep(1.4)
      print("\n=============================================")
      print("=         << RESTAURANT FOUND! >>           =")
      print("=============================================")
      print("                                           ")
      print(f"         Food Type: {FoodChoice}            ")
      print("                                              ")
      print(f"         Name: {restaurantName}             ")
      print("                                           ")
      print(f"         Location: {LocationChoice}         ")
      print("                                           ")
      print(f"         Budget: ${budgetChoice}            ")
      print("                                            ")
      print("=============================================")
      print("\nWould you like to go to this restaurants website? (Y,N): ")
      ConclusionChoice = input(f">> Enter option: ").upper()
      ConclusionChoiceInputs = ["Y", "N"]
      if ConclusionChoice == "Y":
          webbrowser.open(restaurantWebsite) # open the website in the default browser
      while ConclusionChoice not in ConclusionChoiceInputs: # check input is valid from 1-4
        print("Unknown input\n")
  if RestaurantFound == False:
    print("!\nNo restaurants found, please try again.\n!")
      
  searchfile.close() # close the file after looking for a restaurant
  

  #searchfile.close() # close the file after looking for a restaurant
  #time.sleep(1.4)
  #print("\nWould you like to go to this restaurants website? (Y,N) ")
  #ConclusionChoice = input(">> Enter option: ").upper()
  #if ConclusionChoice == "Y":
    #webbrowser.open(restaurantWebsite) # open the website in the default browser
  #elif ConclusionChoice == "N":
      #print("Sending you back to home page.")
      #time.sleep(1.4)
      #welcome()
  #else:
    #print("\nUnknown input")
    #time.sleep(1.4)
  #if RestaurantFound == False:
    #print("!\nNo restaurants found, please try again.\n!")



def foodChoiceOptions():
  time.sleep(1.5) # pauses the program for a set amount of time
  print("\n=============================================")
  print("=  << WHAT WOULD YOU LIKE TO EAT TODAY? >>  =")
  print("=============================================")
  print("=                                           =")
  print("=              1)- fastfood.                =")
  print("=                                           =")
  print("=              2)- indian.                  =")
  print("=                                           =")
  print("=              3)- pizza.                   =")
  print("=                                           =")
  print("=              4)- chinese.                 =")
  print("=                                           =")
  print("=============================================")
  global FoodChoice
  FoodChoice = input(f"\n>> Enter option: ")
  if FoodChoice == "1": 
    fastfood() # calls fastfood functions
  elif FoodChoice == "2": 
    indian() # calls indian functions
  elif FoodChoice == "3":
    pizza() # calls pizza functions
  elif FoodChoice == "4":
    chinese() # calls chinese functions
  else:
    print("\nPlease enter a valid option.")
    time.sleep(1.4) # pauses the program for a set amount of time
    foodChoiceOptions() # calls foodchoiceoptions functions



def login():
    time.sleep(1.4) # pauses the program for a set amount of time
    print("\n=============================================")
    username = input("= Please enter your username: ")
    print("")
    password = pwinput.pwinput(prompt='= Please enter your password: ', mask = "*" ) # makes password hidden when written out
    print("=============================================")
    #for line in open("Accountfile.txt","r").readlines(): # Read the lines
        #login_info = line.split() # Split on the space, and store the results in a list of two strings
        #if username == login_info[0] and password == login_info[1]:
    accountFound = False
    searchFile = open("Accountfile.txt", "r")
    for line in searchFile:
        if f"{username} {password}" in line:
            accountFound = True
            time.sleep(1.4) # pauses the program for a set amount of time
            print("\n=============================================")
            print("Checking details, please hold.")
            time.sleep(3.0) # pauses the program for a set amount of time
            print("\nCorrect credentials!")
            print("=============================================")
            time.sleep(1.4) # pauses the program for a set amount of time
            foodChoiceOptions()
    if accountFound == False:
      print("Checking details, please hold.")
      time.sleep(4.0) # pauses the program for a set amount of time
      print("Incorrect credentials.")

def register():
  time.sleep(1.4) # pauses the program for a set amount of time
  print("\n============================================")
  usernameRegister = input("= Please input your username: ")
  print("")
  passwordRegister = pwinput.pwinput(prompt='= Please enter your password: ', mask = "*" ) # makes password hidden when written out
  print("============================================")
  file = open("Accountfile.txt","a")
  file.write(usernameRegister) # stores username in file
  file.write(" ")
  file.write(passwordRegister) # stores password in file
  file.write("\n") # makes user details appear under any other users in file
  file.close() # closes file
  if login():
      print("\nYou are now logged in...")
      time.sleep(1.4) # pauses the program for a set amount of time
      foodChoiceOptions()
  else:
      print("\nYou aren't logged in!")
      welcome()

def quit_program():
      time.sleep(1.4) # pauses the program for a set amount of time
      print("\n============================================")
      print("Quitting the chatbot, please wait.")
      time.sleep(2.4) # pauses the program for a set amount of time
      print("\nThanks for using the foodbot, have a great day.")
      print("============================================")
      time.sleep(3.0) # pauses the program for a set amount of time


############################
# main program starts here #
############################


def welcome():
    
    print("=============================================")
    print("=  << WELCOME TO THE BRYNDEENY FOODBOT! >>  =")
    print("=                                           =")
    print("=  << Please enter the following number >>  =")
    print("=============================================")
    print("=                                           =")
    print("=              1)- login.                   =")
    print("=                                           =")
    print("=              2)- register.                =")
    print("=                                           =")
    print("=              3)- exit.                    =")
    print("=                                           =")
    print("=============================================")
    choice = input(f"\n>> Enter option: ")
    if choice == "1":
      login()
    elif choice == "2":
      register()
    elif choice == "3":
      quit_program()
    else:
        print("\nPlease enter a valid option.")
        time.sleep(1.4) # pauses the program for a set amount of time
        print(" ")
        welcome()
welcome()


