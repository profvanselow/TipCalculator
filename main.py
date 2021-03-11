# This is a sample Python script.
# I am an awesome programmer. Let's get started.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

#from POGIL12 import do_pogil_12
import POGIL12


def main():

    printMessage()
    print("Change")

def printMessage(): # top line of function definition is called a header (
    # (parameter)
    print("Hello " + name + "!")
    print("Welcome to Python.")
    print("Learn the power of functions!")


def calc_meal_price():
    num_hamburgers = 5
    print('Number of hamburgers set to 5')
    #num_hamburgers = int(input("Enter the number of hamburgers: "))
    num_fries = int(input("Enter the number of fries: "))
    num_drinks = int(input("Enter the number of drinks: "))
    total = num_hamburgers * 2 + num_fries * 1.5 + num_drinks
    print("Total cost: $", format(total, '.2f'), sep='')

def do_pogil_11():
    first_name = input("Enter your name: ")

    print("Name:", first_name)

    # random is a library
    # randint is a function
    # inside of parentheses is arguments
    # https://docs.python.org/3/library/random.html
    print(random.randint(1, 100))

    # Rob McNiven helped with this.
    print(abs(4.5))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

