def money_validation(moneyInput):
    #Check if money input is an int
    #Make sure amount isn't <= 0
    if moneyInput:

         
        try:
            int(moneyInput)
            if int(moneyInput) > 0:
                return True
            else:
                print("Amount cannot be negative.\nPlease try again")
                return False
        except TypeError:
            print("Amount should be a number.\nPlease try again.")
            return False
        except ValueError:
            print("Incorrect amount of money.\nPlease try again.")
            return False
 
    else:
        print("Cash amount is a required field")
        return False

def account_number_validation(accountNumber):
    # Check if accountNumber is not empty
    # if accountNumber is 10 digits
    # if the accountNumber is an integer
    
    if accountNumber:
 
        try:
            int(accountNumber)
            if len(str(accountNumber)) == 10:
                return True

        except ValueError:
            return False

        except TypeError:
            return False

    else:
        return False


