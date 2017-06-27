# Prompt the user to enter the filename
file = input("Type the filename to open: ")
# Open the file from user input
txt = open(file)
# Read the file and print it out
print(txt.read())
# Close the file when done
txt.close()
