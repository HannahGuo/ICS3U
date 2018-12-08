# Hannah Guo
# April 18th 2018
# ICS3UR
# This program calculates when the population of bees will exceed the nest's food supply. The given conditions of this
# hive were that after every hour, the number of bees would double and the amount of honey would be increased to
# accommodate an additional 2000 bees.

# brief program description, printed for the user
print("This program calculates when the population of bees will exceed the nest's food supply using given conditions.")

beeCounter = 5      # this keeps track of how many bees are in the nest
honeyCounter = 500  # this keeps track of how many bees the current amount of honey in the nest can feed
hourCount = 0       # this keeps track of how many hours have gone by since the beginning of the nest

while beeCounter <= honeyCounter:  # this loops runs as long as there is more or enough honey to feed the current number
                                   # of bees (i.e. if the number of bees is less than or equal to the amount of honey
                                   # required for that many bees, then there is enough honey)
    beeCounter *= 2                # doubles the number of bees
    honeyCounter += 2000           # adds honey that will feed 2000 bees to the nest
    hourCount += 1                 # adds 1 to the hourCount as an hour has gone by (hourCount will be the equivalent of
                                   # how many times this while loop has run)

print("The bee population will exceed their food supply after " + str(hourCount) + " hours.")  # prints out after how
                                                                                               # many hours the bee
                                                                                               # population will exceed
                                                                                               # their food supply.
                                                                                               # hourCount is cast to a
                                                                                               # string for
                                                                                               # concatenation