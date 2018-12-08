# Hannah Guo
# April 18th 2018
# ICS3UR
# This program prints out a multiplication table (from 1 to 10) for the user's input. A negative or float value can be
# entered.

print("This program generates a multiplication table for the user's inputted number.")  # brief program description,
                                                                                        # printed for the user.

# receives the input for what number to generate a multiplication for. The value is cast to a float to handle if a
# float value is entered, and will also work for an integer.
userInput = float(input("Input the number you would like to generate a multiplication table for: "))

for i in range(1, 11):  # this loops through the numbers between 1 and 10 (inclusive). The stop range is 11 because a
                        # Python for loop's stop parameter is exclusive, meaning it must be one greater than what is
                        # needed. This means the loop will run 10 times.
    print(str(userInput) + " x " + str(i) + " = " + str(userInput * i))  # this prints out the multiplication equation
                                                                         # of the user's inputted number and the current
                                                                         # value of i. All the variable values are cast
                                                                         # to a string for string concatenation.