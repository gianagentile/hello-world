# this program ask the user for a number an then prints the square of that number

def main():
    number = float(input("Enter a number to be squared: "))
    squared = square(number)
    print(f"The square of {number} is {squared}.")


def square(n):
    return n * n
main()