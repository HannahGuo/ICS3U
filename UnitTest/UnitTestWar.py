# Hannah Guo
# May 24th 2018
# ICS3UR
# This program is the Game of War with a betting system. The player starts with 100 coins and their goal is to get to
# 200 coins. Each turn, they bet if they will win or lose the game. They may bet up to 25 coins and it is possible to
# bet 0 coins (if they are not confident in winning). Two cards are drawn; one for the player and one for the computer.
# The winner is decided by having the card with the higher value, where Ace is valued at 1, Jack at 11, Queen at 12 and
# King at 13 (the highest). If the player wins, their bet amount is added to their total. If they lose, it is
# subtracted. The player has up to 10 rounds to get to 200 coins for them to win the game.

import random  # imports the random library, used to generate a random number.
import sys     # imports the system library, used to for the sys.exit() function which stops the program
import time    # imports the time library, used for delays to enhance the visual effects of the card choosing print

quitFlag = False    # the quitFlag is initially set to False since the checkifQuit() functons hasn't run yet
playerCard, computerCard = (0,) * 2  # playerCard and computerCard are initially set to 0 because they haven't been
                                     # drawn yet.
cardIndex = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]  # this list stores the cards so that the
                                                                          # values can be accessed by using an index
roundRecordCounter = [0, 0, 0]  # this list stores the number of rounds the user has won, lost and tied in their current
                                #  game. The element at index 0 is the win counter, the element at index 1 is the loss
                                # counter and the element at index 2 is the tie counter
gameRecordCounter = [0, 0]  # this list stores the number of game wins (index 0) and losses (index 1)
playerCoins = 100  # starts playerCoins off with 100 coins
playerCoinBet = 0  # starts playerCoinBet off with 0 coins (since they haven't bet yet)
betCounter = 0     # starts betCounter off with 0 (since the player hasn't made any bets yet)


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


def tripleDotDicePrint(message):
    """
    This function prints out the dice rolling print outs to the console. Since it's more aesthetically pleasing if the
    triple dots appear one at a time, this function formats it like that. The message paremeter gets the desired message
    for the print.
    :param message:
    :return:
    """
    sys.stdout.write(message)  # sys.stdout.write() is essentially the same as a print statement, but without the
                               # newline character. This prints out the dice number that is rolling.
    for i in range(3):   # this loop runs three times (for the numbers 0, 1 and 2 which is when i is in range(3)). This
                         # is to generate the three dots.
        sys.stdout.flush()  # Python normally has a buffer for stdout (standard out) prints. By calling the flush()
                            # function, it will write the next contents to the console instead of waiting for the
                            # buffer. This gives the desired effect with the three dots.
        time.sleep(0.67)   # the time library is used here to implement a pause between the printing of the dots.
        sys.stdout.write(".")  # stdout (equivalent to print) another dot.
    print()  # this empty print statement serves as a new line divider so that the print out after this function is
             # called is on its own line (better spacing)

def drawCard():
    """
    This function generates and returns a random integer between 1 and 13.
    :return:
    """
    return random.randint(1, 13)  # returns a random integer between 1 and 13


def determineWinner(player, computer):
    """
    This function takes in the two parameters of the player's card and the computer's card and returns the winner based
    on whichever value is higher. If the values are the same, it is a draw.
    :param player:
    :param computer:
    :return:
    """
    if player > computer:  # if the player's card is higher than the computer's
        return "player"    # return that the player is the winner
    elif player < computer:  # otherwise, if the computer's card is higher than the player's
        return "computer"  # return that the computer is the winner
    else:  # otherwise, the cards are the same
        return "draw"  # return a draw


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

# the print statement below is the game description for the user.
print("Welcome to the game of War. During a round, the player and the computer take turns drawing a card (at random) "
      "from the deck.\nThe user with the higher card value wins, and Ace is considered a 1. There is also a betting "
      "system involved. The player \nstarts off with 100 coins, and their goal is to get to 200. They may only make "
      "bets of up to 25 coins per bet, and have 10 bets. \nIt is allowed to bet 0 coins. ")

# the print statement below is simply a visual divider.
print("**************************************************************************************************")


