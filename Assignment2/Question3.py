# Hannah Guo
# March 29th 2018
# ICS3UR
# This program determines a user's astrological sign based on their inputted month (numerically represented) and day by
# using conditional operators and if conditions.

# brief program description, printed for the user
print("This program outputs the user's astrological sign based on an inputted month and day.")

# receive a month input from the user, cast to an integer for comparison operators later
month = int(input("Please enter a month (as a number, i.e. January = 1, February = 2, etc.): "))

# The following logic prints out the user's astrological sign based on the month and date. First, there is an if
# statement that checks if the inputted month is between 1 and 12 (by checking if it's greater than 0 and less than
# or equal to 12. If it is not a valid month, the program will output that an invalid month was entered. If it is a
# valid month, the program will continue.
#
# Here are the assignments for each astrological sign:
# Capricorn: December 22 - January 19
# Aquarius: January 20 - February 18
# Pisces: February 19 - March 20
# Aries: March 21 - April 19
# Taurus: April 20 - May 20
# Gemini: May 21 - June 21
# Cancer: June 22 - July 22
# Leo: July 23 - August 22
# Virgo: August 23 - September 22
# Libra: September 23 - October 23
# Scorpio: October 24 - November 21
# Sagittarius: November 22 - December 21
#
# For each sign, the month and date must be between the range specified. Each range involves the end of one month
# and the beginning of the next. This means that one of two conditions must be met:
#
# a) the date could be within the start date of the first month and last day of the month
# b) the date could be within the start of the next month and the last specified date of that sign
#
# For example, consider the Capricorn astrological sign, which is between December 22nd and January 19th. The
# conditions would be:
# a) if the day is between the 22nd and 31st of December (which is month 12)
# b) if the day is between the 1st and 19th of January (which is month 1)
#
# In code, this is done by using logic gates of "and" and "or".
# Capricorn's sign is determined by the following if statement in the code below:
# if (month == 12 and 22 <= day <= 31) or (month == 1 and 0 < day <= 19)
#
# This means that either side of the "or" statement can evaluate to true for the sign to be a Capricorn. Brackets
# are used to specify that (month == 12 and 22 <= day <= 31) represents one condition and
# (month == 1 and 0 < day <= 19) represents another.
#
# The left side of the "or" is (month == 12 and 22 <= day <= 31), which checks if condition a) is met.
# It checks if month is 12, and if the date is greater than or equal to 22 and less than or equal to 31.
# These two conditions must both be true for the overall condition a) of Capricorn to be met.
#
# The same is done for condition b), but with month == 1 (which is January) and checking if the day is greater than
# 0 (0 is less than (<) day) because no month starts on day 0, and less than or equal to the specified upper limit,
# which is 19.
#
# Either condition a) or condition b) needs to be met in order for the program to print out the Capricorn
# astrological sign. This logic is done for each sign.
#
# The ending else statement nested inside the "if 0 < month <= 12:" checks if a valid date was entered. All days in
# a year are covered in the logic that checks the sign, meaning that if the month is valid (which was checked in
# the first if with the condition 0 < month <= 12), then the date must be invalid. For example, February 31st would be
# an invalid date.

if 0 < month <= 12:
    day = int(input("Please enter a day: "))  # receive a day input, cast to an integer for comparison operators
    if (month == 12 and 22 <= day <= 31) or (month == 1 and 0 < day <= 19):
        print("Your astrological sign is Capricorn.")
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 0 < day <= 18):
        print("Your astrological sign is Aquarius.")
    elif (month == 2 and 19 <= day <= 29) or (month == 3 and 0 < day <= 20):
        print("Your astrological sign is Pisces.")
    elif (month == 3 and 21 <= day <= 31) or (month == 4 and 0 < day <= 19):
        print("Your astrological sign is Aries.")
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 0 < day <= 20):
        print("Your astrological sign is Taurus.")
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 0 < day <= 21):
        print("Your astrological sign is Gemini.")
    elif (month == 6 and 22 <= day <= 30) or (month == 7 and 0 < day <= 22):
        print("Your astrological sign is Cancer.")
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 0 < day <= 22):
        print("Your astrological sign is Leo.")
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 0 < day <= 22):
        print("Your astrological sign is Virgo.")
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 0 < day <= 23):
        print("Your astrological sign is Libra.")
    elif (month == 10 and 24 <= day <= 31) or (month == 11 and 0 < day <= 21):
        print("Your astrological sign is Scorpio.")
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 0 < day <= 21):
        print("Your astrological sign is Sagittarius.")
    else:
        print("An invalid date has been entered.")
else:
    print("An invalid month has been entered.")