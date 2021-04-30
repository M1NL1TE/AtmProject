#Author: Michael Nwachukwu
#Date last revised: 4/29/2021
#---------------------------------------------

#Import datetime class from datetime module
from datetime import datetime

name = input("What is your name?\n")
allowedUsers = ['Mike', 'Seyi', 'Love']
allowedPassword = ["passwordMike", "passwordSeyi", 'passwordLove']


if(name in allowedUsers):
   password =  input("Enter password:\n")
   userId = allowedUsers.index(name)
   
   if(password == allowedPassword[userId]):
       selectedOption = 0
       print("Welcome %s" % name)
       dateAndTime = datetime.now()
       print("Today's date and time: ", dateAndTime.strftime("%m/%d/%y %H:%M:%S")) #format the date to be d
       currentBalance = 0
       while selectedOption != 4:
        print("These are the available options:")
        print("1: Withdraw")
        print("2: Cash Deposit")
        print("3: Complaint")
        print("4: Exit")

        withdrawAmount = 0
        selectedOption = int(input("Please make a selection\n"))
                
        if selectedOption == 1:
            if (currentBalance == 0):
                print("insufficient funds. Returning to menu")
            else:
                withdrawAmount = int(input("How much would you like to withdraw?\n"))
                while withdrawAmount > currentBalance:
                    print("Insuffient funds, you only have %s left in your account. Enter new amount\n" % "${:,.2f}".format(currentBalance)) # Formats currentBalance to currency
                    withdrawAmount = int(input())
                currentBalance -= withdrawAmount
                print("Your balance is %s\nThank you." % "${:,.2f}".format(currentBalance))
                print("Take your cash")

        elif selectedOption == 2:
            depositAmount = int(input("How much would you like to deposit?\n"))
            currentBalance += depositAmount
            print("Deposit made. Thank you. Returning back to the menu")
            print("Your balance is %s\nThank you. Returning back to the menu" % "${:,.2f}".format(currentBalance))        
    
        elif selectedOption == 3:
            complaintString = input("What issue will you like to report?\n")
            print("Thank you for contacting us.\nReturning to menu")
        
        elif selectedOption == 4:
            print("You have chose to exit. Please take your card\nGood Bye!")  

        else:
            print("Invalid option, please try again")
       
   else: 
       print("Password incorrect, please try again")
else:
    print("Name not found, please try again")
    