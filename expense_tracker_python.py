# IMPORTS
import sys
import datetime
import csv

menuDisplayOptions = '''
1) Display Expense Overview
2) Add Expense
3) Set Budget
4) Exit

Enter option number:\t
'''

categories = '''
    1) Utilitys
    2) Housing
    3) Food and Drink
    4) Transportation
    5) Insurance
    6) Leisure
    7) Education
    8) Personal
    9) Medical
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

def getExpenseCategory(userName):
    while True:
        try:
            expenseCategory = int(input(categories + "Select category from the list (enter number):\t"))
        except ValueError:
            print("That is not a valid input. Try again:\t")
        else:
            if expenseCategory == "":
                print("You have not entered anything. Try again: £")
                continue
            elif expenseCategory == 1:
                expenseCategory = "utilitys"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 2:
                expenseCategory = "housing"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 3:
                expenseCategory = "food and drink"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 4:
                expenseCategory = "transportation"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 5:
                expenseCategory = "insurance"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 6:
                expenseCategory = "leisure"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 7:
                expenseCategory = "education"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 8:
                expenseCategory = "personal"
                newExpense = [userName, expenseCategory]
                return newExpense
            elif expenseCategory == 9:
                expenseCategory = "medical"
                newExpense = [userName, expenseCategory]
                return newExpense
            else:
                print("That is not a valid input. Try again:\t")
                continue

def getExpenseItem(newExpense):
    while True:
        try:
            expenseItem = input("Enter item of expense:\t")
        except ValueError:
            print("That is not a valid input. Try again:\t")
        else:
            if expenseItem == "":
                print("You have not entered anything. Try again: £")
                continue
            else:
                newExpense.append(expenseItem)
                return newExpense

def getExpenseCost(newExpense):
    while True:
        try:
            expenseCost = float(input("Enter cost of item: £"))
        except ValueError:
            print("That is not a valid input. Try again:\t")
        else:
            if expenseCost == "":
                print("You have not entered anything. Try again: £")
                continue
            else:
                newExpense.append(expenseCost)
                return newExpense

def getExpenseDate(newExpense):
    ###expenseData = below
    expenseDate = datetime.datetime.now()
    expenseDate = expenseDate.strftime("%x")
    newExpense.append(expenseDate)
    return newExpense

def addExpense(newExpense):
    with open("user_exp_data.csv", "a") as expenseDataFile:#opens the csv file
        writer = csv.writer(expenseDataFile, lineterminator="")
        #writes a each row in the csv file and at the end of the row create a new line 
        writer.writerows("\n")
        #writes the list created to the csv file as a new row
        writer.writerow(newExpense)
        print("Your expense has been added. Thank you. next")
    expenseDataFile.close

def expenseOverview(userName):
    with open ("user_exp_data.csv", "r") as expenseDataFile:
        fileReader = csv.reader(expenseDataFile, delimiter=",")
        for line in fileReader:
            for i in line:
                if i == "username":
                    print(line)
                if i == userName:
                    print(line)
    expenseDataFile.close

def menuOptions(userName):
    while True:
        try:
            menuOption = int(input(menuDisplayOptions))
        except ValueError:
            print("That is not a valid input. Try again:\t")
        else:
            if menuOption == "":
                print("You have not entered anything. Try again: £")
                continue
            elif menuOption == 1:
                print("You have selected to display expense overview.")
                expenseOverview(userName)
            elif menuOption == 2:
                print("You have selected to add an expense.")
                newExpense = getExpenseCategory(userName)
                newExpense = getExpenseItem(newExpense)
                newExpense = getExpenseCost(newExpense)
                newExpense = getExpenseDate(newExpense)
                addExpense(newExpense)
            elif menuOption == 3:
                print("You have selected to set a budget.")
                setBudget()
            elif menuOption == 4:
                print("Thanks for using the program. Bye!\n")
                quit()
            else:
                print("That is not a valid input. Try again:\t")
                continue

def checkSignIn(userName, userPass):
    userNameSuccess = False
    userPassSuccess = False
    with open ("user_data.csv", "r") as userDataFile:
        fileReader = csv.reader(userDataFile, lineterminator="")
        for line in fileReader:
            for i in line:
                if i == userName:
                    userNameSuccess = True
                if userNameSuccess and i == userPass:
                    print("\n--------------------------------\nYou are successfully signed in.")
                    userPassSuccess = True
                    userDataFile.close()
                    menuOptions(userName)
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
                return userPass

def storeNewAccount(addNewUser):
    with open("user_data.csv", "a") as writeFile:#opens the csv file
        writer = csv.writer(writeFile, lineterminator="")
        #writes a each row in the csv file and at the end of the row create a new line 
        writer.writerows("\n")
        #writes the list created to the csv file as a new row
        writer.writerow(addNewUser)
        print("Your account has been added. For security reasons, please sign in again.")
    writeFile.close

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
                    addNewUser = [userName, userPass]
                    storeNewAccount(addNewUser)


# MAIN CODE
print("------------------------------------------------")
print("--Welcome to the your personal expense tracker--")
print("------------------------------------------------")
input("Press ENTER to continue...")

beginProgram()
