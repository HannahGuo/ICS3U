# Hannah Guo
# May 9th 2018
# ICS3UR
# This program acts as a calculator and can perform the addition, subtraction, multiplication, division, exponent,
# modulus, square root and cube root operations. It accepts a number, followed by the operation, then the second number
# from user inputs, then outputs the solution. (Except in the square root and cube root operators where it performs the
# specified chosenOperation to the first number entered.)

print("This program is a calculator, and allows the user to perform the addition, subtraction, multiplication, "
      "division, exponent, modulus, square root\nand cube root operations mathematical operations.")

keepCalculating = True
operations = ["+", "-", "*", "/", "^", "%", "sqrt", "cbrt"]
while keepCalculating:
    while True:
        try:
            firstNum = float(input("Please input your first number (float or integer): "))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            break

    while True:
        chosenOperation = str(input("Please input your desired operation by entering the operation's code, which can be"
                                    " found between the single quotation marks. The available symbols that can be used "
                                    "are:\n"
                                    "'+' for addition\n"
                                    "'-' for subtraction\n"
                                    "'*' for multiplication\n"
                                    "'/' for division\n"
                                    "'^' for exponents\n"
                                    "'%' for modulus\n"
                                    "'sqrt' for finding the square root (note this function can't accept negative "
                                    "numbers)\n"
                                    "'cbrt' for finding the cube root (note this function can't accept negative "
                                    "numbers)\n"))

        while firstNum < 0 and (chosenOperation == operations[6] or chosenOperation == operations[7]):
            try:
                firstNum = float(input("This function does not accept negative numbers, please enter a positive "
                                       "number: "))
            except ValueError:
                print("Invalid input, please try again. ")
            else:
                if firstNum > 0:
                    break
                print("Invalid input, please try again. ")

        if chosenOperation == operations[6]:
            print("The square root of " + str(firstNum) + " is " + str(firstNum ** (1.0 / 2.0)) + ".")
            break
        elif chosenOperation == operations[7]:
            print("The cube root of " + str(firstNum) + " is " + str(firstNum ** (1.0 / 3.0)) + ".")
            break

        if chosenOperation in operations:
            while True:
                try:
                    secondNum = float(input("Please input your second number (float or integer): "))
                except ValueError:
                    print("Invalid input, please try again.")
                else:
                    break
            if chosenOperation == operations[0]:
                print(str(firstNum) + " + " + str(secondNum) + " = " + str(firstNum + secondNum))
            elif chosenOperation == operations[1]:
                print(str(firstNum) + " - " + str(secondNum) + " = " + str(firstNum - secondNum))
            elif chosenOperation == operations[2]:
                print(str(firstNum) + " * " + str(secondNum) + " = " + str(firstNum * secondNum))
            elif chosenOperation == operations[3]:
                print(str(firstNum) + " / " + str(secondNum) + " = " + str(firstNum / secondNum))
            elif chosenOperation == operations[4]:
                print(str(firstNum) + " ^ " + str(secondNum) + " = " + str(firstNum ** secondNum))
            else:
                print(str(firstNum) + " % " + str(secondNum) + " = " + str(firstNum % secondNum))
            break
        else:
            print("An invalid operator has been entered, please try again.")

    while True:
        userInput = str(input("Enter 'continue' to make another calculation, enter 'quit' to exit. "))
        if userInput == "quit":
            keepCalculating = False
            print("The program has ended.")
        elif userInput == "continue":
            print("Program restarting... ")
        else:
            print("Invalid input, please try again. ")
            continue
        break
