from random import randint
NUMBERS_PER_LINE = 6

number_of_lines = int(input("How many picks? "))
for line in range(number_of_lines):
    numbers = []
    while len(numbers) != NUMBERS_PER_LINE:
        random = randint(0, 45)
        if random not in numbers:
            numbers.append(random)
            numbers.sort()
    print("{:2}".format("").join(str(number) for number in numbers))
