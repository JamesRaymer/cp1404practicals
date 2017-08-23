""" James """


def main():
    get_name()


def get_name():
    name = input("Name: ")
    make_name_odd(name)


def make_name_odd(name):
    while not name:
        name = input("Name: ")
    print(name[::2])

main()