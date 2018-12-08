# Hannah Guo
# May 24th 2018
# ICS3UR
# This program is a number guessing game. The computer randomly generates a number between 1 and the specified cap
# and the user has a certain amount of guesses to guess the number. The cap and the amount of guesses varies per game
# mode, where easy has a cap of up to 10 and 5 guesses, medium has a cap of up to 25 and 6 guesses, hard has a cap of
# up to 50 and 7 guesses and challenger has a cap of 100 and 8 guesses. If the user guessed incorrectly, the program
# will give them a hint on if the computer's number is higher or lower than their guess. The program keeps track of
# the player's wins and losses in each mode, and only ends if the player quits.

import random  # imports the random library, used to generate a random number.
import sys     # imports the system library, used to for the sys.exit() function which stops the program

# The list below stores the wins and total games for each mode. From left to right, the arrays represent easy, medium,
# hard and challenger modes. The first value in the array is the number of wins in that mode. The second value is the
# total number of games played in that mode. The third is the string value for the game mode. The list needs to be
# outside the while loop because it needs to keep track of the wins and losses until the program ends without resetting
# every time the while loop runs.
winRecord = [[0, 0, "easy"], [0, 0, "medium"], [0, 0, "hard"], [0, 0, "challenger"]]
quitFlag = False  # quitFlag monitors if the user has recently exited out of a quit (typed quit, then changed their mind
                  # and said no to the second prompt). Overall, this flag stops the normal invalid input messages that
                  # quit might cause. (see code below)


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
                print("Invalid input, please try again")  # prints that an invalid input was entered. After this runs,
                                                          # the while loop resets and the user is prompted again
                                                          # (returns to doubleChecking)
    return checkString  # this returns the original value for checkString


def pluralize(word, num):
    """
    This function ensures that proper grammar is used. It takes in a word parameter of the original word
    (singular form), and a number parameter. If the number is 1, it returns the singular form of the word.
    Otherwise, it returns the plural form. Since the word "guess" has a special plural form, it has its own condition
    in the function.
    :param word:
    :param num:
    :return the grammatically correct version of the word for the inputted number:
    """
    if word == " guess":  # if the word entered was guess, run this. guess has a space because it was easier to format
                          # strings like this. All instances where this function is used uses this so the condition
                          # works fine.
        if num != 1:     # if the number for the word "guess" was not 1
            return word + "es"  # return "guesses" (guess + es)
    elif num == 1:  # if the number was 1
        return word  # always return the word (no alterations)
    else:  # if this runs, that means the word entered must be plural and regular
        return word + "s"  # return the plural form of the word (word + s)


# the print statement below is the welcoming print message for the user. It includes generated ASCII art of the title,
# of the game (Number Guesser) and a program/game description for the user.
print("**************************************************************************************************"
       "\n _   _                 _                  _____                               "
       "\n| \ | |               | |                / ____|                            "
       "\n|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___  ___ _ __"
       "\n| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|/ _ \ '__|"
       "\n| |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \  __/ |"
       "\n|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/\___|_|\n\n"
      "Welcome to the Number Guesser! This game involves you (the player) to try to guess the number \nthe computer has"
      "randomly generated. There are four modes, each one with a different maximum number \n(called max in the "
      "description of the mode) and different numbers of guesses you have. Note that \nharder modes have a larger "
      "range, though slightly more guesses. Good luck! ")

