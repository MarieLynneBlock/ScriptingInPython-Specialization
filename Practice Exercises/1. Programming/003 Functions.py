# -------------------------------------------------------------------------------------------------
# 
# PRACTICE EXERSISES 3 - FUNCTIONS
#
# Solve each of the practice exercises below. 
# Note that many of these exercises focus on converting a mathematical formula in an equivalent Python expression.
# For these exercises, I will always provide the formula. Your task is to write the Python expression:
#
# -------------------------------------------------------------------------------------------------


"""
3.1

Write a Python function 𝚖𝚒𝚕𝚎𝚜_𝚝𝚘_𝚏𝚎𝚎𝚝 that takes a parameter 𝚖𝚒𝚕𝚎𝚜 and returns the number of feet in 𝚖𝚒𝚕𝚎𝚜 miles.
"""



# TEMPLATE

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.


miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# 13 miles equals 68640 feet.
# 57 miles equals 300960 feet.
# 82.67 miles equals 436497.6 feet.



# SOLUTION


###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.
def miles_to_feet(miles):
    """
    Returns the number of feet in the given number of miles.
    """
    
    return miles * 5280


###################################################
# Tests
# Student should not change this code.


miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# 13 miles equals 68640 feet.
# 57 miles equals 300960 feet.
# 82.67 miles equals 436497.6 feet.


# -------------------------------------------------------------------------------------------------


"""
3.2

Write a Python function 𝚝𝚘𝚝𝚊𝚕_𝚜𝚎𝚌𝚘𝚗𝚍𝚜 that takes three parameters 𝚑𝚘𝚞𝚛𝚜, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜 and
returns the total number of seconds for 𝚑𝚘𝚞𝚛𝚜 hours, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 minutes and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜 seconds.
"""



# TEMPLATE

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# 7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
# 10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
# 1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.



# SOLUTION

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.
def total_seconds(hours, minutes, seconds):
    """
    Returns the number of seconds in the given number of hours, minutes, and seconds.
    """
    
    return (hours * 60 + minutes) * 60 + seconds


###################################################
# Tests
# Student should not change this code.

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# 7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
# 10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
# 1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.


# -------------------------------------------------------------------------------------------------


"""
3.3

Write a Python function 𝚛𝚎𝚌𝚝𝚊𝚗𝚐𝚕𝚎_𝚙𝚎𝚛𝚒𝚖𝚎𝚝𝚎𝚛 that takes two parameters 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 corresponding
to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.
"""



# TEMPLATE

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.


width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
# A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
# A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.



# SOLUTION

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.
def rectangle_perimeter(width, height):
    """
    Returns the perimeter of a rectangle with the given width and height.
    """
    
    return width * 2 + height * 2


###################################################
# Tests
# Student should not change this code.


width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
# A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
# A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.


# -------------------------------------------------------------------------------------------------


"""
3.4

Write a Python function 𝚛𝚎𝚌𝚝𝚊𝚗𝚐𝚕𝚎_𝚊𝚛𝚎𝚊 that takes two parameters 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 corresponding to
the lengths of the sides of a rectangle and returns the area of the rectangle in square inches. 
"""



# TEMPLATE

###################################################
# Rectangle area formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
# A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
# A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.



# SOLUTION

###################################################
# Rectangle area formula
# Student should enter function on the next lines.
def rectangle_area(width, height):
    """
    Returns the area of a rectangle with the given width and height.
    """
    
    return width * height


###################################################
# Tests
# Student should not change this code.

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
# A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
# A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.


# -------------------------------------------------------------------------------------------------


"""
3.5

Write a Python function 𝚌𝚒𝚛𝚌𝚕𝚎_𝚌𝚒𝚛𝚌𝚞𝚖𝚏𝚎𝚛𝚎𝚗𝚌𝚎 that takes a single parameter 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to
the radius of a circle in inches and returns the the circumference of a circle with radius 𝚛𝚊𝚍𝚒𝚞𝚜
in inches. Do not use π = 3.14, instead use the 𝚖𝚊𝚝𝚑 module to supply a higher-precision approximation to π.
"""



# TEMPLATE

import math
PI = math.pi

###################################################
# Circle circumference formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
# A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
# A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.



# SOLUTION

import math
PI = math.pi

###################################################
# Circle circumference formula
# Student should enter function on the next lines.

def circle_circumference(radius):
    """
    Returns the circumference of a circle of the given radius.
    """
    
    return 2 * PI * radius


###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
# A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
# A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.


# -------------------------------------------------------------------------------------------------


"""
3.6

Write a Python function 𝚌𝚒𝚛𝚌𝚕𝚎_𝚊𝚛𝚎𝚊 that takes a single parameter 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to the radius
of a circle in inches and returns the the area of a circle with radius 𝚛𝚊𝚍𝚒𝚞𝚜 in square inches.
Do not use π = 3.14, instead use the 𝚖𝚊𝚝𝚑 module to supply a higher-precision approximation to π.
"""



# TEMPLATE

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A circle with a radius of 8 inches has an area of 201.06192983 square inches.
# A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
# A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.



# SOLUTION

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula
# Student should enter function on the next lines.

