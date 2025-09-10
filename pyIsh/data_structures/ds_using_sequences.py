# Sequence #

# tuples and strings are examples of sequences
# membership tests - allowing `in` and `not in` expressions, and indexing operations

shopping_list = ["apple", "mango", "carrot", "banana"]
name = "Monty Python"

# Indexing or `Subscription` operations
print(f"Index 0 in shopping_list is {shopping_list[0]}")
print(f"Index 1 in shopping_list is {shopping_list[1]}")
print(f"Index 0 in name is {name[0]}")
print(f"The last index of name is {name[-1]}")
print(f"The last index of shopping_list is {shopping_list[-1]}")

# Slicing on a list

print(f"Index 0 - 2 is {shopping_list[0:3]}")  # slice from index 0 to index 2
print(f"First and last index: {shopping_list[:]}")  # slice entire list


# Slicing on a string #
print("characters 1 to 3 is", name[1:3])
print("characters 2 to end is", name[2:])
print("characters 1 to -1 is", name[1:-1])
print("characters start to end is", name[:])
