# Hannah Guo
# May 9th 2018
# ICS3UR
# This program provides the average and median grade for a teacher's class after they have entered how many students
# are in their class and the grades those students received. It also outputs how many students are in each (A to F),
# how many passed or failed the course, the percentage of students that received each grade and the percentage of how
# many passed or failed the course. The program also runs continuously until the user tells it to quit at the end of
# each class.

print("This program receives the grade ranges of a classroom, and outputs the average and median grades, \nas well "
      "as how many students are within each grade category and how many are passing or failing. \nThese are also shown"
      " as percentages of the entire class.")

keepCalculating = True
while keepCalculating:
    gradeRanges = [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0]]
    grades = []
    sumGrades = 0
    courseCode = str(input("Hello! What is the course code for this class? "))

    while True:
        try:
            numStudents = float(input("Please input how many students there are in the '" + courseCode + "' class "
                                      "(a positive integer greater than 0): "))
        except ValueError:
            print("Invalid input, please input a positive integer greater than 0.")
        else:
            if numStudents > 0 == numStudents % 1:
                numStudents = int(numStudents)
                break
            print("Invalid input, please input a positive integer greater than 0.")

    for i in range(numStudents):
        while True:
            try:
                enteredGrade = float(input("Please input a grade (number between 0 and 100): "))
            except ValueError:
                print("Invalid grade input, please input a number between 0 and 100.")
            else:
                if 0 <= enteredGrade <= 100:
                    sumGrades += enteredGrade
                    grades.append(enteredGrade)
                    if 80 <= enteredGrade:
                        gradeRanges[0][1] += 1
                    elif 70 <= enteredGrade:
                        gradeRanges[1][1] += 1
                    elif 60 <= enteredGrade:
                        gradeRanges[2][1] += 1
                    elif 50 <= enteredGrade:
                        gradeRanges[3][1] += 1
                    elif 40 <= enteredGrade:
                        gradeRanges[4][1] += 1
                    else:
                        gradeRanges[5][1] += 1
                    break
                print("Invalid grade input, please input an integer between 0 and 100.")

    studentsFailed = gradeRanges[4][1] + gradeRanges[5][1]
    print(str(numStudents - studentsFailed) + " students passed the '" + courseCode + "' class and " +
          str(studentsFailed) + " students failed! This means that " +
          "{0:.2f}".format(100 - (studentsFailed / numStudents) * 100) + "% of students passed and "
          "{0:.2f}".format((studentsFailed / numStudents) * 100) + "% of students failed.")

    grades.sort()
    median = float(grades[int((len(grades) - 1) / 2)] if len(grades) % 2 != 0 else
                   (grades[int((len(grades) - 1) / 2)] + grades[int((len(grades) - 1) / 2) + 1]) / 2)

    print("The average grade was " + "{0:.2f}".format((sumGrades / numStudents)) +
          ". The average is the sum of the grades divided by the number of grades. "
          "\nThe median grade was " + str("{0:.2f}".format(median)) + ". Median means "
          "the middle value in an ordered set of values, or the average of the two middle numbers.")

    for counter in range(6):
        if (gradeRanges[counter][1]) != 0:
            print(str(gradeRanges[counter][1]) + " student(s) received the " + str(
                gradeRanges[counter][0]) + " grade in the '" + courseCode + "' class. This is " +
                  "{0:.2f}".format((gradeRanges[counter][1] / numStudents) * 100.0) + "% of the students in the class.")

    while True:
        userInput = str(input(
            "Would you like to calculate another class? Enter 'yes' to continue and 'no' to exit. "))
        if userInput == "no":
            keepCalculating = False
            print("The program has ended.")
        elif userInput == "yes":
            print("Program restarting... ")
        else:
            print("Invalid input, please try again. ")
            continue
        break
