# Hannah Guo
# March 29th 2018
# ICS3UR
# This program evaluates credit card application based on the user inputs of the user's age, how long they've lived at
# their current address, their annual income and how many years they've worked at their current job. It uses a point
# system to add and subtract points based on these inputs, and decides on a final action based on the number of points
# a user has accumulated.

# brief program description, printed for the user
print("This program outputs a credit card evaluation based on user inputs.")

# This is the point counter used throughout the program. It is added/subtracted from based on the user's inputs, which
# can be seen below.
points = 0

age = int(input("Please input your age: "))  # receive an age input, cast to an integer for comparison operators later

if age > 50:           # condition checking if the user is older than 50
    points += 25       # add 25 points to the point counter if the condition above is true
elif 31 <= age <= 50:  # condition checking if the user is between 31 and 50 years old (inclusive)
    points += 20       # add 20 points to the point counter if the condition above is true
elif 21 <= age <= 30:  # condition checking if the user is between 21 and 30 years old (inclusive)
    points = points    # no point value change if the condition above is true
else:                  # for this else to run, the user must be either 20 years old or under, or the user inputted an
                       # invalid age (negative).
    points -= 10       # subtract 10 points from the point counter when all the if/elif conditions above are false
    if age < 0:        # if the age is invalid, the program will still assign the lowest point value for this category
                       # and will also print out that this input is invalid.
        print("Invalid input, the lowest point value for your age (-10) will be used to calculate points.")  # prints
                                                                                                             # that the
                                                                                                             # input was
                                                                                                             # invalid

# receive an input for how long the user has lived at their current address, cast to an integer for comparison operators
# later
howLongAtCurrentAddress = int(input("Please input how many years you have lived at your current address: "))

if howLongAtCurrentAddress > 8:          # condition checking if the user has lived at their current address for over 8
                                         # years
    points += 20                         # add 20 points to the point counter if the condition above is true
elif 4 <= howLongAtCurrentAddress <= 8:  # condition checking if the user has lived at their current address for 4 to 8
                                         # years (inclusive)
    points += 12                         # add 12 points to the point counter if the condition above is true
elif 1 <= howLongAtCurrentAddress <= 3:  # condition checking if the user has lived at their current address for 1 to 3
                                         # years (inclusive)
    points += 5                          # add 5 points to the point counter if the condition above is true
else:                                    # for this else to run, the user must not have lived at their current address
                                         # for over a year (0 years) or have entered an invalid input (negative)
    points -= 5                          # subtract 5 points from the point counter when all the if/elifs conditions
                                         # above are false
    if howLongAtCurrentAddress < 0:      # if the number of years is invalid, the program will still assign the lowest
                                         # point value for this category and will also print out that this
                                         # input is invalid
        print("Invalid input, the lowest point value for the number of years you have lived at your current address "
              "(-5) will be used to calculate points.")  # prints that the input was invalid


# receive an input for the user's annual income, cast to an integer for comparison operators later
annualIncome = int(input("Please input your annual income ($): "))

if annualIncome >= 40000:                # condition checking if the user's annual income is at or over $40000
    points += 30                         # add 30 points to the point counter if the condition above is true
elif 25000 <= annualIncome < 40000:      # condition checking if the user's annual income is at or above $25000 and
                                         # below $40000
    points += 24                         # add 24 points to the point counter if the condition above is true
elif 15000 <= annualIncome < 25000:      # condition checking if the user's annual income is at or above $15000 and
                                         # below $25000
    points += 12                         # add 12 points to the point counter if the condition above is true
else:                                    # for this else to run, the user must have an annual income lower than $15000
                                         # or have entered an invalid input (negative)
    points = points                      # no change in points when all the if/elifs conditions above are false
    if annualIncome < 0:                 # if their entered annual income is invalid, the program will still assign the
                                         # lowest point value for this category and will also print out that this input
                                         # is invalid
        print("Invalid input, the lowest point value for your annual income (0) will be used to calculate "
              "points.")  # prints that the input was invalid

# receive an input for how many years the user has worked at the same job, cast to an integer for comparison operators
# later
yearsAtSameJob = int(input("Please input how many years you have been working at the same job for: "))

if yearsAtSameJob > 4:                   # condition checking if the user has worked at their current job for over 4
                                         # years
    points += 15                         # add 15 points to the point counter if the condition above is true
elif 2 <= yearsAtSameJob <= 4:           # condition checking if the user has worked at their current job for between 2
                                         # and 4 years (inclusive)
    points += 8                          # add 8 points to the point counter if the condition above is true
else:                                    # for this else to run, the user must have worked at their job for less than 2
                                         # years or have entered an invalid input (negative)
    points -= 4                          # subtract 4 points from the point counter when all the if/elifs conditions
                                         # above are false
    if yearsAtSameJob < 0:               # if the number of years is invalid, the program will still assign the lowest
                                         # point value for this category and will also print out that this
                                         # input is invalid
        print("Invalid input, the lowest point value for the number of years you have worked at the same job (-4) will "
              "be used to calculate points.")  # prints that the input was invalid

if points <= 20:                                       # condition checking if the user's point value is less than or
                                                       # equal to 20 points
    print("Sorry, you cannot receive a credit card.")  # prints out that the user is illegible to receive a credit card
elif 21 <= points <= 35:                               # condition checking if the user's point value is between 21 and
                                                       # 35 (inclusive)
    print("You can receive a credit card with $500 limit.")  # prints out that the user can receive a credit card with
                                                             # a $500 limit
elif 36 <= points <= 60:                               # condition checking if the user's point value is between 36 and
                                                       # 60 (inclusive)
    print("You can receive a credit card with a $2000 limit.")  # prints out that the user can receive a credit card
                                                                # with a $2000 limit
else:                                                  # if all the conditions above are false, then the user must have
                                                       # over 60 points
    print("You can receive a credit card with a $5000 limit.")  # prints out that the user can receive a credit card
                                                                # with a $5000 limit