while True:  # this while loop will continue running until the user enters 'quit' and the program ends. This allows the
             # program to run continuously.
    # playGame receives an input from the user that says if they want to play the game. The checkIfQuit
    # function is called to check if the user entered 'quit'. It is cast to a string for data consistency.
    playGame = checkIfQuit(str(input("Would you like to draw a card? Type 'yes' to play and 'quit' to stop playing. ")))
    if playGame == "yes":  # if the player said yes to drawing a card
        while True:  # this while loop will continue running until a valid option was entered and break runs
                     # (or the program quits). Essentially, it stops running if a valid input for playerCoinBet is
                     # received.
            # the printout below prints how many coins the player currently has.
            print("You currently have " + str(playerCoins) + pluralize(" coin", playerCoins) + ".")
            try:  # tries running the code in this block
                # the prompt below asks the user for their coin bet and assigns this to playerCoinBet. The checkIfQuit
                # function is called to check if the user entered 'quit'. It is then cast to an int for comparison
                # operators later.
                playerCoinBet = int(checkIfQuit(input("Input how many coins you would like to bet "
                                                      "(a positive integer up to 25, floats will not be accepted): ")))
            except ValueError:  # this will catch anything that would cause a ValueError in the code above. Essentially,
                                # if playerCoinBet is a string or float, it isn't an int. Once this except runs, it will
                                # loop back to the try block
                if quitFlag:  # if the user has recently typed quit, then restart the loop. Since "quit" is a string,
                              # it would cause a ValueError as it's being cast to an int. However, it shouldn't print
                              # out an invalid input. No else is needed since the program will just keep running
                              # normally if this is false.
                    quitFlag = False  # reset quitFlag to False since this case has been handled
                    continue  # restart the loop. None of the code after this point will run this iteration if
                              # continue runs.
                print("Invalid input, please try again.")  # prints out that this input is invalid. The loop resets
                                                           # after this runs, and returns back to the userGuess prompt.
            else:  # this code runs if no ValueError was found
                if playerCoinBet > playerCoins:
                    print("You don't have that many coins to bet! Try again.")
                    continue  # restarts the loop
                elif playerCoinBet == 0:
                    print("You are making a bet with no value.")
                    break
                elif playerCoinBet > 2005:  # this checks if the player coin bet is greater than 25, which is invalid
                                          # since the maximum coin bet per bet is 1500.
                    print("You may only bet up to 25 coins! Try again. ")  # prints out that the user can only bet 25
                                                                           # coins
                    continue  # restarts the loop
                break

        while True:
            tripleDotDicePrint("Drawing your card")  # print out for drawing the player's card
            playerCard = drawCard()  # draws a random card and assigns it to the player
            print("You drew a " + str(cardIndex[playerCard - 1]) + ".")  # prints out what card the player drew
            tripleDotDicePrint("Drawing the computer's card") # print out for drawing the computer's card
            computerCard = drawCard()  # draws a random card and assigns it to the computer
            print("The computer drew a " + str(cardIndex[computerCard - 1]) + ".")  # prints out what card the computer
                                                                                    # drew
            winner = determineWinner(playerCard, computerCard)  # determines the winner by passing in playerCard and
                                                                # computerCard and assigns the value to the winner
                                                                # variable
            if winner == "player":  # if the player is the winner
                print("The player wins this round! You won " + str(playerCoinBet) +
                      pluralize(" coin", playerCoinBet) + ".")  # print out that the user won and how many coins they
                                                                # won
                roundRecordCounter[0] += 1  # add one to the user's round win record
                playerCoins += playerCoinBet  # add the coins bet to the user's total
                break  # break out of this loop
            elif winner == "computer":
                print("The computer wins this round! You lost " + str(playerCoinBet) +
                      pluralize(" coin", playerCoinBet) + ".")  # print out that the player lost and how many coins they
                                                                # won
                roundRecordCounter[1] += 1  # add one to the user's round loss record
                playerCoins -= playerCoinBet  # subtract the coins bet to the user's total
                break  # break out of this loop
            else:  # otherwise, it was a draw so run this
                print("The result is a draw! Both players will now draw another card...")
                roundRecordCounter[2] += 1  # add one to the user's tie record
                continue  # restarts the loop so two more cards can be drawn

        betCounter += 1
        if betCounter == 10:
            print("You ran out of bets! You lose! ")
            gameRecordCounter[1] += 1
        elif playerCoins == 0:
            print("You ran out of coins! You lose! ")
            gameRecordCounter[1] += 1
        elif playerCoins >= 200:
            print("You have reached 200 coins! You win!")
            gameRecordCounter[0] += 1
        else:
            print("You have won " + str(roundRecordCounter[0]) + pluralize(" round", roundRecordCounter[0]) + ", lost " +
                  str(roundRecordCounter[1]) + pluralize(" round", roundRecordCounter[1]) + " and tied " +
                  str(roundRecordCounter[2]) + pluralize(" round", roundRecordCounter[1]) + " against the computer.")

            print("You currently have " + str(playerCoins) + pluralize(" coin", playerCoins) + ".")
            continue
    else:
        if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                      # quit. No else is needed since the program will just keep running normally if this is false.
            quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
            continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop conditions
                      # below don't detect an invalid input and print that out.
        print("Invalid option, please try again, ")

    print("You have won " + str(gameRecordCounter[0]) + pluralize(" game", gameRecordCounter[0]) + " and lost " +
              str(gameRecordCounter[1]) + pluralize(" game", gameRecordCounter[1]))

    while True:  # this while loop continues running until it breaks out (or the program quits)
            # keepPlaying is an input that checks if the user wants to continue or quit. The 'quit' options is handled
            # in the checkIfQuit function.
            keepPlaying = checkIfQuit(str(
                input("Would you like to keep playing? Type 'continue' to play again and 'quit' to exit. ")))

            if quitFlag:  # this checks if quit has been called (quitFlag is only set to true if the user recently typed
                          # quit. N o else is needed since the program will just keep running normally if this is false.
                quitFlag = False  # this sets quitFlag to False because the current quit instance has been handled
                continue  # restart the loop, bringing the user back to the gameMode prompt. This is so the loop
                          # conditions below don't detect an invalid input and print that out.

            if keepPlaying == "continue":  # condition that runs if the user would like to keep playing.
                                           # ('continue' was entered)
                print("Program restarting...")  # prints out that the program is restarting
                playerCoins = 100  # this resets playerCoins to its initial starting value of 100
                betCounter = 0      # this resets betCounter to its initial starting value of 0
                roundRecordCounter = [0, 0, 0]  # this resets the roundRecordCounter for the new game
                break  # breaks out of this while loop to restart the main while loop
            else:      # since 'quit' and 'continue' were already handled, the option entered must be invalid if this
                       # runs.
                       # Note that the while loop will go back to keepPlaying since the while loop hasn't ended.
                print("Invalid input, please try again.")  # prints out that the user's input is invalid.
