def main():
    numbers = []
    print("Please enter 5 numbers.")
    for number in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average number is: {}".format(sum(numbers) / len(numbers)))

main()
