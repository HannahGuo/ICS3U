# Hannah Guo
# June 4th 2018
# ICS3UR
# This program allows users to create a list of names (called a name bank), then manipulate its content
# (add/delete/edit) and view changes. The user can also create a new list if they wish to do so.

nameList = []     # creates an initial blank list of names
listTitle = ""    # initializes the listTitle variable


def createList():
    """
    This function handles creating the list of names.
    :return:
    """

    # The two global declarations means that the function can modify the global variables of nameList and listTitle.
    global nameList
    global listTitle

    while True:   # this while loop will continue running until a valid option was entered and break runs
                  # (or the program quits). Essentially, it stops running if a valid input for numNames is
                  # received.
        # Ask the user for the title of the list and casts to a string for data consistency
        listTitle = str(input("What would you like to name this list? "))

        if listTitle.replace(" ", "") == "":  # checks if listTitle is blank
            print("You can't have a blank list name!")  # prints out that the user can't have a blank list name
            continue  # restarts the loop

        while True:   # this while loop will continue running until a valid option was entered and break runs
                      # (or the program quits). Essentially, it stops running if a valid input for numNames is
                      # received.
            # the prompt below asks the user how many names they would like to initially input.
            numNames = input("How many names would you like to input to '" + listTitle +
                             "' initially (a positive integer): ")
            try:  # try running this code
                # this code attempts to cast numNames to an integer. If this is not possible, then the input is the
                # wrong type (invalid).
                numNames = int(numNames)
            except ValueError:  # if there is a ValueError, run this
                print("Invalid input, please try again.")  # prints that this is an invalid input and loops back to
                                                           # numNames
            else:  # if there is no ValueError, run this
                if numNames < 0:  # if numNames is less than 0 (i.e. it's a negative integer, it's invalid)
                    print("Invalid input, you cannot have a negative number of items in your list! ")  # print that this
                                                                                                       # is an invalid
                                                                                                       # input
                    continue  # loop back to numNames prompt

                if numNames == 0:  # if the user wanted a blank list (numNames is 0)
                    print("A blank list has been created. ")  # print out that a blank list was created
                    return  # exit out of this function since the code below doesn't need to run if the list is blank

                counter = 0  # set counter's initial value to 0
                while counter in range(numNames):  # this creates a for loop that runs as long as counter is in range of
                                                   # 0 to numNames (exclusive). The reason this is a while loop is
                                                   # because we need to check if a name has already been entered, which
                                                   # means it can't be entered again. Therefore, the loop may need to
                                                   # run longer if there was an invalid input, and the counter in for
                                                   # loops can't be changed during the loop.
                    name = str(input("Input a name into this list: "))  # receives an input for the name to be added.
                    if name in nameList:  # if the name is already in the nameList
                        print("This name is already in the list! Please enter another name. ")  # print that the name is
                                                                                                # already in the list.
                    elif name.replace(" ", "") == "":
                        print("You can't have a blank name! Please enter another name. ")
                    else:  # otherwise, it's a new name, so run this
                        nameList.append(name)  # add this name to nameList
                        counter += 1  # increase the counter by one since a valid name was entered.

                print("Your list has been created!")  # prints that the list was created
                return  # exits out of this function


def showList():
    """
    This function prints out the contents of the list.
    :return:
    """
    print("List Title: " + listTitle)  # print the list title

    if len(nameList) == 0:                 # if there are no items in this list
        print("This list has no names! ")  # print out that this is a blank list
        return                             # exit out of this function

    for i in range(len(nameList)):              # loop through the indexes of nameList
        print(str(i + 1) + ". " + nameList[i])  # print out the item's number and value


