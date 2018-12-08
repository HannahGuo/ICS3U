# Hannah Guo
# June 4th 2018
# ICS3UR
# This program allows the user to create and add to a character dictionary. The dictionary removes whitespace and
# converts all letters to lowercase. The user can also clear their current dictionary and create a new one.

dictionary = {}  # this creates a blank dictionary


def dictionaryControl(inputMessage):
    """
    This function controls the dictionary's creation. It can also be used to add to the dictionary.
    :return:
    """
    global dictionary  # defines that the global dictionary will be used
    inputString = ""   # initializes inputString as a blank string

    while True:  # this while loop will continue running until a valid option was entered and break runs
                 # (or the program quits). Essentially, it stops running if a valid input for inputString is
                 # received.
        inputString = str(input(inputMessage)).lower()  # receives a string to add to the dictionary, and translates it
                                                        # to lowercase.
        if inputString.replace(" ", "") == "":  # checks if inputString is simply whitespace.
            print("The program cannot make a dictionary with whitespace, please try again. ")  # prints out that
                                                                                               # whitespace alone can't
                                                                                               # be added
            continue  # restart the loop
        break         # this runs if a valid input was inputted and breaks out of this loop

    for i in range(len(inputString)):  # create a for loop that runs for however long inputString is.
        if inputString[i] in dictionary:     # if the input string's character exists in the dictionary
            dictionary[inputString[i]] += 1  # add one to its value
        elif not inputString[i].isspace():   # otherwise, if the input string's character isn't a space
            dictionary[inputString[i]] = 1   # initialize it's key with a value of 1

    viewDictionary()  # after the dictionary has been creates/updated, view it


def viewDictionary():
    """
    This function prints out the dictionary.
    :return:
    """
    # the print statement below is a visual divider, and also titles the print
    print("********************************************************\nCharacter Dictionary:")
    for i in sorted(dictionary):  # this for loop runs through the sorted items of the dictionary
        print("Key: " + str(i) + " Value: " + str(dictionary[i]))  # this prints out the dictionary's key and its value
    print("********************************************************")  # this print statement is a visual divider


# the print statement below gives a brief program description, along with a visual divider.
print("This program allows you to create a character dictionary for inputted strings, sorted alphabetically. Note that "
      "whitespace is removed, and all letters are converted to lowercase.")

while True:  # this while loop will continue running until the user enters 'quit' and the program ends. This
             # allows the program to run continuously.
    dictionaryControl("Input your string to create its character dictionary: ")  # this runs dictionaryControl with the
                                                                                 # input's message
    while True:  # this while loop will continue running until a valid option was entered and break runs
                 # (or the program quits). Essentially, it stops running if a valid input for computerLevel is
                 # received.
        # this print statement receives an input for menu
        menu = str(input("Type the number that corresponds with your desired option:\n"
                         "(1) Clear this dictionary and create a new one.\n"
                         "(2) Add keys and values to this list.\n"
                         "(3) Quit.\nInput: "))
        print("********************************************************")  # this print statement is a visual divider
        if menu == "1":  # if the user wants to clear the dictionary and create a new one
            while True:  # this runs until it is broken out of, or the program quits
                # the doubleChecking variable asks if the user is sure they want to quit. It's cast to a string for
                # data type consistency.
                doubleChecking = str(input("Are you sure you want to create a new dictionary? This will erase all your "
                                           "progress. Type 'y' to quit, or 'n' to return to the last prompt. "))
                if doubleChecking == "y":  # checks if the user did want to exit (doubleChecking is 'y')
                    dictionary.clear()  # clear the dictionary
                    dictionaryControl("Input your string to create its character dictionary: ")  # create a new
                                                                                                 # dictionary
                    break                    # break out of this loop
                elif doubleChecking == "n":  # checks if the user inputted 'n', which is the option to continue
                    viewDictionary()         # view the dictionary
                    break  # this break exits this while loop so the program can continue
                else:      # if this runs, then an invalid input was entered (not 'y' or 'n')
                    print("Invalid input, please try again.")  # prints that an invalid input was entered. After this
                                                               # runs, the while loop resets and the user is prompted
                                                               # again (returns to doubleChecking)
        elif menu == "2":  # if the user wants to add characters to this dictionary
            dictionaryControl("Input the string you would like to add to this dictionary: ")
        elif menu == "3":  # if the user wants to quit
            while True:  # this runs until it is broken out of, or the program quits
                # the doubleChecking variable asks if the user is sure they want to quit. It's cast to a string for
                # data type consistency.
                doubleChecking = str(input("Are you sure you want to quit? This will erase all your progress. "
                                           "Type 'y' to quit, or 'n' to return to the last prompt. "))
                if doubleChecking == "y":                 # checks if the user did want to exit (doubleChecking is 'y')
                    print("You have quit the program. ")  # prints that the user has quit
                    exit()                                # exits the program (stops running)
                elif doubleChecking == "n":               # checks if the user inputted 'n', which is the option to
                                                          # continue
                    viewDictionary()  # view the dictionary
                    break  # this break exits this while loop so the program can continue
                else:      # if this runs, then an invalid input was entered (not 'y' or 'n')
                    print("Invalid input, please try again.")  # prints that an invalid input was entered. After this
                                                               # runs, the while loop resets and the user is prompted
                                                               # again (returns to doubleChecking)
        else:  # otherwise, the input is invalid
            print("Invalid input, please try again. ")  # print out that this was invalid, and restart the loop
