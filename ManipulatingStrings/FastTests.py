from typing import Dict

def printPicnin(items: Dict[str, int], leftWidth: int, rightWidth: int) -> None:
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in items.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

if __name__ == "__main__":
    picnicBasket: Dict[str, int] = {'sandwich': 4, 'apples': 12, 'cookies': 8000}
    printPicnin(picnicBasket, 12, 5)
    printPicnin(picnicBasket, 20, 6)
