# SquareCube.py
# Author: Jared Buehner
# Class: SDEV 300
# Professor: Muhammad Khan
# Date: 06/08/2020

# Imports.
import math
import sys

# Menu prompt.
def menu():
    print('\n1. Display Square and Cube Values from 1 to 100\
        \n2. Search the sets for a specific integer and display the square and cube values\
        \n3. Display the union of square and cube sets\
        \n4. Display the intersection of square and cube sets\
        \n5. Display the Difference of Square and Cube sets\n6. Quit Application\n')

# Set of square values.
def square():
    square_list = set()
    for seed_value in range(1, 101):
        square_list.add(int(math.pow(seed_value, 2)))
    return set(square_list)

# Set of cube values.
def cube():
    cube_list = set()
    for seed_value in range(1, 101):
        cube_list.add(int(math.pow(seed_value, 3)))
    return set(cube_list)

# Union of sqaures and cubes.
def square_cube_union():
    print('\nUnion of square and cube sets:', cube_set.union(square_set))

# Intersection of squares and cubes.
def inter_of_sets():
    print('\nIntersection of the square and cube sets:', cube_set.intersection(square_set))

# Difference of sqaures and cubes.
def difference_of_sets():
    print('\nDifference of the square and cube sets:',
          cube_set.difference(square_set))

# Specific integer to find square and cube of.
def search_int():
    try:
        int_input = int(input('\nEnter the integer you would like the square and cube of: '))
        if int_input < 1 or int_input > 100:
            raise ValueError # Sends operation to the error message and loops back.
        print('\nSquare =', str(int_input) + '^2 =', math.pow(int_input, 2))
        print('\nCube =', str(int_input) + '^3 =', math.pow(int_input, 3))
    except:
        ValueError
        print('\nEnter a valid integer between 1 and 100.')

# Creates the sets of integers, square set, and cube set
cube_set = cube()
square_set = square()

# Welcome prompt.
print('\n*** Welcome to the Square and Cube Program ***')

loop = True
# Loops until user selects 6.
while loop:
    # Display menu.
    menu()
    try:
        # Holds user's input in memory.
        userInput = int(input())

        if userInput < 1 or userInput > 6:
            raise ValueError # Sends operation to the error message and loops back.

        if userInput == 1:
            print(sorted(square()))
            print(sorted(cube()))

        if userInput == 2:
            print(sorted(search_int()))

        if userInput == 3:
            print(sorted(square_cube_union()))

        if userInput == 4:
            print(sorted(inter_of_sets()))

        if userInput == 5:
            print(sorted(difference_of_sets()))

        if userInput == 6:
            print('\n*** Thanks for trying the Square and Cube Program ***\n')
            loop = False # Exits the program.

    # Error message if the user inputs an invalid type.
    except:
        ValueError
        print('\nEnter a number 1-6')