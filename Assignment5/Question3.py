# Hannah Guo
# May 24th 2018
# ICS3UR
# This program is a game called Not Nim, which is similar to the game of Nim but with a few changes. A random number of
# stones is generated at the beginning of the game. Two players then take turns taking 1, 2 or 3 stones from the
# total number of stones. The player who takes the last stone loses. This program offers both a player vs computer mode
# and a player vs player mode.

import random  # imports the random library, used to generate a random number.
import sys     # imports the system library, used to for the sys.exit() function which stops the program and stdout
               # for printing without a newline character
import time    # imports the time library, used for delays to enhance the visual effects of the print for the computer's
               # turn

quitFlag, expertMode = (False,) * 2    # the quitFlag is initially set to False since the checkifQuit() function hasn't
                                       # run yet. expertMode is initially set to False as well since the program
                                       # defaults to regular mode for the computer.
numStones = random.randint(15, 30)     # this generates a random number of stones between 15 and 30 for the game
playerStones, computerStones, = (0,) * 2  # this sets the initial values of playerStones and computerStones to 0, since
                                          # neither party has taken any stones yet.

# winLoseCounter stores how many games the player(s) has won or lost. It is a list of lists. The first level of lists
# stores the value for regular, expert, Player One and Player Two (as indicated by the third element of each inner list,
# which is a string corresponding with its value. The inner lists store the win and loss counters, where the first
# element is the win counter, the second is the loss counter.
winLoseCounter = [[0, 0, "regular"], [0, 0, "expert"], [0, 0, "Player One"], [0, 0, "Player Two"]]


def checkIfQuit(checkString):
    """
    This function handles if the user has inputted 'quit', in which case they will be prompted if they are sure if they
    want to quit, and if so, will do so. Otherwise, it will just return the value that was inputted into the function.
    :param checkString:
    :return:
    """
    if checkString == "quit":  # if the user inputted quit, run this
        while True:  # this runs until it is broken out of, or the program quits
            # the doubleChecking variable asks if the user is sure they want to quit. It's cast to a string for data
            # type consistency.
            doubleChecking = str(input("Are you sure you want to quit? This will erase all your progress. "
                                       "Type 'y' to quit, or 'n' to return to the last prompt. "))
            if doubleChecking == "y":  # checks if the user did want to exit (doubleChecking is 'y')
                print("You have quit the program. ")  # prints that the user has quit
                sys.exit()  # exits the program (stops running)
            elif doubleChecking == "n":  # checks if the user inputted 'n', which is the option to return to the last
                                         # prompt.
                global quitFlag          # this identifies that the global variable quitFlag is being referenced
                quitFlag = True          # this sets quitFlag to true, since the user recently typed quit but then
                                         # opted out
                break                    # this break exits the while loop, and the return checkString runs
            else:                        # if this runs, then an invalid input was entered (not 'y' or 'n')
                print("Invalid input, please try again.")  # prints that an invalid input was entered. After this runs,
                                                           # the while loop resets and the user is prompted again
                                                           # (returns to doubleChecking)
    return checkString  # this returns the original value for checkString


