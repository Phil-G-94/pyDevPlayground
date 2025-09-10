# Tuples #

# Used to hold together multiple objects
# Similar to lists, but without the extensive functionality included with the `list` class
# Immutable, like strings
# Defined as comma-separated elements within an (optional) pair of parenthesis
# Are sequences

# tuple = ("python", "tiger", "elephant")
# also_tuple = "monkey", "sparrow", "crane"

# print(f"{tuple} is an example of a tuple!")
# print(f"so is {also_tuple}")
# used in cases where a statement or a user-defined function can safely assume that
# the collection of values (i.e. the tuple of values used) will not change.

zoo = ("python", "tiger", "elephant")

new_zoo = ("monkey", "spider", zoo)
# ('monkey', 'spider', ('python', 'tiger', 'elephant'))
# zoo retains identity
