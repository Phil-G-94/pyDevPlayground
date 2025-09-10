# Strings #

# '''
# String interpolation using format()
# {n}
# where n = the position of the variable
# in the args passed into format()
# '''

# name = "Billybob"

# print('{0} was here'.format(name))
# # Billybob was here

# '''
# You can also ommit the variable index
# '''

# print('Why is {} messing with that python?'.format(name))

# '''
# or use f-strings to interpolate strings with named params
# '''

# print(f'Go back to JavaScript {name}!')

# print('{0:.3f}'.format(1.0/3))

# '''
# format() returns a formatted version of the string preceding it, using substitutions from args and kwargs.
# The substitutions are identified by braces ('{' and '}').
# '''

# '''
# print() always ends with an invisible \n character so that
# each print, prints on a new line
# we can alter this behaviour to have it end with " " instead
# '''

# print('a', end=' ')
# print('b', end=' ')
# print('c')
# # a b c

# print('a', end='0')
# print('b', end='0')
# #a0b0

# '''
# Escape sequences

# \

# \t

# \n
# '''

# str = '''
# This is a multi-line string.
# Wonder how it will print?What do you think?


# Hmmmm...I don't rightly know!
# '''

# strA = 'this is also  string.\thow will IT print?'

# strB = "First sentence." \
# " Second sentence."

# print(str) # multi-line formatting respects whitespace and allows you to use single or double quotes freely
# '''
# This is a multi-line string.
# Wonder how it will print? What do you think?
#
#
# Hmmmm...I don't rightly know!
# '''

# print(strA) # \t prints a tab before the second part of the sentence - this is also a multi-line string.       how will IT print?

# print(strB) # \ indicates no newline is added - First sentence. Second sentence.

# Raw String - r | R preceding string means no special processing should be handled
# Basically, won't respect escape sequences - will just print all chars as a ... raw string.

print(R"Newlines are indicated by \n")  # Newlines are indicated by \n
