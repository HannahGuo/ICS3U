# Hannah Guo
# May 9th 2018
# ICS3UR
# This program prints out the "Necklace Problem" that was introduced in the program's problem. The
# 'necklace' problem starts off with the user inputting two positive single-digit integers. The next number of the
# necklace is obtained by finding the one's digit column of the sum of the two previous digits. The necklace ends when
# the two numbers that were entered are repeated (in succession).

print("This program solves the 'Necklace Problem', where two integers are entered by the user, and the program uses"
      " the 'necklace' algorithm to complete the pattern. \nThe 'necklace' problem starts off with the user inputting "
      "two positive single-digit integers. \nThe next number of the necklace is obtained by finding the one's digit "
      "column of the sum of the two previous digits. \nThe necklace ends when the two numbers that were entered are "
      "repeated (in succession).")

keepCalculating = True
while keepCalculating:
    successful = False
    firstNum, secondNum, counter = (0,) * 3

    while True:
        try:
            firstNum = float(input("Input the first number (single-digit integer) that starts the necklace: "))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            if 10 > firstNum >= 0 == firstNum % 1:
                firstNum = int(firstNum)
                break
            print("Invalid input, please try again.")

    while True:
        try:
            secondNum = float(input("Input the second number (single-digit integer) that starts the necklace: "))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            if 10 > secondNum >= 0 == secondNum % 1:
                secondNum = int(secondNum)
                break
            print("Invalid input, please try again.")

    prevNum = firstNum
    currentNum = secondNum

    print("Starting Number: " + str(firstNum) + "\nThe number(s) in this necklace is/are: "
                                                "\nCurrent number on necklace: "
          + str(secondNum))

    while not successful:
        temp = prevNum
        prevNum = currentNum
        currentNum = (currentNum + temp) % 10
        counter += 1

        if currentNum == secondNum and prevNum == firstNum:
            successful = True
            print("Last Number: " + str(currentNum) + "\nThis necklace took " + str(counter) + " steps to complete.")
        else:
            print("Current number on necklace: " + str(currentNum))

    while True:
        userInput = str(input("Enter 'continue' to solve another necklace (restart the program), "
                              "enter 'quit' to exit. "))
        if userInput == "quit":
            keepCalculating = False
            print("The program has ended.")
        elif userInput == "continue":
            print("Program restarting... ")
        else:
            print("Invalid input, please try again. ")
            continue
        break
