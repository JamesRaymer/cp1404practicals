def main():
    print("Input 2 numbers.")
    x = int(input("First Number:"))
    y = int(input("Second Number:"))
    if x % 2 == 0:
        for i in range(x, y + 1, 2):
            print(i, end=' ')
    else:
        for i in range(x + 1, y + 1, 2):
            print(i, end=' ')
    print()
    if x % 2 == 1:
        for i in range(x, y + 1, 2):
            print(i, end=' ')
    else:
        for i in range(x + 1, y + 1, 2):
            print(i, end=' ')
    print()
    for i in range(x, y):
        print(i**i, end=' ')
main()
