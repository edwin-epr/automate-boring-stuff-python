#!/usr/bin/env python
import pyinputplus as pyip

def writeConsole(data: object) -> None:
    print(f'Output: {data}')

# First steps
def fun1() -> None:
    response = pyip.inputNum()
    writeConsole(response)

def fun2() -> None:
    response = pyip.inputInt(prompt='Enter a number: ')
    writeConsole(response)

# help(pyip.inputChoice) to displays help information
# The min, max, greaterThan, and lessThan keyword arguments
def fun3() -> None:
    response = pyip.inputNum('Enter num: ', min=4)
    writeConsole(response)

def fun4() -> None:
    response = pyip.inputNum('Enter num: ', greaterThan=4)
    writeConsole(response)

def fun5() -> None:
    response = pyip.inputNum('>> ', min=4, lessThan=6)
    writeConsole(response)

# The blank keyword argument
def fun6() -> None:
    response = pyip.inputNum('Enter a num: ')
    writeConsole(response)

def fun7() -> None:
    response = pyip.inputNum('Enter a num: ', blank=True)
    writeConsole(response)

# The limit, timeout and default keyword arguments
def fun8() -> None:
    response = pyip.inputNum(prompt='Enter a number: ', limit=2)
    writeConsole(response)

def fun9() -> None:
    response = pyip.inputNum(prompt='Enter a number: ', timeout=10)
    writeConsole(response)

def fun10() -> None:
    response = pyip.inputNum(prompt='Enter a number: ', limit=2, default='N/A')
    writeConsole(response)

if __name__ == '__main__':
    fun10()
