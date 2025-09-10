# Control Flow #

# if ... else #

# number = 23

# guess = int(input("Enter an integer: "))

# if guess == number:
#   print("# inside the first if block #")
#   print("Congratulations you guessed it!")
#   print("But no cigar!")
# elif guess < number:
#   print("# inside the second block - else if")
#   print("No, a little higher than that...")
# else:
#   print("# inside the final block ... #")
#   print("A little lower styl...")
# print("All done!")


# while #

# running = True
# name = "Bob"

# while running:
#   guess = str(input("Enter a name : "))

#   if guess == "Bob":
#     print("You guessed it - well done!")
#     print("What's your name?")
#     running = False
#   elif guess == "Mark":
#     print("Better luck next time...")
#     print("Care to try again?")
#   else:
#     print("Don't worry about it!")
# else:
#   print("The loop is over")
# print("The program has completed.")

# for loop #

# for i in range(0, 12, 2): # range(start, stop, step) | inclusive of start value, exclusive of stop value, step = value to increment by
#   print(i)
# else:
#   print("The for loop is over...")

# break keyword #

# while True:
#   s = input(str("Enter a string to receive it's input length : "))
#   if s == "quit":
#     print("Exiting loop with break keyword...")
#     break
#   print(f'The length of the string is {len(s)}')
# print("Program has completed")

# continue keyword #

# while True:
#   s = str(input("Enter something... : "))

#   if s == "quit":
#     break
#   if len(s) < 3:
#     print("Input is too small. Try again.")
#     continue
#   elif len(s) > 10:
#     print("Input is too large. Try again")
#     continue
#   else:
#     print("Input is just right")
#     break

# print("Program complete.")
