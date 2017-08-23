name = input("Your name: ")
name_file = open("name.txt", 'w')
name_file.write(name)
name_file.close()

name_read_file = open("name.txt", 'r')
name = name_read_file.read()
print("Name:", name)
name_read_file.close()

number_file = open("numbers.txt", 'r')
first_int = int(number_file.readline())
second_int = int(number_file.readline())
print(second_int + first_int)
number_file.close()

any_number_file = open("any_number.txt", 'r')
total = 0
for line in any_number_file:
    number = int(line)
    total += number
print(total)
any_number_file.close()
