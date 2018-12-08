# Hannah Guo
# April 18th 2018
# ICS3UR
# This program prints out a numbers in a pyramid pattern. The program runs until the maximum number, which is received
# from a user input at the beginning of the program.

print("This program prints out numbers in a pyramid pattern based on the user's input.")  # brief program description,
                                                                                          # printed for the user

userInput = int(input("Input the number you would like this pattern to continue on to: "))  # receives the maximum
                                                                                            # number to run the pattern
                                                                                            # to, inputted from the user
                                                                                            # and cast to an integer
                                                                                            # because that's what the
                                                                                            # algorithm uses and what
                                                                                            # the program problem
                                                                                            # required.

if userInput < 0:                                  # this checks if an invalid input has been entered (negative). There
                                                   # is no else statement because the program doesn't need to say if a
                                                   # valid number has been entered, it will just run.
    print("An invalid integer has been entered.")  # prints that an invalid integer has been entered.

for i in range(userInput + 1):  # this loop runs until the value of userInput is reached. Since the stop range of range
                                # is exclusive, add one so that userInput's value is also used in the loop (making it
                                # inclusive, and stopping it at the value after userInput). Note that this loop will not
                                # run if userInput is negative simply because how the range function works (starts at
                                # 0, and the end value is exclusive so if the value was negative, i would never be
                                # within the specified range so it wouldn't run.)
    print(i * str(i))  # up until the maximum number (which was specified by a user input), the program prints out the
                       # number (whatever i is at the time of the loop running) however many times the value of the
                       # number is. For example, when i is 1, the program will print out a line that has 1 once, when i
                       # is 2, the program will print out a line that has 2 twice, etc. The purpose of str(i) is to
                       # ensure that the string value of i is used and not the numerical value of i, otherwise the
                       # value of i ^ 2 would be printed out. Note that if i is 0, then an empty line prints out because
                       # multiplying 0 is nothing.