###
# Author: Randy Shaw
# Date: 1/21/2017
# Class: SSW-567
# Python Version: Python27
# Assignment: P0: Triangle function
#
#Part 3: Use your tools on a simple program to identify different types of triangles.
#You are to write a program, execute, and do preliminary testing on a simple program.  
#Requirements: Write a function classifyTriangle() that takes three  parameters: a, b, and c. 
#The three parameters represent the lengths of the sides of a triangle. 
#The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, 
#and whether it is a right triangle as well.
#
#Please include an opening comment in the script with your name and the purpose of the program.
###

print "----------------------------------------------------------------------"
print "----------------------------------------------------------------------"
print "--     Welcome to Randy Shaw's Triangle Analysis Program  ------------"
print "----------------------------------------------------------------------"
print "--  This program will request 3 numbers that represent the sides    --"
print "--  of a triangle and them return if the triangle is scalene,       --"
print "--  isosceles, or equilateral, and if it is a right triangle.       --"
print "----------------------------------------------------------------------"
print "----------------------------------------------------------------------"
print "" 
import sys
from array import *

retry = 0
Triangle_Sides = array('f',[0.0,0.0,0.0])
num_sides = 3
Isosceles = 0
myfile = open("out.txt","w")
CR_str = "\n"

################################## FUNCTIONS ############################################
#----------------------------------------------------------------------------------------------
### Function for Splitting String into seperate words
def printTriangle (trianglearray):
    counter = 0
    number_of_entries = len(trianglearray)
    while (counter < number_of_entries):
     print "Side ", counter+1, " equals   ", trianglearray[counter]
     sidenum_str = str(counter)
     sideLen_str = str(trianglearray[counter])
     mystr = ("Side " + sidenum_str + " equals   " + sideLen_str + CR_str)
     myfile.write(mystr)
     counter=counter+1
    print ""
    return number_of_entries
### Determine if we have a valid triangle
def validTriangle (validarray):
    # determine if we have a valid triangle
    valid_triangle = 0
    Valid_Sides = sorted(validarray)
    # determine if the lengths form a valid triangle
    Sum_of_two_shorter_sides = Valid_Sides[0] + Valid_Sides[1]
    if ( Valid_Sides[2] < Sum_of_two_shorter_sides ):
     #Since the sum of the two shorter sides is greater than the longer side we have a valid triangle
     valid_triangle = 1
    else:
     #Since the sum of the two shorter sides is less than or equal to the longer side this is NOT a valid triangle
     valid_triangle = 0
    print ""
    return valid_triangle
### Is the triangle an isosceles triangle?
def isoscelesTriangle (isoarray):
    Is_Isosceles = 0
    # determine if 2 sides are equal, meaning we have an isosceles triangle
    sides_sorted = sorted(isoarray)
    shorter_sides_equal = (sides_sorted[0] == sides_sorted[1])
    longer_sides_equal = (sides_sorted[2] == sides_sorted[1])
    if (shorter_sides_equal or longer_sides_equal):
     #if long or short side equals middle side, we have an isosceles
     Is_Isosceles = 1
    else:
     Is_Isosceles = 0
		 # if not isosceles, it is a scalene triangle, 3 unequal sides
    return Is_Isosceles
### Is the triangle a right triangle?
def rightTriangle (rightarray):
    Is_Right = 0
    sorted_sides = sorted(rightarray)
    #if the pythagorean theorem holds, it is a right triangle
    hyp_squared = sorted_sides[2]**2
    a_squared = sorted_sides[0]**2
    b_squared = sorted_sides[1]**2
    a_squ_plus_b_squ = a_squared + b_squared
    if ( hyp_squared == a_squ_plus_b_squ ):
     #if the pythagorean theorem holds, it is a right triangle
     Is_Right = 1
    else:
     Is_Right = 0
		 #if not, it is a notright triangle
    return Is_Right
### Is the triangle a right triangle?
def equilateralTriangle (equiarray):
    Is_Equi = 0
    # determine if we have an equilateral triangle
    max_side = max(equiarray)
    min_side = min(equiarray)
    if ( max_side == min_side ):
     # set Is_Equi
     Is_Equi = 1
    return Is_Equi
### Function for classifying a valid triangle
def classifyTriangle (validTriangle):
    Isosceles = isoscelesTriangle(validTriangle)
    if (Isosceles == 1):
     print "Since at least two sides are the same length"
     print "This is an isosceles triangle"
     print ""
     myfile.write("This is an isosceles triangle\n")
    else:
     print "Since all 3 sides are different lengths, it is a scalene triangle"
		 # if not isosceles or equilateral, it is a scalene triangle, 3 unequal sides
     print ""
     myfile.write("This is a scalene triangle\n")
    Right = rightTriangle (validTriangle)
    if (Right == 1):
     # statement
     print "Since the pythagorean theorem holds, this is a right triangle"
     print ""
     myfile.write("This is a right triangle\n")
    Equi = equilateralTriangle (validTriangle)
    if (Equi == 1):
     # statement
     print "Since all sides are the same length the triangle is also an equilateral triangle"
     print ""
     myfile.write("This is an equilateral triangle\n")
    myfile.write("\n")
    return Equi
######################## Main Program ######################################################
# Allowing user to classify multiple triangles without having to exit and reopen the program
while (retry < 1):
   try:
     print "" 
     # this needs to be in a repeating try statement
     User_Input=(raw_input("Please Enter the length of the first side of the triangle:"))
     # validating that the parameter entered by the user is a numerical value
     Triangle_Sides[0] = float (User_Input)
     # Check validity of entry
     if (Triangle_Sides[0] <= 0.0):
     	print "Side of a triangle must be greater than 0.0", Triangle_Sides[0]
     	# adding extra print space for easier readability
     	print "" 
     User_Input=(raw_input("Please Enter the length of the second side of the triangle:"))
     Triangle_Sides[1] = float (User_Input)
     # Check validity of entry
     if (Triangle_Sides[1] <= 0.0):
     	print "Side of a triangle must be greater than 0.0", Triangle_Sides[1]
     User_Input=(raw_input("Please Enter the length of the third side of the triangle:"))
     Triangle_Sides[2] = float (User_Input)
     # Check validity of entry
     if (Triangle_Sides[2] <= 0.0):
     	print "Side of a triangle must be greater than 0.0", Triangle_Sides[2]
     print "" 
     arraylength = printTriangle(Triangle_Sides)
     valid_tri = 0
     valid_tri = validTriangle(Triangle_Sides)
     if (valid_tri == 1):
      myfile.write("We have a valid triangle\n")
      print "Since the sum of the two shorter sides is greater than the longer side"
      print "we have a valid triangle"
      # only classify valid triangles
      classification = classifyTriangle(Triangle_Sides)
     else:
     	print "Since the sum of the two shorter sides is less than the longer side we DO NOT have a valid triangle"
     	myfile.write("we DO NOT have a valid triangle\n\n")
     print ""
     # Allowing user to continue converting numbers without having to exit and reopen the program
     Retry_Input=(raw_input("Would you like to enter another triangle (y/n)?")) 
     # Kick Out Value is less than 1
     if (Retry_Input !=  "y"):
      retry = 1
      myfile.close()
     else: 
     	retry = 0
   # If the user's entry is not a numerical value
   except ValueError as e:
   	# adding extra print space for easier readability
   	print "" 
   	# customized the exception print message
   	print "Whoops, the value you entered is not an number. Please Try Again." 
# adding extra print space for easier readability
print "" 
#signing off
print "Thank you, Goodbye" 
   
sys.exit()
