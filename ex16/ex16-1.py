from sys import argv

script, filename = argv

txt = open(filename)

print(f"You opened {filename}")
print(txt.read())
