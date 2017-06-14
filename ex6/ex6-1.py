# Write a comment above each line explaining it

# An int variable with value of 10
types_of_people = 10
# A formatted string is stored in a variable named x
x = f"There are {types_of_people} types of people."

# String variables
binary = "binary"
do_not = "don't"
# Another f-string stored in a variable named y
y = f"Those who know {binary} and those who {do_not}."

# Prints out both f-strings stored in variable x and y
print(x)
print(y)

# Prints out f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# A boolean variable named hilarious set to false
hilarious = False
# A string
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints out formatted version of the joke-evaluation string
print(joke_evaluation.format(hilarious))

# Two strings stored in variable w and e
w = "This is the left side of..."
e = "a string with a right side."

# Combine the two strings with a plus
print(w + e)
