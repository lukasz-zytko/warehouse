items = ["Ron Barcelo", "Cuban cigars", "Chocolate sweets", "Red wine"]

def show():
    print(items)

menu = input("Hello. What do you want to do? [exit]:")
if __name__ == "__main__":
    while menu != "exit":
        if menu == "show":
            show()
        menu = input("What do you want to do?:")
    print("Ok. See you later..")
    
