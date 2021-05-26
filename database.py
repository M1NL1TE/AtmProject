# create record
# update record
# read record
# delete record
# CRUD (create, read, update, delete)

#search for user
import os
import validation

user_db_path = "ATMProject/data/user_record/"

def create(accountNumber, first_name, last_name, email, password):
    # create a file
    # name of the file will be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, delete created file

    userDetails = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if doesAccountNumberExist(accountNumber):
        print("Account number exists already, try again\n")
        return False

    if doesEmailExist(email):
        print("Email already exists, try again\n")
        return False

    completionState = False

    try:
        f = open(user_db_path + str(accountNumber) + ".txt", "x")
   
    except FileExistsError:
        doesFileContainData = read(user_db_path + str(accountNumber) + ".txt")
        if not doesFileContainData:
            delete(accountNumber)
  
    else:
        f.write(str(userDetails))
        completionState = True
   
    finally:
        f.close()
        return completionState
    
def userLoginStatus(accountNumber):
    loginStatus = False
    try:
        f = open("ATMProject/data/auth_sessions/" + str(accountNumber) + ".txt", "x" )
    except FileExistsError:
        doesFileContainData = readLogin(accountNumber)
        if not doesFileContainData:
            userLogOut(accountNumber)
    else:
        f.write("User: " + accountNumber + " is logged in" )
        loginStatus = True
    finally:
        return loginStatus

def userLogOut(accountNumber):
    is_delete_successful = False
   
    if os.path.exists("ATMProject/data/auth_sessions/" + str(accountNumber) + ".txt"):
        try:
            os.remove("ATMProject/data/auth_sessions/" + str(accountNumber) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful

    return True


    

def read(accountNumber):
    
    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(accountNumber)
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(accountNumber) + ".txt", "r")
        else:
            f = open(user_db_path + accountNumber, "r")
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid input, need number format")
    else:
        return f.readline()

def readLogin(accountNumber):
    
    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(accountNumber)
    try:
        if is_valid_account_number:
            f = open("ATMProject/data/auth_sessions/" + str(accountNumber) + ".txt", "r")
        else:
            f = open("ATMProject/data/auth_sessions/" + accountNumber, "r")
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid input, need number format")
    else:
        return f.readline()


def update(accountNumber, userDetails):
    # find user with account number
    # fetch the contents of the file
    # update the content of the file
    # save the file\
    # return true
    user = userDetails[0] + "," + userDetails[1] + "," + userDetails[2] + "," + userDetails[3] + "," + userDetails[4]

    try:
        f = open(user_db_path + str(accountNumber) + ".txt", "r+")
        f.write(user)
        return True
    except FileNotFoundError:
        print("User not found")
    

   # return True


def delete(accountNumber):
     # find the user with account number
    # delete the user record (file)
    # return true
    is_delete_successful = False
   
    if os.path.exists(user_db_path + str(accountNumber) + ".txt"):
        try:
            os.remove(user_db_path + str(accountNumber) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful

    return True
   


def doesEmailExist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        userList = str.split(read(user), ',')
        if email in userList:
            return True
    return False

def doesAccountNumberExist(accountNumber):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(accountNumber) + ".txt":
            return True
    return False

def authenticatedUser(accountNumber, password):
    if doesAccountNumberExist(accountNumber):
        user = str.split(read(accountNumber), ',')
        if password == user[3]:
            return user
    
    return False

# create(1234567890, ["Mike", "Nwachukwu", "minlite27@gmail.com", "password", 10])
# print(read(9780374302))
#print(read(9849584732))

#print(doesAccountNumberExist(1210263275))
#print(read({"one": "two"}))