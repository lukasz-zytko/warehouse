def menu(arg):
    if arg == "exit":
        print("OK. See you later..")
        exit(1)
    else:
        pass

choice = input("Hello. What do you want to do?:")

if __name__ == "__main__":
    while choice != "exit":
        menu(choice)
        choice = input("What do you want to do?:")
