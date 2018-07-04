import sys # import user input
import math

def pythag(a, b):

    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)

    added = a_squared + b_squared

    return math.sqrt(added)

def main():

    userInput = sys.argv[1]
    # x = int(sys.argv[2])
    y = int(sys.argv[3])

    if userInput == 'add':
        print(x + y)

    if userInput == 'sub':
        print(x - y)

    if userInput == 'mult':
        print(x * y)

    if userInput == 'div':
        print(x / y)

    if userInput == 'mod':
        print(x % y)

    if userInput == 'power':
        print(x ** y)

    if userInput == 'sqrt':
        print(x ** (1/y))

    if userInput == "countto":

        for i in range(x+1):
            print(i)

    if userInput == 'hypot':

        print(pythag(x, y))

    if userInput == 'REPEAT':
        x = sys.argv[2]

        for i in range(y):
            print(x)


if __name__ == '__main__':
    main()