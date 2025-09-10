# Modules #

# can have the .py
# or the .pyc extension - write modules in C

# import sys  # import module using `import` statement | the sys module contains information pertaining to the interpreter and its environment

# print("The command line arguments are: ")

# for i in sys.argv:
#     print(i, sep="\n", end="\n")

# print("\n\nThe PYTHONPATH is", sys.path, "\n")

# we can also use from..import syntax #

# from math import sqrt

# print(f"the square root of 16 is {round(sqrt(16))}")

# Import your own modules #

# import mymodule

# mymodule.say_hi("John")

# from mymodule import say_hi, __version__

# say_hi("John")

# the `dir` function - returns the list of names defined by an object #
# if object is a module - returns list includes functions, classes/variables etc. defined inside the module

"""
python -> enter REPL
import sys
dir(sys)
# returns names of attributes in sys module
"""
