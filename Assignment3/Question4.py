# Hannah Guo
# April 18th 2018
# ICS3UR
# This program acts as a password checker. It prompts the user to set a password, then checks if they entered the
# correct password later on. As requested by the assignment, it doesn't use an if condition and instead uses a while
# loop.

# brief program description, printed for the user.
print("This program checks if the user entered a password that is the same as their specified password.")

userInput = str(input("Please set your password: "))   # receives the user's input for their password, cast to a string
                                                       # for comparison operators later
attempt = str(input("Check your password: "))          # this prompts the user to enter in a password, cast to a string
                                                       # for comparison operators later

while attempt != userInput:  # this while loop will only exit if this condition is false, meaning if the attempted input
                             # is the same as the userInput (i.e. the correct password has been entered)
    attempt = str(input("Please try again: "))   # this resets the attempt variable to accept a new input (a new
                                                 # password attempt. Then, the while loop runs again to check if this
                                                 # new input is equal to the set password.
print("The correct password has been entered!")  # this prints out that the correct password has been entered. Note that
                                                 # this will only run if the while loop has exited. 
