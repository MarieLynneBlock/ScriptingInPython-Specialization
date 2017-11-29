# -------------------------------------------------------------------------------------------------
# 
# PRACTICE EXERSISES 1 - EXPRESSIONS
#
# Solve each of the practice exercises below. 
# 
# -------------------------------------------------------------------------------------------------


"""
1.1

There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles.
"""



# TEMPLATE

###################################################
# Miles to feet conversion formula
# Student should enter statement on the next line.



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#68640



# SOLUTION

###################################################
# Miles to feet conversion formula
# Student should enter statement on the next line.
print(13 * 5280)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#68640


# -------------------------------------------------------------------------------------------------


"""
1.2

Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.
"""



# TEMPLATE

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497



# SOLUTION

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.
print((7 * 60 + 21) * 60 + 37)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497


# -------------------------------------------------------------------------------------------------


"""
1.3

The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides. Write a Python statement that calculates
and prints the length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches.
"""



# TEMPLATE 

###################################################
# Rectangle perimeter formula
# Student should enter statement on the next line.



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#22



# SOLUTION

###################################################
# Rectangle perimeter formula
# Student should enter statement on the next line.
print(4 * 2 + 7 * 2)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#22


# -------------------------------------------------------------------------------------------------


"""
1.4

The area of a rectangle is wh, where w and h are the lengths of its sides. Note that the multiplication operation is not shown
explicitly in this formula. This is standard practice in mathematics, but not in programming. Write a Python statement that
calculates and prints the area in square inches of a rectangle with sides of length 4 and 7 inches.
"""



# TEMPLATE 

###################################################
# Rectangle area formula
# Student should enter statement on the next line.


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#28



# SOLUTION

###################################################
# Rectangle area formula
# Student should enter statement on the next line.
print(4 * 7)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#28


# -------------------------------------------------------------------------------------------------


"""
1.5

The circumference of a circle is 2πr where r is the radius of the circle. Write a Python statement that calculates and prints the
circumference in inches of a circle whose radius is 8 inches. Assume that the constant π=3.14.
"""



# TEMPLATE

###################################################
# Circle circumference formula
# Student should enter statement on the next line.



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#50.24



# SOLUTION

###################################################
# Circle circumference formula
# Student should enter statement on the next line.
print(2 * 3.14 * 8)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#50.24


# -------------------------------------------------------------------------------------------------


"""
1.6

The area of a circle is πr**2 where r is the radius of the circle. (The raised 2 in the formula is an exponent.) Write a Python statement
that calculates and prints the area in square inches of a circle whose radius is 8 inches. Assume that the constant π=3.14.
"""



# TEMPLATE

###################################################
# Circle area formula
# Student should enter statement on the next line.


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#200.96



# SOLUTION

###################################################
# Circle area formula
# Student should enter statement on the next line.
print(3.14 * 8 ** 2)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#200.96


# -------------------------------------------------------------------------------------------------


"""
1.7

Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is p(1+0.01r)y.
(Remember that you don't need to understand how this formula works, only how to translate it into Python.)
Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.
"""



# TEMPLATE

###################################################
# Future value formula
# Student should enter statement on the next line.



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729



# SOLUTION

###################################################
# Future value formula
# Student should enter statement on the next line.
print(1000 * (1 + 0.01 * 7) ** 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729


# -------------------------------------------------------------------------------------------------


"""
1.8

Write a single Python statement that combines the three strings "𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜", "your first name (x)" and "your surname (y)" (plus a
couple of other small strings) into one larger string "𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 (x) (y)." and prints the result. (Hint: Experiment with adding two
strings in Python using the + operator.)
"""



# TEMPLATE

###################################################
# Name tag formula
# Student should enter statement on the next line.


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is (x) (y).



# SOLUTION

###################################################
# Name tag formula
# Student should enter statement on the next line.
print("My name is " + "Marie-Lynne" + " " + "Block" + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is (x) (y).


# -------------------------------------------------------------------------------------------------


"""
1.9

Write a Python expression that creates the string "(x) (y) 𝚒𝚜 (z) 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍." from several strings including "your first name your surname"
and the number (z) and then prints the result (Hint: Use the function 𝚜𝚝𝚛 to convert the number into a string.)
"""



# TEMPLATE

###################################################
# Name and age formula
# Student should enter statement on the next line.


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# (x) (y) is (z) years old.



# SOLUTION

###################################################
# Name and age formula
# Student should enter statement on the next line.
print("Marie-Lynne Block" + " is " + str(27) + " years old.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# (x) (y) is (z) years old.


# -------------------------------------------------------------------------------------------------


"""
1.extra

The distance between two points (x0,y0) and (x1,y1) is √(x0−x1)**2+(y0−y1)**2. Write a Python statement that calculates
and prints the distance between the points (2,2) and (5,6). (Hint: Remember that a square root can be computed by raising a value to the 0.5 power.)
"""



# TEMPLATE

###################################################
# Distance formula
# Student should enter statement on the next line.

# Hint: You need to use the power operation ** .


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0



# SOLUTION

###################################################
# Distance formula
# Student should enter statement on the next line.
print(((2 - 5) ** 2 + (2 - 6) ** 2) ** 0.5)

# Hint: You need to use the power operation ** .


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0
