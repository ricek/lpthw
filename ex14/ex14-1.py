from sys import argv

script, name, like = argv
prompt = '-> '

print(f"Hi {name}, I'm the {script} script.")
print(f"I see that you like {like}")
print(f"Why do you like it?")
reason = input(prompt)

print(f"""
Let me get it together {name} :)
So you like {like} because {reason}
""")
