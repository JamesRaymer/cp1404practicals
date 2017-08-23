def main():
    name = input("Your name:")
    menu = "(H)ello\n(Goodbye)\n(Quit)"
    print(menu)
    choice = input()
    while choice != "Q":
        if choice == "H":
            print("Hello, " + name)
        elif choice == "G":
            print("Goodbye, " + name)
        else:
            print("Invalid choice")
        print(menu)
        choice = input()
    print("Finished")
main()
