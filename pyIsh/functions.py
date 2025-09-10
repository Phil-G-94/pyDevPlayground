# Functions #

# Functions are defined using the `def` keyword

# Function w/o params #


# def hello_world():
#     print("HelloWorld")


# hello_world()

# # Function w/ params #


# def add_two(a, b):
#     name = "Steve"  # scoped to fn block
#     print(f"{name} a + b = {a + b}")


# add_two(1, 2)

# global statement #

# scopes a variable to the global scope, instead of local scope (i.e. within a function)
# it is impossible to assign a value to a variable defined outside a function without the global statement
# once we scope the variable to the global scope
# we can change the value of the variable
# and have it reflected outside of the function as well

# x = "HelloWorld"

# def printX():

#     global x

#     print(f"x is {x}")  # prints nothing

#     x = 12

#     print(f"now x is {x}")


# printX()
# # x is HelloWorld
# # now x is 12

# print(x)
# # 12

# without global keyword #

# x = "Hello World"


# def printX():
#     # print(
#     #     f"x is {x}"  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     # )

#     x = 12

#     print(f"x is now {x}")


# printX()  # x is now 12

# print(x)  # Hello World

# default argument values #


# def say(message, times=2):
#     print(message * times)
#     print(f"{message} has been printed {times} times")


# say("Hello World")

# say("Hello World", times=3)

# keyword arguments #

# allow us to specify only some arguments when calling the function
# unspecified arguments fall back to default values


# def many_args(a, b=5, c=10):
#     print(f"a is {a}", f"b is {b}", f"c is {c}", sep=" ")


# many_args(2, c=10)

# """
# Output:
# a is 2 b is 5 c is 10
# """

# many_args(10, 10, 10)

# """
# Output:
# a is 10 b is 10 c is 10
# """

# VarArgs parameters - variable arguments #
# when we declare a starred parameter as *param, then all positional args from that point until the end are collected as a tuple called 'param'
# when we declare a double-starred parameter as **param, then all the keyword arguments from that point until end are collected as a dictionary called 'param'
# positional arguments => arguments passed without explicitly naming the parameter. assigned to parameters in the order that they appear.
# keyword arguments => arguments passed by explicitly naming the paramter in the form key=value


# def var_args(a=5, *numbers, **phonebook):
#     print(f"a is {a}")

#     for item in numbers:
#         print(f"Item is {item}")

#     print(numbers)  # (1, 2, 3) - tuple

#     for first_part, second_part in phonebook.items():
#         print(f"{first_part}, {second_part}")

#     print(phonebook)  # {'Jack': 1123, 'John': 2231, 'Inge': 1560}


# var_args(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)

# return statement #

# used to return from a fn, i.e break out or return a value


# def fn(x):
#     return x

# DocStrings #
# Used to specify what the function does and what types of args it expects


def printMax(x: int, y: int):
    """
    Prints the maximum of two numbers.

    The two values must be integers.
    """

    x = int(x)
    y = int(y)

    if x > y:
        print(f"The bigger number is {x}")
    elif y > x:
        print(f"The bigger number is {y}")
    else:
        print("I don't know which number is bigger")


printMax(40, 4)  # Output: The bigger number is 40

print(printMax.__doc__)

"""
Output:
Prints the maximum of two numbers.

The two values must be integers.
"""
