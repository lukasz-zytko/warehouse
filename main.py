items = [{
    "name": "Ron Barcelo", "quantity": "5", "unit": "l", "unit_price": "100"
    },{
        "name": "Cuban cigars", "quantity": "3", "unit": "pic", "unit_price": "65"
        },{
            "name": "Chocolates", "quantity": "10", "unit": "kg", "unit_price": "27"
            },{
                "name": "Red Wine", "quantity": "10", "unit": "l", "unit_price": "37"
                }]

def show():
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t--------\t----\t----------------")
    for item in items:
        print(item["name"]+"\t"+item["quantity"]+"\t\t"+item["unit"]+"\t\t"+item["unit_price"])

def add(a,b,c,d):
    items.append({"name":a, "quantity":b, "unit": c, "unit_price":d})

menu = input("Hello. What do you want to do? [exit] [show] [add]:")
if __name__ == "__main__":
    while menu != "e":
        if menu == "s":
            show()
        elif menu == "a":
            print("Add new item to your warehouse:")
            name = input("Item name: ")
            quantity = input("Item quantity: ")
            unit = input("Item unit: ")
            unit_price = input("Item unit price: ")
            add(name,quantity,unit,unit_price)
        menu = input("What do you want to do?:")
    print("Ok. See you later..")
    
