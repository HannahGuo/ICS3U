# Hannah Guo
# April 18th 2018
# ICS3UR
# This program prints out the sum and average of a set amount of grades. The program asks the user how many grades will
# be entered (how many students are in the class), and this value is later used in a loop to find the summation of the
# grades and to calculate the average.

print("This program calculates the sum and the average of an inputted set of grades.")  # brief program description,
                                                                                        # printed for the user.

numGrades = int(input("Input how many students are in your class: "))  # receives the user's input for how many grades
                                                                       # the program will receive from the user.
sumGrades = 0  # counter for the sum of the grades

if numGrades <= 0:  # this condition runs if the number of grades entered is invalid. It doesn't require an else because
                    # the program will run normally if numGrades is valid.
    print("The number of grades entered was invalid, the following calculations are useless.")  # prints out that the
                                                                                                # number of grades
                                                                                                # entered is invalid

for i in range(numGrades):  # Since the loop starts at 0 and has a stop parameter that is exclusive, it runs however
                            # many times its stop parameter is. In this case, it runs for numGrades, which was specified
                            # by the user earlier. Note that this will not run if numGrades is invalid, since the range
                            # functions begins at 0 by default, and nothing runs to the ending bound of a negative/zero
                            # number.
    enteredGrade = int(input("Enter in a grade: "))  # prompts the user to enter in a grade as an integer, cast to an
                                                     # integer for comparison operators and integer addition later.
                                                     # Final grades are also always given as integers and not floats.

    if not 0 <= enteredGrade <= 100:                 # if condition checking if the grade inputted is not valid (i.e. it
                                                     # is not between 0 and 100). There is no else statement because
                                                     # the entered grade is always added to the sum (regardless if it is
                                                     # invalid or not). Basically, there is no special condition needed
                                                     # for valid numbers, whereas with invalid numbers, an extra print
                                                     # out is needed.

        # print out that the entered grade was invalid
        print("An invalid grade has been entered. The average and sum calculations will not be accurate.")

    sumGrades += enteredGrade  # adds the entered grade to the total sum of grades

print("The average of these grades is " + str(sumGrades / numGrades) + ".")  # this prints out the average of the
                                                                             # grades, which is the sum of the grades
                                                                             # divided by how many grades were entered
                                                                             # (numGrades, which was entered by the
                                                                             # user). Since the quotient of sumGrades
                                                                             # and numGrades isn't a string, cast it to
                                                                             # a string for string concatenation

print("The sum of these grades is " + str(float(sumGrades)) + ".")  # this prints out the sum of the grades, which is
                                                                    # just the counter sumGrades. sumGrades is cast to
                                                                    # a float so it's the same format as the average,
                                                                    # then a string for string concatenation
