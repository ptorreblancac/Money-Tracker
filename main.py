from datetime import datetime
from transaction import Transaction
from dashboard import Dashboard 
from category import Category

dash = Dashboard()

def showMainPanel():
    print("1. Add new transaction.")
    print("2. Edit existing transaction.")
    print("3. Modify categories.")
    print("4. Show all transactions.")
    print("5. Show monthly report.")

def addTransaction():
    type = input("Type of transaction [earning/expense]: ")
    name = input("Enter a name for the transaction: ")
    description = input("Enter a description for the transaction or leave this space blank: ")
    amount = input("Enter the amount: ")
    category = input("Enter the category of the expense: ")
    date = input("Enter the date: ")

    t = Transaction(type,name,description,amount,category,date)
    dash.addTransaction(t)
    print("Your transaction was added successfully!\n")

def editTransactions():
    allTransactions = dash.getAllTransactions()
    for index,t in enumerate(allTransactions):
        print(f"{index+1}. {t.name}: {t.description}. Type: {t.type}. Amount: {t.amount}. Category: {t.category}. Date: {t.date}\n")

    try:
        opt = int(input("Please choose the transaction you want to edit: "))
        t = allTransactions[opt-1]
    except ValueError:
        print("You must enter a valid option!\n")

    continueEditing = True
    while (continueEditing):
        try: 
            print("Choose which field you would like to edit:") 
            n = int(input("[1] Name. [2] Description. [3] Amount. [4] Type. [5] Category.\n")) 
            allAttributes = ["name","description","amount","type","category"]
        except ValueError: print("You must enter a valid option!\n")

        newValue = input("Please provide the new value for the option you chose: ")
        dash.editTransaction(opt-1,newValue,allAttributes[n-1])

        choice = input("Do you want to keep editing the transaction? [y/n]")
        if (choice == 'n'):
            continueEditing = False
    

def modifyCategories():
    try:
        n = int(input(("What would you like to do? [1] Add Category. [2] Remove category. [3] Change name.")))
    except ValueError:
        print("You must enter a valid option!")
        
    allCategories = dash.getAllCategories()
    match n:
        case 1:
            name = input("Insert the name of the category you want to create: ")
            c = Category(name,0)
            dash.addCategory(c)
        case 2:
            dash.removeCategory(allCategories[opt-1])
        case 3:
            print("Here is a list of all categories:\n")
            for index,c in enumerate(allCategories):
                print(f"{index+1}. {c.name}\n")
            try:
                opt = int(input("Select the index of the category you want to modify: "))
            except ValueError:
                print("You must enter a valid option!")
            newName = input("Please enter the new name for the category you selected: ")
            dash.updateCategories(opt-1,newName)


def showAllTransactions():
    allTransactions = dash.getAllTransactions()
    if (len(allTransactions) == 0):
        print("There are currently no trasactions to show!")
    else:
        for index, t in enumerate(allTransactions):
            print(f"{index+1}. Name: {t.name}.  Type: {t.type}. Amount: {t.amount}. Category: {t.category}. Date: {t.date}\n")

def showMonthlyReport():
    ### TO BE IMPLEMENTED ###
    print()


print("Welcome to your money tracker!")
while True:
    showMainPanel()
    try:
        opt = int(input("Please choose the action you want to take: "))
        match opt:
            case 1:
                addTransaction()
            case 2:
                editTransactions()
            case 3:
                modifyCategories()
            case 4:
                showAllTransactions()
            case 5:
                showMonthlyReport()
            case _:
                print("You must enter a valid number!\n")
    except ValueError:
        print("Please make sure you enter a valid integer!\n")        





