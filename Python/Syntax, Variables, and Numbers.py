# 0.
# This is a silly question intended as an introduction to the format we use for hands-on exercises throughout all Kaggle courses.

# **What is your favorite color? **

# To complete this question, create a variable called color in the cell below with an appropriate value. The function call q0.check() (which we've already provided in the cell below) will check your answer.

color = 'blue'


# 1.
# Complete the code below. In case it's helpful, here is the table of available arithmetic operations:
# Operator	Name	Description
# a + b	Addition	Sum of a and b
# a - b	Subtraction	Difference of a and b
# a * b	Multiplication	Product of a and b
# a / b	True division	Quotient of a and b
# a // b	Floor division	Quotient of a and b, removing fractional parts
# a % b	Modulus	Integer remainder after division of a by b
# a ** b	Exponentiation	a raised to the power of b
# -a	Negation	The negative of a

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = radius ** 2 * pi


# 2.
# Add code to the following cell to swap variables a and b (so that a refers to the object previously referred to by b and vice versa).

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
# a = [1, 2, 3]
# b = [3, 2, 1]
# q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

#a, b = b, a


# 3a.
# Add parentheses to the following expression so that it evaluates to 1.

# 5 - 3 // 2
#(5 - 3) // 2


# 3b. 🌶️
# Questions, like this one, marked a spicy pepper are a bit harder.

# Add parentheses to the following expression so that it evaluates to 0.

# 8 - 3 * 2 - 1 + 1
#(8 - 3) * (2 - (1 + 1))


# 4.
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.


# alice_candies = 121 
# bob_candies = 77
# carol_candies = 109

# print(alice_candies + bob_candies + carol_candies) % 3