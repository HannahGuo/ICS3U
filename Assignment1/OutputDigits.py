# Hannah Guo
# February 23rd 2018
# ICS3UR
# This program splits and prints out a 3-digit number (inputted by the user) into its values of the hundreds, tens and
# ones columns. It uses the modulus function to calculate the value of each column, which is shown below.

print("This program splits a 3-digit number into hundreds, tens and ones.")  # brief program description for the user
num = int(input("Please input a 3-digit number: "))                          # user inputs number

ones = num % 10                 # calculates the ones column, which is the remainder when the number is divided by 10

tens = (num % 100) - ones       # calculates the tens column, which is the remainder when the number is divided by 100,
                                # and the previously calculated ones column is subtracted

hundreds = num - (ones + tens)  # calculates the hundreds column, which is the remainder when the number is divided by
                                # 100, and the previously calculated ones and tens column are subtracted

print(str(hundreds) + " " + str(tens) + " " + str(ones))  # prints out the hundreds, tens and ones values
