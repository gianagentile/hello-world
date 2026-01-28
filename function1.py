# this program greets the user by name after cleaning up the input

def main():
    name = input("what's your name?").title()
    clean = " ".join(name.split())
    hello(clean)

def hello(to ='John Doe'):
    print("Hello," , to) 

main()
