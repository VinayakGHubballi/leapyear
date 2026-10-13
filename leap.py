import sys

def leapYear(year):
    if(year%4 == 0):
        print("Leap year")
    else:
        print("Not a leap year")

year = int(sys.argv[1])
leapYear(year)