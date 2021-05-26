#Author: Michael Nwachukwu
#Date last revised: 4/29/2021
#---------------------------------------------
#register
# - First name, last name, email, password
# - generate user id


# login
# - account number, password

#Import datetime class from datetime module
from datetime import datetime
#import random module to generate random numbers
import random
import validation
import database
from getpass import getpass 

database1 = {1234567890: 
          ["Mike", "Nwachukwu", "minlite27@gmail.com", "password", 10]} 
#database of type dictionary to hold user information

def init():

    print("Welcome to Bank ReskillLMS")
    dateAndTime = datetime.now()
    print("Today's date and time: ", dateAndTime.strftime("%m/%d/%y %I:%M %p")) #format the date to be mm/dd/yy and time to be mm:hh AM/PM
       
    haveAccount = int(input("Do you have an account with us?\n 1 (yes) 2 (no): "))

    if(haveAccount == 1 and database1):
        login()
    elif(haveAccount == 1 and not database1):
        print("No users in database, please register")
        register()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("-------- Login --------")

    global accountNumberFromUser

    accountNumberFromUser = input("What is your account number?\n")

    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)
   
    if is_valid_account_number:
        try:
            
            password = getpass("what is your password?\n")
            if not password:
                raise ValueError("Password is a required field")
        except ValueError as e:
            print(e)

        user = database.authenticatedUser(accountNumberFromUser, password)
        if user:
            database.userLoginStatus(accountNumberFromUser)
            bankOperation(user)
                
        # for accountNumber,userDetails in database.items():
        #     if(accountNumber == int(accountNumberFromUser)):
        #         if(userDetails[3] == password):
        #             bankOperation(userDetails)
        #         else:
        #             print("Invalid Password, try again.\n")
        #             init()
        else:
            print("Invalid account, please try again\n")
            init()
    else:
        print("account number invalid: check that you have 10 digits")
        init()
        
     
    
def register():

    print("-------- Register --------")

    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = getpass("Create a password\n")


    accountNumber = generateAccountNumber()

    #database[accountNumber] = [first_name, last_name, email, password, 0] 
    #the zero value (last value for the key) will represent the user's balance
     
    is_user_created = database.create(accountNumber, first_name, last_name, email, password)
    # using database module to create a new record
    # create a file
    if is_user_created:
        print("Your account has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is %d" % accountNumber)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")
        
        login()
    else:
        print("Something went wrong, please try again")
        register()

def bankOperation(user):
    
    print("Welcome %s %s\n" % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdraw (3) Logout (4) Complaint (5) Exit\n"))

    if(selectedOption == 1):
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawOperation(user)
    elif(selectedOption == 3):
        database.userLogOut(accountNumberFromUser)
        login() #return user to log in
    elif(selectedOption == 4):
        complaint(user)
    elif(selectedOption == 5):
        database.userLogOut(accountNumberFromUser)
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawOperation(user):
    print("-------- Withdraw --------\n")

    currentBalance = int(getCurrentBalance(user))
    print("Your balance is %s\n" % "${:,.2f}".format(currentBalance))
    if (currentBalance == 0):
        print("insufficient funds\n(You should make a deposit first).\nReturning to menu\n")
        bankOperation(user)
    else:
        withdrawAmount = input("How much would you like to withdraw?\n")
        is_valid_withdraw_amount = validation.money_validation(withdrawAmount)  

        if is_valid_withdraw_amount:
            
            withdrawAmount = int(withdrawAmount)

            while withdrawAmount > currentBalance:
                print("Insuffient funds, you only have %s left in your account. Enter new amount\n" % "${:,.2f}".format(currentBalance))
                 # Formats currentBalance to currency
                withdrawAmount = int(input())

            currentBalance -= withdrawAmount
            setCurrentBalance(user, str(currentBalance))
            if database.update(accountNumberFromUser, user):
                print("Your balance is %s\nThank you.\n" % "${:,.2f}".format(currentBalance))
                print("Take your cash...Returning to menu\n")
                bankOperation(user)
        else:
            withdrawOperation(user)
        

def depositOperation(user):
    print("-------- Deposit --------\n")

    currentBalance = int(getCurrentBalance(user))
    depositAmount = input("How much would you like to deposit?\n")
    is_valid_deposit_amount = validation.money_validation(depositAmount)

    if is_valid_deposit_amount:

        depositAmount = int(depositAmount)
        currentBalance += depositAmount
        setCurrentBalance(user, str(currentBalance))
        
        if database.update(accountNumberFromUser, user):
            print("Deposit made.\n")
            print("Your balance is %s\nThank you.\nReturning back to the menu\n" % "${:,.2f}".format(currentBalance))
            bankOperation(user)
    else:
        bankOperation(user)


def complaint(user):
    complaintString = input("What issue will you like to report?\n")
    print("Thank you for contacting us. Returning to menu\n")
    bankOperation(user)

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance 

def getCurrentBalance(userDetails):
    return userDetails[4]

#### START OF PROGRAM ####

init()



