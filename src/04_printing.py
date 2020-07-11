"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %2d, y is %5.2f, z is "%s" ' % (x, y, z))

# Use the 'format' string method to print the same thing

print('x is {x:2d}, y is {y:5.2f}, z is "{z}"'.format(**locals()))

# Finally, print the same thing using an f-string
fmsg = f'x is {x}, y is {y:5.2f}, z is "{z}"'
print(fmsg)
