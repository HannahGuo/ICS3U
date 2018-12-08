# Hannah Guo
# May 24th 2018
# ICS3UR
# This program is a game of Arcade Dice. The user starts off with 1000 coins, and their goal is to increase this amount
# to at least 10000. This is done by betting their current coins and predicted the outcome of the sum of two rolled
# dice. The user guesses "low" when they think that the sum of the two dice will be between 2 and 6, and "high" if they
# predict the sum of the two dice will be between 8 and 12. If the user guessed correctly, they will receive the amount
# of coins they bet. If they guess incorrectly, they will lose the amount of coins they bet. No coins are gained or lost
#  if a 7 is rolled). The user only has 10 bets, and can only make bets up to 1500 coins at a time.

import random  # imports the random library, used to generate a random number.
import sys     # imports the system library, used to for the sys.exit() function which stops the program and stdout
               # for printing without a newline character
import time    # imports the time library, used for delays to enhance the visual effects of the dice rolling print

playerCoins = 1000  # this sets the initial value of playerCoins to be 1000 since this is how many coins the player
                    # starts with
quitFlag = False    # the quitFlag is initially set to False since the checkifQuit() functons hasn't run yet
winCounter, lossCounter, betCounter = (0,) * 3  # this sets the winCounter, loseCounter and betCounter to the initial
                                                # value of 0 since the user hasn't won, lost, or bet yet


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


def diceRoll():
    """
    This function acts as a dice roll. It generates a random integer between 1 and 6 (dice range, inclusive), and
    returns it.
    :return A random dice roll (int):
    """
    return random.randint(1, 6)  # generates a random integer between 1 and 6 (inclusive) and returns it.


def tripleDotDicePrint(num):
    """
    This function prints out the dice rolling print outs to the console. Since it's more aesthetically pleasing if the
    triple dots appear one at a time, this function formats it like that.
    :param num:
    :return:
    """
    sys.stdout.write("Rolling dice #" + str(num))  # sys.stdout.write() is essentially the same as a print statement,
                                                   # but without the newline character. This prints out the dice number
                                                   # that is rolling.
    for i in range(3):   # this loop runs three times (for the numbers 0, 1 and 2 which is when i is in range(3)). This
                         # is to generate the three dots.
        sys.stdout.flush()  # Python normally has a buffer for stdout (standard out) prints. By calling the flush()
                            # function, it will write the next contents to the console instead of waiting for the
                            # buffer. This gives the desired effect with the three dots.
        time.sleep(0.67)   # the time library is used here to implement a pause between the printing of the dots.
        sys.stdout.write(".")  # stdout (equivalent to print) another dot.
    print()  # this empty print statement serves as a new line divider so that the print out after this function is
             # called is on its own line (better spacing)


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
# of the game (Arcade Dice) and a program/game description for the user.
print("**************************************************************************************************"
      "\n                             _        _____  _   "
      "\n     /\                     | |      |  __ \(_)         "
      "\n    /  \   _ __ ___ __ _  __| | ___  | |  | |_  ___ ___ "
      "\n   / /\ \ | '__/ __/ _` |/ _` |/ _ \ | |  | | |/ __/ _ \ "
      "\n  / ____ \| | | (_| (_| | (_| |  __/ | |__| | | (_|  __/"
      "\n /_/    \_\_|  \___\__,_|\__,_|\___| |_____/|_|\___\___|"
      "\n\nWelcome to the Arcade! You have been given 1000 coins. The goal of the game is to walk out of the \narcade "
      "with at least 10000 coins in 10 bets. State how many coins you want to put on the line (max limit of \n1500 "
      "coin bets), and guess the outcome of a dice roll. If you guess the outcome correctly, your \nbet is doubled and "
      "returned to you. If you guess wrong, you lose your coins! The game ends \nonce you go broke, run out of bets, "
      "or win! \nType 'quit' at any point in the program to quit the game. ")

