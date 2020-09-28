#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

a = input("One side is ")
b = input("One side is ")
c = input("The hypotenuse is ")
a = float(a)
b = float(b)
c = float(c)
import math
c2 = math.sqrt(a ** 2 + b ** 2)

if 0 <= c2 - c <= 0.02:
    print("that is a right triangle")
elif c2 -c > 0.02:
    print("that is an acute triangle")
elif c2 -c < 0:
    print("that is an obtuse triangle")
