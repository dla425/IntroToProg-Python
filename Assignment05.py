# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DAlbano,2.15.22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # A capture of the user task entered
strPriority = ""  # A capture of the user priority for the task entered
strItem = ""  # A capture of the user task to remove

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"task": strData[0], "priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print("Task: ", row['task'], "|", "Priority: ", row['priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter the task: ")
        strPriority = input("Enter the priority: ")
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)
        print("\nTask added!")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = input("Enter task to remove: ")
        for row in lstTable:
            if row["task"].lower() == strItem.lower():
                lstTable.remove(row)
                print("\nTask removed")
            else:
                print("\nTask not found")
            break
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["task"]) + ',' + str(row["priority"]) + '\n')
        objFile.close()
        print("Data saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye!")
        break  # and Exit the program
