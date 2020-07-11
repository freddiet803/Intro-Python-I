# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(aNum):
    if int(aNum) % 2 == 0:
        return True
    else:
        return False


print(is_even(5), ' is even function')

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def input_is_even(aNum):
    if(aNum % 2 == 0):
        print("Even!")
    else:
        print("Odd!")


input_is_even(num)
