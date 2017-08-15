# -------------------------------------------------------------------------------------------------
# 
# PRACTICE EXERSISES 2 - VARIABLES AND ASSIGNMENTS
#
# Solve each of the practice exercises below. 
# Note that many of these exercises focus on converting a mathematical formula in an equivalent Python
# expression.
# For these exercises, I will always provide the formula. Your task is to write the Python expression:
#
# -------------------------------------------------------------------------------------------------


"""
2.1

Given a template that pre-defines a variable 𝚖𝚒𝚕𝚎𝚜, write an assignment statement that defines a variable
𝚏𝚎𝚎𝚝 whose value is the number of feet in 𝚖𝚒𝚕𝚎𝚜 miles.
"""



# TEMPLATE

# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
miles = 13


# Test 2
miles = 57


# Test 3
miles = 82.67


###################################################
# Miles to feet conversion formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print str(miles) + " miles equals " + str(feet) + " feet."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.



# SOLUTION

# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
miles = 13


# Test 2
miles = 57


# Test 3
miles = 82.67


###################################################
# Miles to feet conversion formula
# Student should enter formula on the next line.
feet = miles * 5280


###################################################
# Test output
# Student should not change this code.

print str(miles) + " miles equals " + str(feet) + " feet."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.


# -------------------------------------------------------------------------------------------------


"""
2.2 

Given a template that pre-defines three variables 𝚑𝚘𝚞𝚛𝚜, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜, write an assignment
statement that updates the variable 𝚝𝚘𝚝𝚊𝚕_𝚜𝚎𝚌𝚘𝚗𝚍𝚜 to have a value corresponding to the total number
of seconds for 𝚑𝚘𝚞𝚛𝚜 hours, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 minutes and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜 seconds.
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
hours = 7
minutes = 21
seconds = 37


# Test 2
hours = 10
minutes = 1
seconds = 7


# Test 3
hours = 1
minutes = 0
seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds) + " seconds.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
hours = 7
minutes = 21
seconds = 37


# Test 2
hours = 10
minutes = 1
seconds = 7


# Test 3
hours = 1
minutes = 0
seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.
total_seconds = (hours * 60 + minutes) * 60 + seconds


###################################################
# Test output
# Student should not change this code.

print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds) + " seconds.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.


# -------------------------------------------------------------------------------------------------


"""
2.3

Given a template that pre-defines the variables 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 that are the lengths of the sides
of a rectangle, write an assignment statement that defines a variable 𝚙𝚎𝚛𝚒𝚖𝚎𝚝𝚎𝚛 whose value is the
perimeter of the rectangle in inches.
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
width = 4
height = 7


# Test 2
width = 7
height = 4


# Test 3
width = 10
height = 10


###################################################
# Rectangle perimeter formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(perimeter) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
width = 4
height = 7


# Test 2
width = 7
height = 4


# Test 3
width = 10
height = 10


###################################################
# Rectangle perimeter formula
# Student should enter formula on the next line.
perimeter = width * 2 + height * 2


###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(perimeter) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.


# -------------------------------------------------------------------------------------------------


"""
2.4

Given a template that pre-defines the variables 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 that are the lengths of the sides
of a rectangle, write an assignment statement that defines a variable 𝚊𝚛𝚎𝚊 whose value is the area
of the rectangle in square inches.
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
width = 4
height = 7


# Test 2
width = 7
height = 4


# Test 3
width = 10
height = 10


###################################################
# Rectangle area formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(area) + " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
width = 4
height = 7


# Test 2
width = 7
height = 4


# Test 3
width = 10
height = 10


###################################################
# Rectangle area formula
# Student should enter formula on the next line.
area = width * height


###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(area) + " square inches.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.


# -------------------------------------------------------------------------------------------------


"""
2.5

Given a template that pre-defines the constant 𝙿𝙸 and the variable 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to the
radius of a circle in inches, write an assignment statement that defines a variable 𝚌𝚒𝚛𝚌𝚞𝚖𝚏𝚎𝚛𝚎𝚗𝚌𝚎
whose value is the circumference of a circle with radius 𝚛𝚊𝚍𝚒𝚞𝚜 in inches.
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1
radius = 8


# Test 2
radius = 3


# Test 3
radius = 12.9


###################################################
# Circle circumference formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      "inches has a circumference of " + str(circumference) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has a circumference of 50.24 inches.

