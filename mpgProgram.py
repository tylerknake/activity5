# Tyler Knake
# ISQA 3900 - 10/17/2021
# The Miles Per Gallon program - a small application that accepts user input of miles driven and gallons used
# to calculate mpg, saving all three values and writing them to a file called trips.csv.

import csv
import sys

global trips
global trip
global FILENAME

# Exit Program
def exit_program():
    write_trips()
    print("Goodbye.")
    sys.exit()


# Read File - Exception Handling
def read_file():
    global FILENAME
    FILENAME = "trips.csv"
    cont = input("Would you like to read trips from a file? (y/n) ")
    while cont != "y" or "n":
        if cont == "y":
            print_file()
            print()
            break
        elif cont == "n":
            break
        else:
            print("Please enter 'y' or 'n' to answer yes or no.")
            continue

def print_file():
    global FILENAME
    FILENAME = str(input("Please enter csv filename containing input data: "))
    global trips
    try:
        with open(FILENAME) as file:
            #print("Trips: ")
            lines = file.readlines()
            for line in lines:
                vals = line.split(',')
                read_trip = []
                for val in vals:
                    read_trip.append(float(val))

                trips.append(read_trip)
    except FileNotFoundError as e:
        print("Trips not read from file. File not found: " + FILENAME)
    except Exception as e:
        print(type(e), e)
        exit_program()


# Input Trips - Exception Handling
def input_trips():
    global trip
    trip = []
    cont = input("Would you like to enter trip data? (y/n) ")
    while cont != "y" or "n":
        if cont == "y":
            miles_input()
            gallons_input()
            mpg = trip[0] / trip[1]
            mpg = round(mpg, 2)
            trip.append(mpg)
            trips.append(trip)
            print_trip_format()
            print()
            cont = input("Would you like to continue? (y/n) ")
            if cont == "y":
                trip = []
                continue
            if cont == "n":
                exit_program()
        elif cont == "n":
            exit_program()
        else:
            print("Please enter 'y' or 'n' to answer yes or no.")
            continue

def miles_input():
# Finish these
    #global miles_driven
    global trip
    while True:
            try:
                miles_driven = float(input("Enter miles driven:\t\t"))
                if (miles_driven < 0 or miles_driven == str):
                    raise ValueError()
            except ValueError:
                print("Enter positive numeric values only. Try again.")
                continue
            else:
                if miles_driven > 0:
                    trip.append(miles_driven)
                    break

def gallons_input():
    #global gallons_used
    global trip
    while True:
            try:
                gallons_used = float(input("Enter gallons of gas used:\t"))
                if (gallons_used < 0 or gallons_used == str):
                    raise ValueError()
            except ValueError:
                print("Enter positive numeric values only. Try again.")
                continue
            else:
                if gallons_used > 0:
                    # Create conversion to save as a string
                    # Create for loop to put in correct spot
                    trip.append(gallons_used)
                    break


# Format for printing out the trip
def print_trip_format():
    # Create format for printing the rows
    # Requires infamous Nate Moody for loop (Joke from my internship)
    global trips
    count = 0
    for a_trip in trips:
        print("%d. Miles: %-10.2fGallons of Gas: %-10.2fMpg: %.2f" % (count + 1, a_trip[0], a_trip[1], a_trip[2]))
        count += 1


# Write List to Trips.csv
def write_trips():
    global FILENAME
    global trips
    FILENAME = "trips.csv"
    try:
        with open(FILENAME, "w") as file:
            for a_trip in trips:
                file.write(format("%f,%f,%.2f\n" % (a_trip[0], a_trip[1], a_trip[2])))
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()


# Run Program
def main():
    # Initialize Trips 2-D List
    global trips
    trips = []
    # Display Title
    print("The Miles Per Gallon program")
    print()
    # Read File Option
    read_file()
    print_trip_format()
    # Trip Input Option
    input_trips()

if __name__ == "__main__":
    main()
