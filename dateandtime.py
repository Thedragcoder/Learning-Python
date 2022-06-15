# write a program to display the current date and time
import datetime
from datetime import date


def currentdandt():
    now = datetime.datetime.now()
    print("The current time is : ")
    print(now.strftime("%Y-%M-%d %H:%M:%S")
          )

# write a program to input the radius and display the area of circle


def areaofcircle():
    pi = 3.14
    takeUsersInput = int(input("Enter the radius : "))
    calculatedResult = pi * (takeUsersInput**2)
    print(calculatedResult)


# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def nameInRevese():
    firstName = input("Enter your first name please: ")
    secondName = input("Enter your second name please: ")
    print(f"{secondName} {firstName}")

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.


def convertListAndTuple():
    UsersInput = input("Please enter the data separated with comma: ")
    convertedList = UsersInput.split(",")
    ChangeToTuple = tuple(convertedList)
    print("List: ", convertedList)
    print("Tuples: ", ChangeToTuple)

# Write a Python program to accept a filename from the user and print the extension of that.


def fileNamePrinter():
    fileWithName = input("Please enter the name with file extension: ")
    fileExtension = fileWithName.split(".")
    print("The extension is : " + repr(fileExtension[-1]))

# Write a Python program to display the first and last colors from the following list.


def firstLastColors():
    color_list = ["Red", "Green", "White", "Black"]
    print(color_list[::3])

# Write a Python program to display the examination schedule


def examDate():
    examStartsFrom = (11, 12, 2014)
    print("The exam starts form %i-%i-%i" % examStartsFrom)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn


def computeValue():
    valueToCompute = int(input("Enter the number"))
    restComputedValues = (valueToCompute ** 2) + \
        (valueToCompute * valueToCompute * valueToCompute)
    computedValue = valueToCompute + restComputedValues
    print(computedValue)


# write a program to calulate days left
def remainingDays():
    ldate = date(2022, 8, 10)
    fdate = date(2022, 5, 28)
    daysleft = fdate - ldate
    print(daysleft.days)


remainingDays()
