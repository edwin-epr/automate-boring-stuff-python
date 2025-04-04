import pyinputplus as pyip

def writeConsole(data: object) -> None:
    print(f'Output: {data}')

def main() -> None:
    # First steps
    # response = pyip.inputNum()
    # writeConsole(response)

    # response = pyip.inputInt(prompt='Enter a number: ')
    # writeConsole(response)

    # help(pyip.inputChoice) to displays help information
    # The min, max, greaterThan, and lessThan keyword arguments

    # response = pyip.inputNum('Enter num: ', min=4)
    # writeConsole(response)

    # response = pyip.inputNum('Enter num: ', greaterThan=4)
    # writeConsole(response)

    # response = pyip.inputNum('>> ', min=4, lessThan=6)
    # writeConsole(response)

    # The blank keyword argument
    # response = pyip.inputNum('Enter a num: ')
    # writeConsole(response)

    response = pyip.inputNum('Enter a num: ', blank=True)
    writeConsole(response)

if __name__ == '__main__':
    main()