while True:        # this while loop continues running until the user enters 'quit' and the program ends. This allows
                   # the program to run continuously.
    gameMode = ""  # this stores the current game mode
    gameSettings = [0] * 2  # this creates a list with an initial value of [0, 0]. The first value represents the
                            # maximum number that the random geneerator can generate, and the second value represents
                            # the maximum number of guesses
    userGuess, guessCounter = (0,) * 2  # This assigns userGuess and guessCounter an initial value of 0. userGuess
                                          # is the number that the user guesses. guessCounter counts how many guesses
                                          # the user has tried.

    while True:  # this while loop will continue running until a valid option was entered and break runs
                 # (or the program quits). Essentially, it stops running if a valid input for gameMode is received.
        # this print statement is simply a visual divider to separate games
        print("**************************************************************************************************")

        # gameMode stores which game mode the user would like to play on. The input is cast to a string (for data type
        # consistency), and this input runs through the checkIfQuit function to check if the user inputted 'quit'. If
        # the user's input wasn't 'quit', it will assign the input to gameMode.
        gameMode = checkIfQuit(str(input("Select your game mode. "
                                         "\nType 'easy' for easy (max 10, 5 guesses), "
                                         "\n'medium' for medium (max 25, 6 guesses), "
                                         "\n'hard' for hard (max 50, 7 guesses), or"
                                         "\n'challenger' for challenger (max 100, 8 guesses)."
                                         "\nInput your choice: ")))
        if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                      # quit. No else is needed since the program will just keep running normally if this is false.
            quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
            continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop conditions
                      # below don't detect an invalid input and print that out.

        if gameMode == winRecord[0][2]:    # checks if the gameMode entered was 'easy'
            gameSettings[0] = 10  # sets the maximum number that the random number generator will generate to as 10
            gameSettings[1] = 5   # sets the number of guesses for the game to 5
            winRecord[0][1] += 1  # adds a game played in easy to the total number of games played in that mode
                                  # (stored in winRecord)
        elif gameMode == winRecord[1][2]:  # checks if the gameMode entered was 'medium'
            gameSettings[0] = 25    # sets the maximum number that the random number generator will generate to as 25
            gameSettings[1] = 6     # sets the number of guesses for the game to 5
            winRecord[1][1] += 1    # adds a game played in medium to the total number of games played in medium
                                    # (stored in winRecord)
        elif gameMode == winRecord[2][2]:  # checks if the gameMode entered was 'hard'
            gameSettings[0] = 50  # sets the maximum number that the random number generator will generate to as 50
            gameSettings[1] = 7   # sets the number of guesses for the game to 10
            winRecord[2][1] += 1  # adds a game played in hard to the total number of games played in hard
                                  # (stored in winRecord)
        elif gameMode == winRecord[3][2]:  # checks if the gameMode entered was 'challenger'
            gameSettings[0] = 100  # sets the maximum number that the random number generator will generate to as 100
            gameSettings[1] = 8    # sets the number of guesses for the game to 10
            winRecord[3][1] += 1   # adds a game played in challenger to the total number of games played in challenger
                                   # (stored in winRecord)
        else:  # if this runs, an invalid mode was entered.
            print("Invalid game mode, please type in a valid option. ")  # prints out that an invalid option was entered
            continue  # restarts the while loop (back to the gameMode prompt)
        break         # this only runs if a valid mode was entered (since if an invalid mode was entered, continue would
                      # have run). This breaks out of this while loop and continue with the rest of the program.

    randomNum = random.randint(1, gameSettings[0] + 1)  # this generates a random number between 1 and whatever the
                                                        # maximum limit is for the selected game mode. Note that
                                                        # the highest value (second parameter specified) is exclusive,
                                                        # so it must be incremented by 1 to include the highest value.
    # the print statement below states the range of the number generated and how many guesses the user has to guess it
    print("A random number has been generated between 1 and " + str(gameSettings[0]) +
          ". You have " + str(gameSettings[1]) + " guesses left.")

    while True:  # this while loop runs until it breaks out, which only happens if the user wins, or if the program
                 # quits. Essentially, it stops running if a valid input for userGuess is received.
        try:  # tries running the code in this block
            # the prompt below asks the user to guess the number and assigns their guess to userGuess. Again, the
            # checkIfQuit function is called to check if the user entered 'quit'. It is then cast to an int.
            userGuess = int(checkIfQuit(input("Guess the number (input an integer between a 1 and " +
                                              str(gameSettings[0]) + ", floats are considered invalid): ")))
        except ValueError:  # this will catch anything that would cause a ValueError in the code above. Essentially,
                            # if userGuess is a string or float, it isn't an int. Once this except runs, it will
                            # loop back to the try block
            if quitFlag:    # if the user has recently typed quit, then restart the loop. Since "quit" is a string,
                            # it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                            # out an invalid input. No else is needed since the program will just keep running normally
                            # if this is false.
                quitFlag = False  # reset quitFlag to False since this case has been handled
                continue          # restart the loop. None of the code after this point will run this iteration if
                                  # continue runs.
            print("Invalid input, please try again.")  # prints out that this input is invalid. The loop resets after
                                                       # this runs, and returns back to the userGuess prompt.
        else:  # this code runs if no ValueError was found
            if not (1 <= userGuess <= gameSettings[0]):  # this makes sure that the number entered is within the range
                                                         # of the generator. Remember that the maximum number that the
                                                         # random generator can generate is stored in gameSettings[0].
                print("The number you typed in isn't within range, please try again. ")  # prints that the number wasn't
                                                                                         # in range
                continue  # this restarts the while loop, prompting the user for another number guess

            guessCounter += 1           # since the user just guessed, add 1 to the guessCounter

            if userGuess == randomNum:  # if the user's guess is the same as the random number generated by the
                                        # computer, this means they have successfully guessed the number. No else
                                        # is needed because an else wouldn't do anything; the code just keeps running.
                # the print statement below tells the user that they won, and how many guesses it took them.
                # pluralize() is used to ensure proper grammar
                print("You win! It took you " + str(guessCounter) + pluralize(" guess", guessCounter) + "!")

                if gameMode == winRecord[0][2]:  # run this code if the current mode is 'easy'
                    winRecord[0][0] += 1  # the array at winRecord[0] stores values for the easy mode. The first
                    # value counts how many times the user has won by, so since the user
                    # just won, add 1 to their win score for this mode
                elif gameMode == winRecord[1][2]:  # run this code if the current mode is 'medium'
                    winRecord[1][0] += 1  # the array at winRecord[1] stores values for the medium mode. The first
                    # value counts how many times the user has won by, so since the user
                    # just won, add 1 to their win score for this mode
                elif gameMode == winRecord[2][2]:  # run this code if the current mode is 'hard'
                    winRecord[2][0] += 1  # the array at winRecord[2] stores values for the hard mode. The first
                    # value counts how many times the user has won by, so since the user
                    # just won, add 1 to their win score for this mode
                else:  # since we already know the modes are valid (from the initial checker when gameMode was first
                    # entered, the last valid mode is 'challenger'. This code runs if the mode is 'challenger'.
                    winRecord[3][0] += 1  # the array at winRecord[3] stores values for the challenger mode.
                    # The first value counts how many times the user has won by, so since the
                    # user just won, add 1 to their win score for this mode
                for counter in range(4):  # this for loop has a counter variable named "counter". It runs through
                    # the numbers 0 to 3 (since for loops start at 0 by default, and the end
                    # cap of 4 is exclusive)
                    # the if below checks if the user has played a game in the specified mode. There is no point in
                    # printing out data for a mode that the user has never played. No else is needed since nothing
                    # needs to be done if the if statement is false.
                    if winRecord[counter][0] + winRecord[counter][1] != 0:
                        # This print statement says how many games the user has won and lost in the game mode.
                        # Games lost is calculated by subtracting the number of wins from the total number of games
                        # played. pluralize() is called to ensure proper grammar.
                        print("You have won " + str(winRecord[counter][0]) +
                              pluralize(" game", winRecord[counter][0]) + " and lost " +
                              str(winRecord[counter][1] - winRecord[counter][0]) +
                              pluralize(" game", winRecord[counter][1] - winRecord[counter][0]) + " in " +
                              winRecord[counter][2] + " mode. ")
                break  # now that the user has won, this while loop is broken out of

            if guessCounter < gameSettings[1]:  # remember that gameSettings[1] stores the maximum number of guesses
                                                # that the user has for that game mode. This if checks if the user
                                                # hasn't gone above that limit.
                # This print statement says that the user guessed incorrectly and says how many games the user has left.
                # pluralize() is called to ensure correct grammar.
                print("Wrong answer, please try again. You have " + str(gameSettings[1] - guessCounter) +
                      pluralize(" guess", gameSettings[1] - guessCounter) + " left.")

                if userGuess > randomNum:  # this code runs if the userGuess is higher than the computer's randomly
                                           # generated number. This means that the user should guess lower.
                    print("Try guessing a lower number!")  # prints out that the user should try guessing a lower
                                                           # number
                else:  # since we know that the user's number isn't greater than the computer's number, and an if
                       # statement above already checks if the numbers are equal (i.e. the user won), then if this
                       # code runs, the user's number must be lower than the generated number. Therefore, they
                       # should guess a higher number.
                    print("Try guessing a higher number!")  # prints out that the user should try guessing a higher
                                                            # number
            else:  # this means that the user has run out of guesses
                # the print statement below tells the user they ran out of guesses, and what the number they were
                # trying to guess was
                print("You ran out of guesses! You lose! The number was " + str(randomNum) + ".")
                break  # breaks out of the while loop game

    while True:  # this while loop continues running until it breaks out (if the user wants to continue running the
                 # program) or they quit the program. Essentially, it stops running if a valid input for keepPlaying
                 # is received.
        # keepPlaying is an input that checks if the user wants to continue or quit. The 'quit' options is handled
        # in the checkIfQuit function.
        keepPlaying = checkIfQuit(str(
            input("Would you like to keep playing? Type 'continue' to play again and 'quit' to exit. ")))

        if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                      # quit. No else is needed since the program will just keep running normally if this is false.
            quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
            continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop conditions
                      # below don't detect an invalid input and print that out.

        if keepPlaying == "continue":  # condition that runs if the user would like to keep playing. ('continue' was
                                       # entered)
            print("Program restarting...")  # prints out that the program is restarting
            break  # breaks out of this while loop to restart the main while loop on line 47
        else:      # since 'quit' and 'continue' were already handled, the option entered must be invalid if this runs.
                   # Note that the while loop will go back to keepPlaying since the while loop hasn't ended.
            print("Invalid input, please try again.")  # prints out that the user's input is invalid.
