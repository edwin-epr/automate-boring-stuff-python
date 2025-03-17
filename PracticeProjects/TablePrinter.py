#!/usr/bin/env python3

def columWidth(tableData: list[list[str]], rowNumber: int) -> list[int]:

    columWidth: list[int] = [0] * rowNumber

    for index, item in enumerate(tableData):
        maxWidth: int = len(max(item, key=len))
        columWidth[index] = maxWidth
        # print(f'${index} ${item} ${len(max(item, key=len))}')

    return columWidth

def printTable(tableData: list[list[str]]) -> None:

    rowNumber: int = len(tableData)
    colNumber: int = len(tableData[0])
    colWidth: list[int] = columWidth(tableData, rowNumber)

    for col in range(colNumber):
        for row in range(rowNumber):
            print(tableData[row][col].rjust(colWidth[row]), end=' ')
        print()

if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
