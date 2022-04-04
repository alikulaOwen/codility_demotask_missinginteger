# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from missing_int import solution


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')
    print("Please enter a list of integer:\ngiven an array A of N integers, returns the smallest positive integer (greater than 0)\nthat does not occur in A.For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5")


if __name__ == '__main__':
    name = input("Enter name: ")
    print_hi(name)
    A = list(map(int, input().split(" ")))
    print(solution(A))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