while True:  # this while loop will continue running until the user enters 'quit' and the program ends. This
             # allows the program to run continuously.
    # the print statement below gives a brief program description, along with a visual divider.
    print("This program allows you to create a list of names (called a name bank), then make various changes to it "
          "after. \n"
          "**************************************************************************************************")

    createList()  # this runs the createList function
    while True:   # this while loop will continue running until a valid option was entered and break runs
                  # (or the program quits). Essentially, it stops running if a valid input for computerLevel is
                  # received.
        # the print statement below is simply a visual divider.
        print("**************************************************************************************************")
        # this prompt allows users to type in which menu options they would like to perform, and assigns this value to
        # menuOptions. It's cast to a string for data type consistency.
        menuOption = str(input("Type the number that corresponds to your desired action:"
                               "\n(1) Display all names.\n"
                               "(2) Edit a name.\n"
                               "(3) Add a name.\n"
                               "(4) Delete a name.\n"
                               "(5) Clear the current list and create a new one.\n"
                               "(6) Rename list.\n"
                               "(7) Quit/close program.\nType your input: "))
        # the print statement below is simply a visual divider.
        print("**************************************************************************************************")
        if menuOption == "1":  # if the user would like to display the names
            showList()         # run the showList function to show the user's list
        elif menuOption == "2":  # if the user would like to edit a name
            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for nameToEdit is
                         # received.
                showList()  # run the showList function to show the user's list

                if len(nameList) == 0:  # if the list is blank
                    break  # break out of this loop and continue to the main loop

                nameToEdit = str(input("Which name would you like to edit? "))  # receive an input on which name to
                                                                                # edit, cast to a string for data
                                                                                # consistency.

                if nameToEdit not in nameList:  # if the name is not in the list, the user can't edit this name
                    print("That name isn't in the list, please try again. ")  # print that the name isn't in the list
                    continue  # loop back to the showList() and nameToEdit prompt

                while True:  # this while loop will continue running until a valid option was entered and break runs
                             # (or the program quits). Essentially, it stops running if a valid input for editedName is
                             # received.
                    # the following prompt asks what the user wants to changes this name to, cast to a string for data
                    # consistency
                    editedName = str(input("What would you like to change " + nameToEdit + " to? "))

                    if editedName.replace(" ", "") == "":  # this checks if the name entered was blank
                        print("You can't add a blank name!")  # this prints out that the user can't enter a blank name
                        continue  # this restarts the loop

                    nameList[nameList.index(nameToEdit)] = editedName  # set nameToEdit in nameList to editedName by
                                                                       # accessing what index nameToEdit is.
                    break
                break  # break out of this loop to return to the main loop
        elif menuOption == "3":  # if the user wants to add a name
            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for nameToAdd is
                         # received.
                nameToAdd = str(input("What name would you like to add to the list? "))  # ask what the user would like
                                                                                         # to add to this list, cast to
                                                                                         # a string for data consistency

                if nameToAdd.replace(" ", "") == "":  # this checks if the name entered was blank
                    print("You can't add a blank name!")  # this prints out that the user can't enter a blank name
                    continue  # this restarts the loop

                nameList.append(nameToAdd)  # append this item to the end of the list
                break

            print(nameToAdd + " has been added to your list.")  # print out that this item has been added to the list
        elif menuOption == "4":  # if the user wants to delete a name
            while True:     # this while loop will continue running until a valid option was entered and break runs
                            # (or the program quits). Essentially, it stops running if a valid input for nameToRemove is
                            # received.
                showList()  # run the showList function to show the user's list

                if len(nameList) == 0:  # if the list is blank
                    break  # break out of this loop and continue to the main loop

                nameToRemove = str(input("Which name would you like to remove? "))   # receive an input on which name to
                                                                                     # remove, cast to a string for data
                                                                                     # consistency.
                if nameToRemove in nameList:                    # if the name the user wants to remove is in the list
                    nameList.remove(nameToRemove)               # remove that name
                    print(nameToRemove + " has been removed.")  # print out that that name has been removed
                    break  # break out of this loop to return to the main loop

                print("That name isn't in the list, please try again. ")  # print out that this name isn't in the list,
                                                                          # and restarts the loop to the showList() call

        elif menuOption == "5":  # if the user wants to clear this list and create a new one
            while True:   # this while loop will continue running until a valid option was entered and break runs
                          # (or the program quits). Essentially, it stops running if a valid input for confirm is
                          # received.
                # the prompt below receives confirmation that the user wants to clear the current list cast to a string
                # for data consistency.
                confirm = str(input("Are you sure you want to clear your current list? Type 'y' for yes and 'n' "
                                    "for no: "))
                if confirm == "y":  # if the user does want to create a new list
                    nameList = []   # reset nameList
                    listTitle = ""  # reset listTitle
                    createList()    # create a new list
                    break           # break out of this loop and return to the main loop
                elif confirm == "n":  # if the user does not want to create a new list
                    break             # break out of this loop and return to the main loop
                else:                 # otherwise, this was an invalid input
                    print("Invalid input, please try again.")  # prints out that this was an invalid input and return
                                                               # to the confirm prompt
        elif menuOption == "6":  # if the user wants to rename the list
            while True:
                listTitle = str(input("What would you like to rename your list to? "))  # set listTitle to the user's
                                                                                        # desired string title
                if listTitle.replace(" ", "") == "":  # checks if listTitle is blank
                    print("You can't have a blank list name!")  # prints out that the user can't have a blank list name
                    continue  # restarts the loop
                break   # otherwise break out of this loop and return to the main one
        elif menuOption == "7":  # if the user wants to quit
            while True:          # this runs until it is broken out of, or the program quits
                # the doubleChecking variable asks if the user is sure they want to quit. It's cast to a string for
                # data type consistency.
                doubleChecking = str(input("Are you sure you want to quit? This will erase all your progress. "
                                           "Type 'y' to quit, or 'n' to return to the last prompt. "))
                if doubleChecking == "y":                 # checks if the user did want to exit (doubleChecking is 'y')
                    print("You have quit the program. ")  # prints that the user has quit
                    exit()                                # exits the program (stops running)
                elif doubleChecking == "n":               # checks if the user inputted 'n', which is the option to
                                                          # continue
                    break  # this break exits this while loop so the program can continue
                else:      # if this runs, then an invalid input was entered (not 'y' or 'n')
                    print("Invalid input, please try again.")  # prints that an invalid input was entered. After this
                                                               # runs, the while loop resets and the user is prompted
                                                               # again (returns to doubleChecking)
        else:                                          # otherwise, the input was invalid
            print("Invalid input, please try again.")  # prints out that the input was invalid, and loop back to the
                                                       # menuOption prompt.
