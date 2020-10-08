#! python3

#  In math, if a quadratic equation is in the format
# ax^2 + bx + c = 0, the discriminant can be calculated as
# b^2 - 4 * a * c
# If the discriminant is a perfect square, the equation can
# be factored.  Furthermore, if the discriminant is negative,
# then the equation has no solutions (not used in this assignment).
# Have the user enter in values for a, b and c and then 
# tell them if the equation can be factored.

# Inputs:
# - 3 numbers (a, b, c)

# Outputs:
# - "the equation can be factored"
# - "the equation can not be factored"

a = input("a is ")
b = input("b is ")
c = input("c is ")
a = float(a)
b = float(b)
c = float(c)

R = b ** 2 - 4 * a * c


import math

if R < 0:
    print("the equation can not be factored")
elif math.sqrt(R) % 1 == 0:
    print("the equation can be factored")
else:
    print("the equation can not be factored")
