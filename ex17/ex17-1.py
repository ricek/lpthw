from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# the file open and close once the line runs
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
