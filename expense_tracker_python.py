# IMPORTS
import sys
import datetime
import csv

menuDisplayOptions = '''
1) Display Expense Overview
2) Add Expense
3) Set Budget

Enter option number:\t
'''

def setBudget():
    while True:
        try:
            newBudget = float(input("Enter Budget: £"))
        except ValueError:
            print("That is not a valid input. Try again: £")
        else:
            if newBudget == "":
                print("You have not entered anythin. Try again: £")
                continue
            else:
                print("Thank you for your input. Your new budget of " + str(newBudget) + " has been set.")
                break

def menuOptions():
    while True:
        try:
            menuOption = int(input(menuDisplayOptions))
        except ValueError:
            print("That is not a valid input. Try again:\t")
        else:
            if menuOption == "":
                print("You have not entered anythin. Try again: £")
                continue
            elif menuOption == 1:
                print("You have selected to display expense overview.")
            elif menuOption == 2:
                print("You have selected to add an expense.")
            elif menuOption == 3:
                print("You have selected to set a budget.")
                setBudget()
            else:
                print("That is not a valid input. Try again:\t")
                continue

def checkSignIn(userName, userPass):
    with open ("user_data.csv", "r") as userDataFile:
        fileReader = csv.reader(userDataFile, delimiter=",")
        for line in fileReader:
            for i in line:
                print(i)
                if i == userName:
                    print("You are successfully signed in.")
                    userDataFile.close()
                    menuOptions()
        print("Sorry, that username and/or password is not recognised.")
    userDataFile.close()

def signInUser():
    # Username
    while True:
        try:
            userName = input("Username:\t")
        except ValueError:
            print("Sorry we are not able to process that at the moment. Please try again:")
            continue
        else:
            if userName == "":
                print("You have not entered anything. Try again.")
                continue
            else:
                return userName
                
def signInPass():
    while True:
        # Password
        try:
            userPass = input("Password:\t")
        except ValueError:
            print("Sorry we are not able to process that at the moment. Please try again:")
            continue
        else:
            if userPass == "":
                print("You have not entered anything. Try again.")
                continue
            else:
                print("end")
                return userPass

# def createAccount():
#     while True:


def createAccountName():
    # New Username
        while True:
            try:
                userName = input("New Username:\t")
            except ValueError:
                print("Sorry we are not able to process that at the moment. Please try again:")
                continue
            else:
                if userName == "":
                    print("You have not entered anything. Try again.")
                else:
                    return userName

def createAccountPass():
    while True:
        try:
            userPass = input("New Password:\t")
        except ValueError:
            print("Sorry we are not able to process that at the moment. Please try again:")
            continue
        else:
            if userPass == "":
                print("You have not entered anything. Try again.")
                continue
            else:
                print("end")
                return userPass


def beginProgram():
    while True:
        try:
            haveAccount = input("Do you have an account? (y/n)\t")
            haveAccount = haveAccount.lower()
        except ValueError:
            print("That is not a valid option. Try again:")
            continue
        else:
            if haveAccount == "":
                print("You have not entered data. Try again")
            else:
                if haveAccount == "y" or haveAccount == "yes":
                    haveAccount = "y"
                    userName = signInUser()
                    userPass = signInPass()
                    checkSignIn(userName, userPass)
                else:
                    haveAccount = "n"
                    print("You do not have an account. Please create one to continue.")
                    userName = createAccountName()
                    userPass = createAccountPass()
                    checkSignIn(userName, userPass)


# MAIN CODE
print("------------------------------------------------")
print("--Welcome to the your personal expense tracker--")
print("------------------------------------------------")
input("Press ENTER to continue...")

beginProgram()
