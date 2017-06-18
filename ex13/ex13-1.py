from sys import argv
# read the WYSS section for how to run this
script, first, last = argv

# Prints out first and last name from CL arguments
print("Hello", first, last)
# Ask the user for nickname
nickname = input("What is your nickname? ")

# Pritns out their name and nickname
print(f"{first} {last}'s nickname is {nickname}")
