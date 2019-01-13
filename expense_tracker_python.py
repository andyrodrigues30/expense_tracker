# IMPORTS
import sys
import datetime
import csv

# menu options
menuDisplayOptions = '''
================================
1) Display Expense Overview
2) Add Expense
3) Set Budget
4) Exit

Enter option number:\t
'''

# expense categories
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

# check budget
def checkBudget(newBudget):
    with open("user_exp_data.csv", "r") as expenseDataFile:
        totalExpense = 0
        for i in expenseDataFile:
            reader = csv.reader(expenseDataFile, lineterminator="")
            for row in reader:
                totalExpense = totalExpense + float(row[3])
        print("\nThe current budget is £" + str(newBudget) + ".")
        if totalExpense > newBudget:
            print("You have gone over budget by £" + str(totalExpense - newBudget) + ".\n")
        else:
            amountLeft = round(((totalExpense - newBudget) * (-1)),2)
            print("You are £" + str(amountLeft) +" within the budget. Congrats!\n")

# set budget function
def setBudget(newBudget):
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
                return newBudget

# choose category to enter into file
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

# enter item to add to file
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

# enter cost of item to add to file
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

# add date to save to file
def getExpenseDate(newExpense):
    ###expenseData = below
    expenseDate = datetime.datetime.now()# current datetime
    expenseDate = expenseDate.strftime("%x")# take of the time, only have the date stored
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

def expenseOverview(userName, newBudget):
    checkBudget(newBudget)
    with open ("user_exp_data.csv", "r") as expenseDataFile:
        fileReader = csv.reader(expenseDataFile, delimiter=",")
        for line in fileReader:
            for i in line:
                if i == "username":
                    # output table header
                    print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format(*line))
                if i == userName:
                    # output all data in each line
                    print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format(*line))
    expenseDataFile.close

# check menu option that is entered
def menuOptions(userName, newBudget):
    while True:
        try:
            menuOption = int(input(menuDisplayOptions))
        except ValueError:
            # check value error
            print("That is not a valid input. Try again:\t")
        else:
            if menuOption == "":
                # nothing entered
                print("You have not entered anything. Try again: £")
                continue
            elif menuOption == 1:
                # user selected to se an overview of the expense
                print("You have selected to display expense overview.")
                expenseOverview(userName, newBudget)
            elif menuOption == 2:
                # add an expense to the file
                print("You have selected to add an expense.")
                newExpense = getExpenseCategory(userName)
                newExpense = getExpenseItem(newExpense)
                newExpense = getExpenseCost(newExpense)
                newExpense = getExpenseDate(newExpense)
                addExpense(newExpense)
            elif menuOption == 3:
                #create a new  budget
                print("You have selected to set a budget.")
                newBudget = setBudget(newBudget)
            elif menuOption == 4:
                #exit the program completely
                print("Thanks for using the program. Bye!\n")
                quit()
            else:
                print("That is not a valid input. Try again:\t")
                continue

# check username and password in database
def checkSignIn(userName, userPass, newBudget):
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
                    menuOptions(userName, newBudget)
        print("Sorry, that username and/or password is not recognised.")
    userDataFile.close()

# allow user to enter username
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

# allow user to enter password        
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

# store new user account details
def storeNewAccount(addNewUser):
    with open("user_data.csv", "a") as writeFile:#opens the csv file
        writer = csv.writer(writeFile, lineterminator="")
        #writes a each row in the csv file and at the end of the row create a new line 
        writer.writerows("\n")
        #writes the list created to the csv file as a new row
        writer.writerow(addNewUser)
        print("Your account has been added. For security reasons, please sign in again.")
    writeFile.close

# create new user account name
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

# create user account password
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

# begin program function
def beginProgram():
    newBudget = 0
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
                    checkSignIn(userName, userPass, newBudget)
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