def circle_area(radius):
    """
    Returns the area of a circle of the given radius.
    """
    return PI * radius ** 2


###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A circle with a radius of 8 inches has an area of 201.06192983 square inches.
# A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
# A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.


# -------------------------------------------------------------------------------------------------


"""
3.7

Write a Python function 𝚏𝚞𝚝𝚞𝚛𝚎_𝚟𝚊𝚕𝚞𝚎 that takes three parameters 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎, 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎 and 𝚢𝚎𝚊𝚛𝚜
and returns the future value of 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎 dollars invested at 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎 percent interest,
compounded annually for 𝚢𝚎𝚊𝚛𝚜 years.
"""



# TEMPLATE

###################################################
# Future value formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.


present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
# The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
# The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.



# SOLUTION

###################################################
# Future value formula
# Student should enter function on the next lines.
def future_value(present_value, annual_rate, years):
    """
    Returns the future value of the given money invested at an annual
    interest rate, compounded annually for the given number of years.
    """
    
    return present_value * (1 + 0.01 * annual_rate) ** years


###################################################
# Tests
# Student should not change this code.


present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
# The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
# The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.


# -------------------------------------------------------------------------------------------------


"""
3.8

Write a Python function 𝚗𝚊𝚖𝚎_𝚝𝚊𝚐 that takes as input the parameters 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎 (strings)
and returns a string of the form "𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 % %." where the percents are the strings
𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎. Reference the test cases in the provided template for an exact description
of the format of the returned string.
"""



# TEMPLATE

###################################################
# Name tag formula
# Student should enter function on the next lines.


    
###################################################
# Tests
# Student should not change this code.
    
    
first_name, last_name = "Jesper", "Ase"
print(name_tag(first_name, last_name))

first_name, last_name = "Lien", "Block"
print(name_tag(first_name, last_name))

first_name, last_name = "Anthony", "Claessen"
print(name_tag(first_name, last_name))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# My name is Jesper Ase.
# My name is Lien Block.
# My name is Anthony Claessen.



# SOLUTION

###################################################
# Name tag formula
# Student should enter function on the next lines.
def name_tag(first_name, last_name):
    """
    Returns a name tag string with the given name.
    """
    
    return "My name is " + first_name + " " + last_name + "."

    
###################################################
# Tests
# Student should not change this code.
    
    
first_name, last_name = "Jesper", "Ase"
print(name_tag(first_name, last_name))

first_name, last_name = "Lien", "Block"
print(name_tag(first_name, last_name))

first_name, last_name = "Anthony", "Claessen"
print(name_tag(first_name, last_name))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# My name is Jesper Ase.
# My name is Lien Block.
# My name is Anthony Claessen.


# -------------------------------------------------------------------------------------------------


"""
3.9

Write a Python function 𝚗𝚊𝚖𝚎_𝚊𝚗𝚍_𝚊𝚐𝚎 that takes as input the parameters 𝚗𝚊𝚖𝚎 (a string)
and 𝚊𝚐𝚎 (a number) and returns a string of the form "% 𝚒𝚜 % 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍."
where the percents are the string forms of 𝚗𝚊𝚖𝚎 and 𝚊𝚐𝚎. Reference the test cases in the
provided template for an exact description of the format of the returned string.
"""



# TEMPLATE

###################################################
# Name and age formula
# Student should enter function on the next lines.



###################################################
# Tests
# Student should not change this code.

    
name, age = "Tim Janssen", 31
print(name_and_age(name, age))

name, age = "Lien Block", 27
print(name_and_age(name, age))

name, age = "Anthony Claessen", 46
print(name_and_age(name, age))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Tim Janssen is 31 years old.
# Lien Block is 27 years old.
# Anthony Claessen is 46 years old.



# SOLUTION

###################################################
# Name and age formula
# Student should enter function on the next lines.
def name_and_age(name, age):
    """
    Returns a string stating the person's age.
    """
    
    return name + " is " + str(age) + " years old."


###################################################
# Tests
# Student should not change this code.


name, age = "Tim Janssen", 31
print(name_and_age(name, age))

name, age = "Lien Block", 27
print(name_and_age(name, age))

name, age = "Anthony Claessen", 46
print(name_and_age(name, age))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Tim Janssen is 31 years old.
# Lien Block is 27 years old.
# Anthony Claessen is 46 years old.


# -------------------------------------------------------------------------------------------------


"""
3.10

Write a Python function 𝚙𝚘𝚒𝚗𝚝_𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎 that takes as input the parameters 𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷 and 𝚢_𝟷,
and returns the distance between the points (x0,y0) and (x1,y1).
"""



# TEMPLATE

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .


###################################################
# Tests
# Student should not change this code.


x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The distance from (2, 2) to (5, 6) is 5.0.
# The distance from (1, 1) to (2, 2) is 1.41421356237.
# The distance from (0, 0) to (3, 4) is 5.0.



# SOLUTION

###################################################
# Distance formula
# Student should enter function on the next lines.
def point_distance(x_0, y_0, x_1, y_1):
    """
    Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
    """
    
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
# Hint: You need to use the power operation ** .


