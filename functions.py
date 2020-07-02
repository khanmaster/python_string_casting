# what is a function?

# Why should we use function
# what is the benefit - REUSEIBILITY OF CODE
# What functions have we used so far?
# DRY - don't repeat yourself

# syntax:- def name of the function with () and :
# # create a function to greeting
# def greeting():
#     return "Hello world"
#      # pass # - is used to skip the function
#
# # how do we call the a function
# print(greeting())
# # very example of creating a function and calling it with return statement to display string message
#
# def test():
#     pass # it will skip the methods and there will be no outcome
#          # it is used in creating or building a unit test

# methods with Parameters/arguments
# create a function with two args to return a subtraction of the 2 values given
def add_values(number1, number2):
    return number1 + number2 # we can return anything- string - int with + operator

# print(add_values())
print(add_values(4, 5))

# create a function with two args to return a subtraction of the 2 values given

# create a function with two args to return a division of the 2 values given


# create a function with two args to return a remainder of  of the 2 values given


# create a function with two args to return a * of the 2 values given






# create a function with multiple args

def multi_args(*args):

    for arg in args:
        print(arg)

    return arg

print(multi_args(1, 2, 3, 4,5))






