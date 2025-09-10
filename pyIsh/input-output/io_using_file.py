text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

# open file for writing
file = open("lorem.txt", "w")

# write to file
file.write(text)

# close the file
file.close()

# second arg = mode
# if no mode is specified,
# read mode is assumed by default
file = open("lorem.txt")

while True:

    line = file.readline()

    # Zero length indicates end of file
    if len(line) == 0:
        break

    print(line, end="")

# close the file
file.close()