###################################################
# Tests
# Student should not change this code.


x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The distance from (2, 2) to (5, 6) is 5.0.
# The distance from (1, 1) to (2, 2) is 1.41421356237.
# The distance from (0, 0) to (3, 4) is 5.0.


# -------------------------------------------------------------------------------------------------


"""
3.11 [Challenge]

Write a Python function 𝚝𝚛𝚒𝚊𝚗𝚐𝚕𝚎_𝚊𝚛𝚎𝚊 that takes the parameters
𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷,𝚢_𝟷, 𝚡_𝟸, and 𝚢_𝟸 (all numbers),and returns the area of the triangle
with vertices (x0,y0), (x1,y1) and (x2,y2).
(Hint: use the function 𝚙𝚘𝚒𝚗𝚝_𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎 as a helper function and apply Heron's formula.)
"""



# TEMPLATE

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Use point_distance as a helper function.




###################################################
# Tests
# Student should not change this code.

def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""
    
    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
# A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
# A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.



# SOLUTION

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Use point_distance as a helper function.

def point_distance(x_0, y_0, x_1, y_1):
    """
    Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
    """
    
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
    
def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """
    Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2).
    """
    
    # Compute the lengths of the three sides.
    len_01 = point_distance(x_0, y_0, x_1, y_1)
    len_02 = point_distance(x_0, y_0, x_2, y_2)
    len_12 = point_distance(x_1, y_1, x_2, y_2)
    
    # Compute the semi-perimeter length, i.e., half of the perimeter length.
    semi_perim = (len_01 + len_02 + len_12) / 2
    
    # Compute the area according to Heron's formula.
    return (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_12)) ** 0.5


###################################################
# Tests
# Student should not change this code.

def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""
    
    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
# A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
# A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.


# -------------------------------------------------------------------------------------------------


"""
3.12 [Challenge]

Write a Python function 𝚙𝚛𝚒𝚗𝚝_𝚍𝚒𝚐𝚒𝚝𝚜 that takes an integer 𝚗𝚞𝚖𝚋𝚎𝚛 in the range [0,100),
(i.e., at least 0, but less than 100) and prints the message "𝚃𝚑𝚎 𝚝𝚎𝚗𝚜 𝚍𝚒𝚐𝚒𝚝 𝚒𝚜 %,
𝚊𝚗𝚍 𝚝𝚑𝚎 𝚘𝚗𝚎𝚜 𝚍𝚒𝚐𝚒𝚝 𝚒𝚜 %.", where the percent signs should be replaced with the appropriate values.
(Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits.)
Note that this function should print the desired message, rather than returning it as a string.
"""



# TEMPLATE

###################################################
# Digits function
# Student should enter function on the next lines.



    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The tens digit is 4, and the ones digit is 2.
# The tens digit is 9, and the ones digit is 9.
# The tens digit is 0, and the ones digit is 5.



# SOLUTION

###################################################
# Digits function
# Student should enter function on the next lines.
def print_digits(number):
    """
    Prints the tens and ones digit of an integer in [0,100).
    """
    
    print("The tens digit is " + str(number // 10) + ", and the ones digit is " + 
          str(number % 10) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# The tens digit is 4, and the ones digit is 2.
# The tens digit is 9, and the ones digit is 9.
# The tens digit is 0, and the ones digit is 5.


# -------------------------------------------------------------------------------------------------


"""
3.13 [Challenge]

Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery
ticket with a specific number combination and, if the number on the ticket matches the numbers
generated in a random drawing, the player wins a massive jackpot.
Write a Python function 𝚙𝚘𝚠𝚎𝚛𝚋𝚊𝚕𝚕that takes no arguments and prints the message
"𝚃𝚘𝚍𝚊𝚢'𝚜 𝚗𝚞𝚖𝚋𝚎𝚛𝚜 𝚊𝚛𝚎 %, %, %, %, 𝚊𝚗𝚍 %. 𝚃𝚑𝚎 𝙿𝚘𝚠𝚎𝚛𝚋𝚊𝚕𝚕 𝚗𝚞𝚖𝚋𝚎𝚛 𝚒𝚜 %.".
The first five numbers should be random integers in the range [1,60),
i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct,
but for this problem, we will allow duplicates. The Powerball number is a random integer
in the range [1,36), i.e., at least 1 but less than 36.
Note that this function should print the desired message, rather than returning it as a string. 

tip: import the 𝚛𝚊𝚗𝚍𝚘𝚖 module and then use the function 𝚛𝚊𝚗𝚍𝚘𝚖.𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎() to generate the appropriate random numbers.
"""



# TEMPLATE

import random

###################################################
# Powerball function
# Student should enter function on the next lines.



    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.



# SOLUTION

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    """
    Prints Powerball lottery numbers.
    """
    
    # Note that including the optional argument end = "" to print() cause
    # print to NOT generate a newline
    
    print("Today's numbers are " + str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "") 
    print(str(random.randrange(1, 60)) + ", and ", end = "")
    print(str(random.randrange(1, 60)) + ". The Powerball number is ",  end = "") 
    print(str(random.randrange(1, 36)) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
# Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
# Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
# Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.

