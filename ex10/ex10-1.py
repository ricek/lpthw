# Combine escape sequences and format strings

import sys

world = 'world'

print('''
This is muti-line string
\t{}
\t\t{}
'''.format('Hello', world), end='')

python = "3.6.1"
print(f"from python {python}")
