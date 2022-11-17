# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# TTadesse,11.13.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None   # An object that represents a file
strFile = "ToDoList.txt"  # A text file to save the data in
strData =""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, 'r')
for row in objFile:
    strData = row.split(",") # each element of the file would be separated by comma
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()} # stores the data as a dictionary
    lstTable.append(dicRow) #adds the dictionary rows in a table
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current data is: ")
        print("Task" + ' | ' + "Priority(h or l)")
        for row in lstTable:
            print(row["Task"] + ' | ' + row["Priority"]) #calls and prints file from the processing section
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        Task = input("Enter a task here: ")
        Priority = input("Enter a priority for your task. 'h' for high or 'l' for low: ")
        dicRow = {"Task": Task, "Priority": Priority} # takes the user input and adds it to a dictionary
        lstTable.append(dicRow) # adds the dictionary to a table
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Which Task would you like to delete?")
        delTask = input("Enter task to delete: ") # takes input from user for a key word to delete
        if lstTable:
            for row in lstTable:
                if row["Task"] == delTask: # searches the word in the rows in table
                    lstTable.remove(row) # deletes the row that contains the input word
                    print("Your task is deleted")
        else:
            print(delTask + " doesn't exit as a listed task")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile,'w') # opens the text file to write data to it
        for row in lstTable:
            objFile.write((row["Task"] + ',' + row["Priority"]) + '\n') # adds the new data in the table as a list
        print("your 'ToDo List' Data is saved")
        print("Type '1' to display your current data ")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Would you like to exit the program?")
        exitcode = input("Enter 'y' for yes or 'n' for no: ")
        if exitcode.lower() == 'y': #ends the program when y is chosen,
            break
        else:
            continue # the program continues if the user decided not to end it.
    else: # the program continues if the user decided not to end it.
        print("*** Menu of Options Not Found ***", '\n')
        print("Please, choose [1 to 5] to perform")