# Test 2 output:
#A circle with a radius of 3 inches has a circumference of 18.84 inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has a circumference of 81.012 inches.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1
radius = 8


# Test 2
radius = 3


# Test 3
radius = 12.9


###################################################
# Circle circumference formula
# Student should enter formula on the next line.
circumference = 2 * PI * radius


###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circumference) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has a circumference of 50.24 inches.

# Test 2 output:
#A circle with a radius of 3 inches has a circumference of 18.84 inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has a circumference of 81.012 inches.


# -------------------------------------------------------------------------------------------------


"""
2.6

Given a template that pre-defines the constant 𝙿𝙸 and the variable 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to the
radius of a circle in inches, write an assignment statement that defines a variable 𝚊𝚛𝚎𝚊 whose
value is the area of a circle with radius 𝚛𝚊𝚍𝚒𝚞𝚜 in square inches
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1
radius = 8


# Test 2
radius = 3


# Test 3
radius = 12.9


###################################################
# Circle area formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(area) + " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has an area of 200.96 square inches.

# Test 2 output:
#A circle with a radius of 3 inches has an area of 28.26 square inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has an area of 522.5274 square inches.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1
radius = 8


# Test 2
radius = 3


# Test 3
radius = 12.9


###################################################
# Circle area formula
# Student should enter formula on the next line.
area = PI * radius ** 2


###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(area) + " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has an area of 200.96 square inches.

# Test 2 output:
#A circle with a radius of 3 inches has an area of 28.26 square inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has an area of 522.5274 square inches.


# -------------------------------------------------------------------------------------------------


"""
2.7

Given the pre-defined variables 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎, 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎 and 𝚢𝚎𝚊𝚛𝚜, write an assignment statement
that define a variable 𝚏𝚞𝚝𝚞𝚛𝚎_𝚟𝚊𝚕𝚞𝚎 whose value is 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎 dollars invested at 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎
percent interest, compounded annually for 𝚢𝚎𝚊𝚛𝚜 years
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
present_value = 1000
annual_rate = 7
years = 10


# Test 2
present_value = 200
annual_rate = 4
years = 5


# Test 3
present_value = 1000
annual_rate = 3
years = 20


###################################################
# Future value formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print("The future value of $" + str(present_value) + " in " + str(years) + 
      "years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.

# Test 2 output:
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.

# Test 3 output:
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
present_value = 1000
annual_rate = 7
years = 10


# Test 2
present_value = 200
annual_rate = 4
years = 5


# Test 3
present_value = 1000
annual_rate = 3
years = 20


###################################################
# Future value formula
# Student should enter formula on the next line.
future_value = present_value * (1 + 0.01 * annual_rate) ** years


###################################################
# Test output
# Student should not change this code.

print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.

# Test 2 output:
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.

# Test 3 output:
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.


# -------------------------------------------------------------------------------------------------


"""
2.8

Give the pre-defined variables 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎, write an assignment statement that defines
the variable 𝚗𝚊𝚖𝚎_𝚝𝚊𝚐 whose value is the string "My name is % %." where the percents should be
replaced by 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎. Remember that, in Python, you can use the + operator on
strings to concatenate (i.e. join) them together into a single string. 
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
first_name = "Lien"
last_name = "Block"


# Test 2
first_name = "Anthony"
last_name = "Claessen"


# Test 3
first_name = "Jesper"
last_name = "Ase"


###################################################
# Name tag formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print(name_tag)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#My name is Lien Block.

# Test 2 output:
#My name is Tim Janssen.

# Test 3 output:
#My name is Anthony Claessen.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
first_name = "Lien"
last_name = "Block"


# Test 2
first_name = "Tim"
last_name = "Janssen"


# Test 3
first_name = "Anthony"
last_name = "Claessen"


###################################################
# Name tag formula
# Student should enter formula on the next line.
name_tag = "My name is " + first_name + " " + last_name + "."


###################################################
# Test output
# Student should not change this code.

print(name_tag)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#My name is Lien Block.

# Test 2 output:
#My name is Tim Janssen.

# Test 3 output:
#My name is Anthony Claessen.


# -------------------------------------------------------------------------------------------------


"""
2.9