def computerTurn():
    """
    This function handles the computer's turn. It returns a value for how many stones the computer will take, and also
    prints out when it's the computer's turn (for the user).
    :return:
    """
    print("It's the computer's turn.")  # print out that it is the computer's turn.

    for i in range(3):  # this loop runs three times (for the numbers 0, 1 and 2 which is when i is in range(3)). This
                        # is to generate the three dots.
        sys.stdout.flush()  # Python normally has a buffer for stdout (standard out) prints. By calling the flush()
                            # function, it will write the next contents to the console instead of waiting for the
                            # buffer. This gives the desired effect with the three dots.
        time.sleep(0.45)        # the time library is used here to implement a pause between the printing of the dots.
        sys.stdout.write(".")  # stdout (equivalent to print) another dot.
    print()  # this empty print statement serves as a new line divider so that the print out after this function is
             # called is on its own line (better spacing)

    if numStones <= 4:  # if there is 4 or fewer stones left, we always want the computer to take the number of stones
                        # necessary to leave one left (since this is the smartest move for both modes). Since the number
                        # of stones is less than 4, the highest number we can take is 3, which is a valid move.
        return numStones - 1  # return the number of stones - 1 so that the player is forced to take the last stone.

    if expertMode:      # checks if the user is in expertMode (expertMode is True)
        # This next bit of logic is a bit complicated because it is based off a concept found in a paper online and
        # manually implemented into Python. Essentially, it ensures that the player must play perfectly in order to
        # win the game. If the player makes a single incorrect move, the computer's move will be calculated so that it
        # will always win. Paper Concept:
        # https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1008&context=mathmidexppap#7
        if numStones % 4 != 1:  # if the number has a remainder of 1 when it is divisible by 1, it doesn't matter what
                                # the computer does since the player will win. Therefore, we would skip this math and
                                # simply return a random turn.
            return numStones - ((int((numStones - 1) / 4) * 4) + 1)  # The computer wants to take the number of stones
                                                                     # so that the number of stones remaining, when
                                                                     # divided by 4, has a remainder of 1. The code was
                                                                     # written by the programmer of this program after
                                                                     # much suffering and they hope you appreciate it.
    return random.randint(1, 3)  # if none of the conditions above are met, it doesn't matter what the computer's turn
                                 # is (i.e it won't determine the outcome of the game), so randomly generate a number
                                 # between 1 and 3 (inclusive) for its turn.


def pluralize(word, num):
    """
    This function ensures that proper grammar is used. It takes in a word parameter of the original word
    (singular form), and a number parameter. If the number is 1, it returns the singular form of the word.
    Otherwise, it returns the plural form.
    :param word:
    :param num:
    :return the grammatically correct version of the word for the inputted number:
    """
    if num == 1:        # runs if the number entered is 1. The reason there is no else statement is because once a
                        # function returns something, it stops running. Therefore, if this if is false, then it will
                        # just run the code outside the statement.
        return word     # returns the singular form of the word
    return word + "s"   # returns the plural form of the word


# the print statement below is the welcoming print message for the user. It includes generated ASCII art of the title,
# of the game (Not Nim) and a program/game description for the user.
print("**************************************************************************************************"
      "\n _   _       _     _   _ _ "
      "\n| \ | |     | |   | \ | (_) "
      "\n|  \| | ___ | |_  |  \| |_ _ __ ___ "
      "\n| . ` |/ _ \| __| | . ` | | '_ ` _ \ "
      "\n| |\  | (_) | |_  | |\  | | | | | | | "
      "\n|_| \_|\___/ \__| |_| \_|_|_| |_| |_| "
      "\n\nThe game of Not Nim is similar to the Game of Nim. A random number of stones is generated between 15 and 30 "
      "\n(inclusive). Two players then alternate turns taking either 1, 2 or 3 stones. The player who is forced to "
      "\ntake the last stone loses.")

