#this program prompts the user for their name and greets them
name = input("what's your name?").title()
clean = " ".join(name.split())
print(f"Hello, {clean}")