Given the pre-defined variables 𝚗𝚊𝚖𝚎 (a string) and 𝚊𝚐𝚎 (a number), write an assignment statement
that defines a variable 𝚜𝚝𝚊𝚝𝚎𝚖𝚎𝚗𝚝 whose value is the string "% 𝚒𝚜 % 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍." where the percents
should be replaced by 𝚗𝚊𝚖𝚎 and the string form of 𝚊𝚐𝚎.
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
name = "Lien Block"
age = 27


# Test 2
name = "Tim Janssen"
age = 31


# Test 3
name = "Anthony Claessen"
age = 46


###################################################
# Name and age formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

print(statement)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#Lien Block is 27 years old.

# Test 2 output:
#Tim Janssen is 31 years old.

# Test 3 output:
#Anthony Claessen is 46 years old.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
name = "Lien Block"
age = 27


# Test 2
name = "Tim Janssen"
age = 31


# Test 3
name = "Anthony Claessen"
age = 46


###################################################
# Name and age formula
# Student should enter formula on the next line.
statement = name + " is " + str(age) + " years old."


###################################################
# Test output
# Student should not change this code.

print(statement)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#Lien Block is 27 years old.

# Test 2 output:
#Tim Janssen is 31 years old.

# Test 3 output:
#Anthony Claessen is 46 years old.


# -------------------------------------------------------------------------------------------------


"""
2.10 (!)

Given the variables 𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷, and 𝚢_𝟷, write an assignment statement that defines a variable
𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎 whose values is the distance between the points (x0,y0) and (x1,y1).
"""



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
x_0 = 2
y_0 = 2
x_1 = 5
y_1 = 6


# Test 2
x_0 = 1
y_0 = 1
x_1 = 2
y_1 = 2


# Test 3
x_0 = 0
y_0 = 0
x_1 = 3
y_1 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.

# Hint: You need to use the power operation ** .


###################################################
# Test output
# Student should not change this code.

print("The distance from (" + str(x_0) + ", " + str(y_0) + 
      ") to (" + str(x_1) + ", " + str(y_1) + ") is " + str(distance) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
x_0 = 2
y_0 = 2
x_1 = 5
y_1 = 6


# Test 2
x_0 = 1
y_0 = 1
x_1 = 2
y_1 = 2


# Test 3
x_0 = 0
y_0 = 0
x_1 = 3
y_1 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.
distance = ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
# Hint: You need to use the power operation ** .


###################################################
# Test output
# Student should not change this code.

print("The distance from (" + str(x_0) + ", " + str(y_0) + 
      ") to (" + str(x_1) + ", " + str(y_1) + ") is " + str(distance) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.


# -------------------------------------------------------------------------------------------------


"""
2.11 (!)

 Heron's formula states the area of a triangle is √s(s−a)(s−b)(s−c) where a, b and c
 are the lengths of the sides of the triangle and s=12(a+b+c) is thesemi-perimeterof the triangle.
 Given the variables 𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷, 𝚢_𝟷, 𝚡_𝟸, and 𝚢_𝟸, write a Python program that computes a variable
 𝚊𝚛𝚎𝚊 whose value is the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: the
 solution uses five assignment statements.)
 """



# TEMPLATE

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
x_0, y_0 = 0, 0
x_1, y_1 = 3, 4
x_2, y_2 = 1, 1


# Test 2
x_0, y_0 = -2, 4
x_1, y_1 = 1, 6
x_2, y_2 = 2, 1


# Test 3
x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.



###################################################
# Test output
# Student should not change this code.

print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + ")," + 
      "(" + str(x_1) + "," + str(y_1) + "), and" + 
      "(" + str(x_2) + "," + str(y_2) + ") has an area of " + str(area) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.0.



# SOLUTION

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1
x_0, y_0 = 0, 0
x_1, y_1 = 3, 4
x_2, y_2 = 1, 1


# Test 2
x_0, y_0 = -2, 4
x_1, y_1 = 1, 6
x_2, y_2 = 2, 1


# Test 3
x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.
len_01 = ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
len_02 = ((x_0 - x_2) ** 2 + (y_0 - y_2) ** 2) ** 0.5
len_12 = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
semi_perim = (len_01 + len_02 + len_12) / 2
area = (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_12)) ** 0.5


###################################################
# Test output
# Student should not change this code.

print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + ")," + 
      " (" + str(x_1) + "," + str(y_1) + "), and" + 
      " (" + str(x_2) + "," + str(y_2) + ") has an area of " + str(area) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.0.
