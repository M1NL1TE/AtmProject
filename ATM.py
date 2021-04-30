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

database = {} #database of type dictionary to hold user information

def init():

    print("Welcome to Bank ReskillLMS")
    dateAndTime = datetime.now()
    print("Today's date and time: ", dateAndTime.strftime("%m/%d/%y %I:%M %p")) #format the date to be mm/dd/yy and time to be mm:hh AM/PM
       
    haveAccount = int(input("Do you have an account with us?\n 1 (yes) 2 (no): "))

    if(haveAccount == 1 and database):
        login()
    elif(haveAccount == 1 and not database):
        print("No users in database, please register")
        register()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("-------- Login --------")

    accountNumberFromUser = int(input("What is your account number?\n"))
    password = input("What is your password?\n")

    for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                else:
                    print("Invalid Account Number or Password, try again.\n")
                    login()
    
    if( accountNumberFromUser not in database.keys()):
        print("Invalid Account Number or Password, try again.\n")
        login()
    
def register():

    print("-------- Register --------")

    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("Create a password\n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, 0] #the zero value (last value for the key) will represent the user's balance

    print("Your account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    
    login()

def bankOperation(user):

    print("Welcome %s %s\n" % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdraw (3) Logout (4) Complaint (5) Exit\n"))

    if(selectedOption == 1):
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawOperation(user)
    elif(selectedOption == 3):
        login() #return user to log in
    elif(selectedOption == 4):
        complaint(user)
    elif(selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawOperation(user):
    print("-------- Withdraw --------\n")
    if (user[4] == 0):
        print("insufficient funds\n(You should make a deposit first).\nReturning to menu\n")
        bankOperation(user)
    else:
        withdrawAmount = int(input("How much would you like to withdraw?\n"))
        while withdrawAmount > user[4]:
            print("Insuffient funds, you only have %s left in your account. Enter new amount\n" % "${:,.2f}".format(user[4])) # Formats currentBalance to currency
            withdrawAmount = int(input())
        user[4] -= withdrawAmount
        print("Your balance is %s\nThank you.\n" % "${:,.2f}".format(user[4]))
        print("Take your cash...Returning to menu\n")
        bankOperation(user)



def depositOperation(user):

   depositAmount = int(input("How much would you like to deposit?\n"))
   user[4] += depositAmount
   print("Deposit made.\n")
   print("Your balance is %s\nThank you.\nReturning back to the menu\n" % "${:,.2f}".format(user[4]))
   bankOperation(user)

def complaint(user):
    complaintString = input("What issue will you like to report?\n")
    print("Thank you for contacting us. Returning to menu\n")
    bankOperation(user)

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

#### START OF PROGRAM ####

init()