while True:  # this while loop will continue running until the user enters 'quit' and the program ends. This allows the
             # program to run continuously.
    while True:  # this while loop will continue running until a valid option was entered and break runs
                 # (or the program quits). Essentially, it stops running if a valid input for gameMode is received.
        # the prompt below asks the user for which game mode they would like to play. The checkIfQuit
        # function is called to check if the user entered 'quit'. It's cast to a string for data consistency.
        gameMode = checkIfQuit(str(input("Would you like to play against the computer (1) or another player (2)? "
                                         "\nType the number that corresponds with your desired action: ")))
        if gameMode == "1":  # if the user entered 1 for gameMode, run the one player vs computer game
            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for computerLevel is
                         # received.
                # the prompt below asks the user if they want to verse the computer in regular or expert mode. The
                # checkIfQuit function is called to check if the user entered 'quit'. It's cast to a string for data
                # consistency.
                computerLevel = checkIfQuit(str(input("Which mode would you like to play? Type: "
                                                      "\n'regular' for regular mode or "
                                                      "\n'expert' for expert mode."
                                                      "\nInput your answer: ")))
                if computerLevel == "regular":   # if computerLevel is regular, set expertMode to False (in case the
                                                 # last time the user wanted to play expert).
                    expertMode = False           # set expertMode to False
                elif computerLevel == "expert":  # otherwise, if the user wanted to play expertMode (they entered
                                                 # 'expert' for their mode)
                    expertMode = True            # set expertMode to True
                else:             # if neither of these options were entered
                    if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user
                                  # recently typed quit. No else is needed since the program will just keep running
                                  # normally if this is false.
                        quitFlag = False  # this sets quitFlag to False because the current quit instance has been
                                          # handled
                        continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the
                                  # program doesn't print out that an invalid input was entered.
                    print("Invalid input, please try again. ")  # prints out that the input was invalid for the user
                    continue  # skips the break statement in this loop and go back to the computerLevel input
                break  # if a valid mode was entered, this break statement will run and exit the loop

            # the print below tells the user how many stones are in the pile.
            print("The pile started off with " + str(numStones) + " stones.")
            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for goFirst is
                         # received.
                # the prompt below asks the user if they would like to make the first move.  The
                # checkIfQuit function is called to check if the user entered 'quit'. It's cast to a string for data
                # consistency.
                goFirst = checkIfQuit(
                    str(input("Would you like to make the first move? (type 'y' for yes and 'n' for no): ")))

                if goFirst == "n":  # if the user entered 'n' (i.e. they want the computer to go first)
                    computerStones = computerTurn()  # assign computerStones to the output of computerTurn(). Note that
                                                     # computerTurn() includes the necessary printouts for the
                                                     # the computer's turn.
                    # the print out below tells the user how many stones the computer took. The pluralize function is
                    # also called for proper grammar in the word "stone".
                    print("The computer took " + str(computerStones) + " " + pluralize("stone", computerStones) + ".")
                    numStones -= computerStones  # subtract the stones the computer took from the total amount of stones
                    break  # break out of this loop and move on to the user's turn.
                elif goFirst == "y":  # otherwise, if the user entered 'y' (i.e. they want to go first)
                    break  # break out of this loop and move on to the user's turn.
                else:  # if neither of the inputs above was entered
                    if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a
                        # string, it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                        # out an invalid input. No else is needed since the program will just keep running normally if
                        # this is false.
                        quitFlag = False  # reset quitFlag to False since this case has been handled
                        continue  # restart the loop. None of the code after this point will run this iteration if
                        # continue runs.
                    print("Invalid input, please try again.")  # prints out that this input is invalid. The loop resets
                                                               # after this runs, and returns back to the userGuess
                                                               # prompt.

            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for playerStones is
                         # received.
                # the following print statement is simply a visual divider, as well as a print out that tells the user
                # how many stones are in the pile.
                print(
                    "**************************************************************************************************"
                    "\nThe pile currently has " + str(numStones) + " stones.")
                try:  # tries running the code in this block
                    # the prompt below asks the user for how many stones they want to take and assigns this to
                    # playerStones. The checkIfQuit function is called to check if the user entered 'quit'. It is then
                    # cast to an int for proper operator use later.
                    playerStones = int(
                        checkIfQuit(input("Input how many stones you would like to take (1, 2, or 3): ")))
                except ValueError:  # this will catch anything that would cause a ValueError in the code above.
                                    # Essentially, if playerStones is a string or float, it isn't an int. Once this
                                    # except runs, it will loop back to the try block
                    if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a
                                  # string, it would cause a ValueError as it's being cast to an int. However, it
                                  # shouldn't print out an invalid input. No else is needed since the program will just
                                  # keep running normally if this is false.
                        quitFlag = False  # reset quitFlag to False since this case has been handled
                        continue  # restart the loop. None of the code after this point will run this iteration if
                                  # continue runs.
                    print(
                        "Invalid input, please try again.")  # prints out that this input is invalid. The loop resets
                                    # after this runs, and returns back to the userGuess prompt.
                else:  # this code runs if no ValueError was found
                    if not 1 <= playerStones <= 3:  # since the limit of the number of stones that a player can pick
                                                    # is between 1 to 3, if the number they inputted is not within this
                                                    # range, run this code
                        print("You cannot pick up that many stones! Please try again. ")  # print out that this was an
                                                                                          # invalid number of stones
                                                                                          # to the user
                        continue  # loop back to the beginning of the while loop (skip any code after this)
                    elif numStones < playerStones:  # the player cannot pick up more stones than how many are left.
                                                    # i.e. if there are 2 stones left, they cannot pick up 3
                        print("There aren't that many stones left, please try again.")  # print out that the user
                                                                                        # inputted to pick up more
                                                                                        # stones than are left.
                        continue  # loop back to the beginning of the while loop (skip any code after this)

                    numStones -= playerStones  # subtract the number of stones that the player chose from the total
                                               # number of stones. At this point, the number of stones that the user
                                               # inputted has been checked to be valid.
                    if numStones == 1:  # this checks if the user has won. If, after their turn, there is one stone
                                        # left, the computer would have to take this stone. Therefore, the player wins.
                        print("The computer was forced to take the last stone... You win!")  # prints out that the
                                                                                             # player won
                        if expertMode:  # if expertMode is enabled run this
                            winLoseCounter[1][0] += 1  # add one to the user's win counter in expert mode (see the
                                                       # comments for the winLoseCounter list above)
                        else:           # otherwise (i.e. regular mode is enabled) run this
                            winLoseCounter[0][0] += 1  # add one to the user's win counter in regular mode (see the
                                                       # comments for the winLoseCounter list above)
                        break           # this game is finished, break out of this loop.
                    elif numStones == 0:  # if there are no stones left by the end of the user's turn, this means that
                                          # they accidentally took the last stone, meaning they lose.
                        print("Oops... you took the last stones. You lose!")  # prints out that the player lost
                        if expertMode:  # if expertMode is enabled run this
                            winLoseCounter[1][1] += 1  # add one to the user's loss counter in expert mode (see the
                                                       # comments for the winLoseCounter list above)
                        else:           # otherwise (i.e. regular mode is enabled) run this
                            winLoseCounter[0][1] += 1  # add one to the user's win counter in regular mode (see the
                                                       # comments for the winLoseCounter list above)
                        break           # this game is finished, break out of this loop.

                    print("The pile currently has " + str(numStones) + " stones.")  # prints out the current number
                                                                                    # of stones in the pile (before
                                                                                    # the computer's turn)
                    computerStones = computerTurn()  # assign computerStones to the output of computerTurn(). Note that
                                                     # computerTurn() includes the necessary printouts for the
                                                     # the computer's turn.
                    # the print out below tells the user how many stones the computer took. The pluralize function is
                    # also called for proper grammar in the word "stone".
                    print("The computer took " + str(computerStones) + pluralize(" stone", computerStones) + ".")
                    numStones -= computerStones  # subtract the stones the computer took from the total amount of stones

                    if numStones == 1:  # after the computer's turn, if there is one stone left, the next turn the user
                                        # would be forced to take it, meaning they lose.
                        print("You're forced to take the last stone... You lose!")  # prints out that the player lost
                        if expertMode:  # if expertMode is enabled run this
                            winLoseCounter[1][1] += 1  # add one to the user's loss counter in expert mode (see the
                                                       # comments for the winLoseCounter list above)
                        else:           # otherwise (i.e. regular mode is enabled) run this
                            winLoseCounter[0][1] += 1  # add one to the user's win counter in regular mode (see the
                                                       # comments for the winLoseCounter list above)
                        break           # this game is finished, break out of this loop.

            # the print statement below only runs if the current game ended. It prints out how many games the user has
            # won and lost in regular mode, and how many games the user has won and lost in expert mode.
            # It calls the pluralize function to ensure correct grammar.
            print("You have won " + str(winLoseCounter[0][0]) + pluralize(" game", winLoseCounter[0][0])
                  + " in " + winLoseCounter[0][2] + " mode and lost " + str(winLoseCounter[0][1]) +
                  pluralize(" game", winLoseCounter[0][1]) + ".\nYou have won " + str(winLoseCounter[1][0]) +
                  pluralize(" game", winLoseCounter[1][0]) + " in " + winLoseCounter[1][2] + " mode and lost " +
                  str(winLoseCounter[1][1]) + pluralize(" game", winLoseCounter[1][1]) + ".")
            break  # this second break breaks out of the loop for the gameMode prompt so that the program can
                   # go to the while loop that checks if the user wants to play again.

        elif gameMode == "2":  # otherwise, if the user wants to run player vs player mode (they selected 2 for their
                               # gameMode), run this
            # the print out below is a visual divider and also tells the users how many stones there are in the pile
            # to begin with
            print("************************************************************************************************** "
                  "\nThe pile started off with " + str(numStones) + " stones.")
            firstPlayer = random.randint(1, 2)  # randomly choose a number between 1 and 2 (the two players) to choose
                                                # which will go first.

            if firstPlayer == 1:  # if firstPlayer generates 1, run this.
                currentPlayer = "One"  # assign currentPlayer to "One", meaning Player One starts
            else:  # otherwise, this means firstPlayer generated 2 (since there are only 2 possibilities), so run this
                currentPlayer = "Two"  # assign currentPlayer to "Two", meaning Player Two starts

            print("Player " + currentPlayer + " will start.")  # prints out which player will start the game

            while True:  # this while loop will continue running until a valid option was entered and break runs
                # (or the program quits). Essentially, it stops running if a valid input for playerStones is received.
                # the following print statement is simply a visual divider, as well as a print out that tells the users
                # how many stones are in the pile.
                print(
                    "**************************************************************************************************"
                    "\nThe pile currently has " + str(numStones) + " stones.")
                try:  # tries running the code in this block
                    # the prompt below asks the current player for how many stones they want to take and assigns this to
                    # playerStones. The checkIfQuit function is called to check if the user entered 'quit'. It is then
                    # cast to an int for proper operator use later.
                    playerStones = int(
                        checkIfQuit(input("Player " + currentPlayer + ", how many stones you would like to take? "
                                                                      "(1, 2, or 3): ")))
                except ValueError:  # this will catch anything that would cause a ValueError in the code above.
                                    # Essentially, if playerStones is a string or float, it isn't an int. Once this
                                    # except runs, it will loop back to the try block
                    if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a
                        # string, it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                        # out an invalid input. No else is needed since the program will just keep running normally if
                        # this is false.
                        quitFlag = False  # reset quitFlag to False since this case has been handled
                        continue  # restart the loop. None of the code after this point will run this iteration if
                                  # continue runs.
                    print("Invalid input, please try again.")  # prints out that this input is invalid. The loop resets
                                                               # after this runs, and returns back to the userGuess
                                                               # prompt.
                else:  # this code runs if no ValueError was found
                    if not 1 <= playerStones <= 3:  # since the limit of the number of stones that a player can pick
                                                    # is between 1 to 3, if the number they inputted is not within this
                                                    # range, run this code
                        print("You cannot pick up that many stones! Please try again. ")  # print out that this was an
                                                                                          # invalid number of stones
                                                                                          # to the user
                        continue  # loop back to the beginning of the while loop (skip any code after this)
                    elif numStones < playerStones:  # the player cannot pick up more stones than how many are left.
                                                    # i.e. if there are 2 stones left, they cannot pick up 3
                        print("There aren't that many stones left, please try again.")  # print out that the user
                                                                                        # inputted to pick up more
                                                                                        # stones than are left.
                        continue  # loop back to the beginning of the while loop (skip any code after this)

                    numStones -= playerStones  # subtract the stones the player took from the total amount of stones

                    if currentPlayer == "One":  # if the current player is One, check these conditions
                        if numStones == 1:  # after Player One's turn, if there is one stone left, the next turn
                                            # Player Two would be forced to take it, meaning Player Two loses.
                            # prints out that Player Two must take the last stone so Player One wins
                            print("Player Two is forced to take the last stone. Player One win!")
                            winLoseCounter[2][0] += 1  # increment Player One's win counter by one
                            winLoseCounter[3][1] += 1  # increment Player Two's loss counter by one
                            break  # this game is finished, break out of this loop.
                        elif numStones == 0:  # if there are no stones left after Player One's turn, Player One must've
                                              # took the last stone, so Player Two wins
                            # prints out that Player One took the last stone so Player Two wins
                            print("Oops... Player One took the last stone. Player Two wins!")
                            winLoseCounter[2][1] += 1  # increment Player One's loss counter by one
                            winLoseCounter[3][0] += 1  # increment Player Two's win counter by one
                            break  # this game is finished, break out of this loop.
                        currentPlayer = "Two"  # since Player One's turn is finished, switch the current player to
                                               # Player Two
                        print("It is now Player Two's turn.")  # print out that it's now Player Two's turn

                    else:  # if the current player is Two (since that's the only other possibility if the player
                           # isn't One), check these conditions
                        if numStones == 1:  # after Player Two's turn, if there is one stone left, the next turn
                                            # Player One would be forced to take it, meaning Player One loses.
                            # prints out that Player One must take the last stone so Player One wins
                            print("Player One is forced to take the last stone. Player Two win!")
                            winLoseCounter[2][1] += 1  # increment Player One's loss counter by one
                            winLoseCounter[3][0] += 1  # increment Player Two's win counter by one
                            break  # this game is finished, break out of this loop.
                        elif numStones == 0:  # if there are no stones left after Player Two's turn, Player Two must've
                                              # took the last stone, so Player One wins
                            # prints out that Player One took the last stone so Player Two wins
                            print("Oops... Player Two took the last stone. Player One wins!")
                            winLoseCounter[2][0] += 1  # increment Player One's win counter by one
                            winLoseCounter[3][1] += 1  # increment Player Two's loss counter by one
                            break  # this game is finished, break out of this loop.
                        currentPlayer = "One"  # since Player Two's turn is finished, switch the current player to
                                               # Player One
                        print("It is now Player One's turn. ")  # print out that it's now Player One's turn

            # the print statement below only runs if the current game ended. It prints out how many games Player One has
            # won and lost, and how many games the Player Two has won and lost. It calls the pluralize function to
            # ensure correct grammar.
            print(winLoseCounter[2][2] + " has won " + str(winLoseCounter[2][0]) +
                  pluralize(" game", winLoseCounter[2][0]) + " and lost " + str(winLoseCounter[2][1]) +
                  pluralize(" game", winLoseCounter[2][1]) + ".\n" +
                  winLoseCounter[3][2] + " has won " + str(winLoseCounter[3][0]) +
                  pluralize(" game", winLoseCounter[3][0]) + " and lost " + str(winLoseCounter[3][1]) +
                  pluralize(" game", winLoseCounter[3][1]) + ".")
            break  # this second break breaks out of the loop for the gameMode prompt so that the program can
                   # go to the while loop that checks if the user wants to play again.
        else:
            if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a string,
                          # it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                          # out an invalid input. No else is needed since the program will just keep running normally
                          # if this is false.
                quitFlag = False  # reset quitFlag to False since this case has been handled
                continue  # restart the loop. None of the code after this point will run this iteration if
                          # continue runs.
            print("Invalid input, please try again.")  # prints out that the input entered was invalid. After this runs
                                                       # the code loops back to the gameMode prompt.

    while True:  # this while loop continues running until it breaks out (or the program quits)
        # the following print statement is simply a visual divider
        print("**************************************************************************************************")
        # keepPlaying is an input that checks if the user wants to continue or quit. The 'quit' options is handled
        # in the checkIfQuit function.
        keepPlaying = checkIfQuit(str(
            input("Would you like to keep playing? Type 'continue' to play again and 'quit' to exit. ")))

        if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                      # quit No else is needed since the program will just keep running normally if this is false.
            quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
            continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop conditions
                      # below don't detect an invalid input and print that out.

        if keepPlaying == "continue":  # condition that runs if the user would like to keep playing.
                                       # ('continue' was entered)
            print("Program restarting...")  # prints out that the program is restarting
            numStones = random.randint(15, 30)  # this generates another random number of stones between 15 and 30 for
                                                # the next game
            break  # breaks out of this while loop to restart the main while loop on line 47
        else:      # since 'quit' and 'continue' were already handled, the option entered must be invalid if this runs.
                   # Note that the while loop will go back to keepPlaying since the while loop hasn't ended.
            print("Invalid input, please try again.")  # prints out that the user's input is invalid.
