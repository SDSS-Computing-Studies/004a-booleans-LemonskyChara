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

a = float(input("One side is "))
b = float(input("One side is "))
c = float(input("The hypotenuse is "))

import math
d = math.sqrt(a ** 2 + b ** 2)

if 0 <= d - c <= 0.02:
    print("that is an acute triangle")
elif d -c > 0.02:
    print("that is an obtuse triangle")
elif d -c < 0:
    print("that is a right triangle")