while True:  # this while loop will continue running until the user enters 'quit' and the program ends. This allows the
             # program to run continuously.
    playerCoinBet = 0  # playerCoinBet is reset to 0, since the player hasn't made a bet their coins for this round.
                       # This value can be changed and accessed throughout the whole while loop.
    playerBet = ""     # the player's desired bet ("high" or "low") is reset to a blank string. This value can be
                       # changed and accessed throughout the whole while loop.
    while True:  # this while loop will continue running until a valid option was entered and break runs
                 # (or the program quits). Essentially, it stops running if a valid input for playerCoinBet is received.
        # the following print statement is simply a visual divider
        print("**************************************************************************************************")

        try:  # tries running the code in this block
            # the prompt below asks the user for their coin bet and assigns this to playerCoinBet. The checkIfQuit
            # function is called to check if the user entered 'quit'. It is then cast to an int for comparison operators
            # later.
            playerCoinBet = int(checkIfQuit(input("Input how many coins you would like to bet "
                                                  "(a positive integer, floats will not be accepted): ")))
        except ValueError:  # this will catch anything that would cause a ValueError in the code above. Essentially,
                            # if playerCoinBet is a string or float, it isn't an int. Once this except runs, it will
                            # loop back to the try block
            if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a string,
                # it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                # out an invalid input. No else is needed since the program will just keep running normally if this is
                # false.
                quitFlag = False  # reset quitFlag to False since this case has been handled
                continue  # restart the loop. None of the code after this point will run this iteration if
                          # continue runs.
            print("Invalid input, please try again.")  # prints out that this input is invalid. The loop resets after
                                                       # this runs, and returns back to the userGuess prompt.
        else:  # this code runs if no ValueError was found
            if playerCoinBet > 1500:  # this checks if the player coin bet is greater than 1500, which is invalid since
                                      # the maximum coin bet per bet is 1500.
                print("The highest amount of coins you can bet at once is 1500!")  # prints out that the highest coin
                                                                                   # amount is 1500
                continue  # restart the loop
            elif 1 > playerCoinBet:  # this checks if the user entered in a bet that was less than 1 coin, which is
                                     # invalid since the minimum coin bet is 1 coin, and negative bets aren't allowed.
                print("You must bet at least one coin!")  # prints out that the user must bet at least one coin.
                continue  # restart the loop
            elif playerCoinBet > playerCoins:  # this checks if the user placed a bet that was more than the amount of
                                               # coins that they had. This is invalid since in this game, it's
                                               # impossible to bet coins that the user doesn't have.
                print("You don't have that many coins! You only have " + str(playerCoins) + " coins!")  # prints out
                                                                                                        # that the user
                                                                                                        # doesn't have
                                                                                                        # enough coins
                                                                                                        # for their bet
                continue  # restart the loop
            while True:  # this while loop will continue running until a valid option was entered and break runs
                         # (or the program quits). Essentially, it stops running if a valid input for playerBet
                         # is received.
                # the following print statement is simply a visual divider
                print("****************************************************"
                      "**********************************************")
                # the prompt below asks the user for their bet on the outcome of the dice roll and assigns this
                # to playerBet. The checkIfQuit function is called to check if the user entered 'quit'. It's cast to
                # a string for data consistency.
                playerBet = checkIfQuit(str(input("Would you like to guess high or low? Type: "
                                                  "\n'low' to guess if the sum of the two dice rolled will be "
                                                  "between 2 and 6\n'high' to guess if the sum of the two dice "
                                                  "rolled will be between 8 and 12. \nNo action is taken if a sum of 7 "
                                                  "is rolled.\nInput: ")))

                if playerBet == "low" or playerBet == "high":  # this checks if a valid option ('low' or 'high')
                                                               # was entered
                    betCounter += 1  # a bet was made, so increment bet by one.
                    break  # since a valid option was entered, break out of this while loop and move on to the next
                           # part of the code

                if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user
                              # recently typed quit. No else is needed since the program will just keep running normally
                              # if this is false.
                    quitFlag = False  # this sets quitFlag to False because the current quit instance has been
                                      # handled
                    continue   # restart the loop, bringing the user back to the playerBet prompt. This is so the
                               # invalid input print below doesn't print out

                print("Invalid input, please try again. ")  # prints out that an invalid input was entered. Once
                                                            # this runs, playerBet is run again as the loop goes on
                                                            # to its next iteration.

            tripleDotDicePrint(1)  # runs the tripleDotDicePrint() function for dice one, note that this is only
                                   # the visual prints for the user.
            diceOne = diceRoll()   # assigns diceOne a random dice value (generated by the diceRoll() function)
            print("Dice #1 has rolled a " + str(diceOne) + "!")  # prints out the value of diceOne for the user

            tripleDotDicePrint(2)  # runs the tripleDotDicePrint() function for dice two, note that this is only
                                   # the visual prints for the user.
            diceTwo = diceRoll()   # assigns diceTwo a random dice value (generated by the diceRoll() function)
            print("Dice #2 has rolled a " + str(diceTwo) + "!")  # prints out the value of diceTwo for the user

            diceSum = diceOne + diceTwo  # assigns diceSum the sum of diceOne and diceTwo.
            diceStatus = ""              # create a variable called diceStatus that can be accessed and assigned by
                                         # the statements below.

            print("The sum of these dice is " + str(diceSum) + ".")  # prints out the sum of the dice for the user

            if 2 <= diceSum <= 6:   # if the diceSum is low (between 2 and 6, inclusive) run this code
                diceStatus = "low"  # assigns diceStatus to 'low'
            elif 8 <= diceSum <= 12:  # if the diceSum is high (between 8 and 12, inclusive) run this code
                diceStatus = "high"   # assigns diceStatus to 'high'
            else:                   # this else code only runs if a sum of 7 occured, since the only possible
                                    # sums are the integers from 2 to 12 (since the minimum value of each dice and
                                    # the maximum is 6). Since all other possibilities were covered, the only
                                    # remaining option is that there was a sum of 7.
                # The print statement below prints that a 7 was rolled. It also states the user's current coin
                # balance and how many bets they have remaining. Since the user has 10 initial bets, subtract
                # the current number of bets they have made from 10. The pluralize function is also called for
                # proper grammar in the word "bet".
                print("No action is taken since a 7 was rolled. Your current balance is " + str(playerCoins)
                      + " coins. You have " + str(10 - betCounter) + pluralize(" bet", 10 - betCounter)
                      + " remaining to get 10000 coins.")
                continue  # this skips the rest of the loop and goes back to the playerBet prompt to receive the
                          # next bet

            print("The dice sum is " + diceStatus + ".")  # prints out the diceStatus for the user

            if diceStatus == playerBet:  # this runs if the player's guess (playerBet) was the same as the dice
                                         # result (i.e they guessed correctly)
                playerCoins += playerCoinBet  # add the coin amount the user bet to their coin sum
                # the print statement below tells the user that they correctly guessed the sum status (low or high)
                # of the dice roll, and the amount of coins that has been added to their total.
                print("You guessed correctly! Your balance has increased by " + str(playerCoinBet) +
                      pluralize(" coin", playerCoinBet) + ".")
            else:  # this runs if the player did not guess the dice result correctly
                playerCoins -= playerCoinBet  # deducts coin amount the user bet to their coin sum
                # the print statement below tells the user that they incorrectly guessed the sum status
                # (low or high) of the dice roll, and the amount of coins that have lost. The pluralize function is
                # called to ensure proper grammar.
                print("You guessed incorrectly! You lost the " + str(playerCoinBet) +
                      pluralize(" coin", playerCoinBet) + " that you bet. ")

            # prints out the player's current coin balance. The pluralize function is called to ensure proper grammar.
            print("Your current balance is " + str(playerCoins) + pluralize(" coin", playerCoins) + ".")

            if betCounter == 10:  # this checks if the user has reached the bet limit (10)
                print("You ran out of bets! ")  # prints out that the user ran out of bets, meaning they lose
                lossCounter += 1  # the user has lost, so add 1 to the lose counter
                break  # break out of this loop so the rest of the code runs
            elif playerCoins <= 0:  # this runs if the user has 0 or less coins, in which case they don't have any
                                    # coins to bet with anymore so they lose
                print("You ran out of coins!")  # prints out that the user ran out of coins
                lossCounter += 1  # the user has lost, so add 1 to the lose counter
                break  # break out of this loop so the rest of the code runs
            elif playerCoins >= 10000:  # this runs if the user has 10000 or more coins, which is a win
                winCounter += 1  # the user has won, so add 1 to the win counter
                print("Congrats, you have reached 10000 coins! It took you " + str(betCounter) +
                      pluralize(" bet", betCounter) + " to win!")
                break  # break out of this loop so the rest of the code runs

            # This print statement only runs if none of the conditions above are met. It prints out the user's
            # current balance, how many bets they have made, and how many bets they have left to get 10000 coins.
            # Once this print finishes, the loop moves on to its next iteration (back up to the playerBet prompt).
            # Again, the pluralize function is called to ensure proper grammar.
            print("You have made " + str(betCounter)
                  + pluralize(" bet", betCounter) + ". " + "You have " + str(10 - betCounter)
                  + pluralize(" bet", 10 - betCounter) + " left to get to 10000 coins.")

    # This print statement only runs if the user has won or lost their current game. It prints out how many games
    # the user has won and lost (accessing these numbers through winCounter and loseCounter). Again, the pluralize
    # function is called to ensure proper grammar.
    print("You have won " + str(winCounter) + pluralize(" game", winCounter) +
          " and lost " + str(lossCounter) + pluralize(" game", lossCounter) + ".")

    while True:  # this while loop continues running until it breaks out (or the program quits)
            # keepPlaying is an input that checks if the user wants to continue or quit. The 'quit' options is handled
            # in the checkIfQuit function.
            keepPlaying = checkIfQuit(str(
                input("Would you like to keep playing? Type 'continue' to play again and 'quit' to exit. ")))

            if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                          # quit. No else is needed since the program will just keep running normally if this is false.
                quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
                continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop
                          # conditions below don't detect an invalid input and print that out.

            if keepPlaying == "continue":  # condition that runs if the user would like to keep playing.
                                           # ('continue' was entered)
                print("Program restarting...")  # prints out that the program is restarting
                playerCoins = 1000  # this resets playerCoins to its initial starting value of 1000
                betCounter = 0      # this resets betCounter to its initial starting value of 0
                break  # breaks out of this while loop to restart the main while loop on line 47
            else:      # since 'quit' and 'continue' were already handled, the option entered must be invalid if this
                       # runs.
                       # Note that the while loop will go back to keepPlaying since the while loop hasn't ended.
                print("Invalid input, please try again.")  # prints out that the user's input is invalid.
