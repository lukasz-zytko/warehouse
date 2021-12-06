items = [{
    "name": "Ron Barcelo", "quantity": "5", "unit": "l", "unit_price": "100"
    },{
        "name": "Cuban cigars", "quantity": "3", "unit": "pic", "unit_price": "65"
        },{
            "name": "Chocolates", "quantity": "10", "unit": "kg", "unit_price": "27"
            },{
                "name": "Red Wine", "quantity": "10", "unit": "l", "unit_price": "37"
                }]

sold_items = []

def show():
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t--------\t----\t----------------")
    for item in items:
        print(item["name"]+"\t"+item["quantity"]+"\t\t"+item["unit"]+"\t\t"+item["unit_price"])

def add(a,b,c,d):
    items.append({"name":a, "quantity":b, "unit": c, "unit_price":d})

def sell_item(a,b):
    for item in items:
        if item["name"] == a:
            item["quantity"] = str(int(item["quantity"])-int(b))
            sold_items.append({"name": item["name"], "quantity": b, "unit": item["unit"], "unit_price": item["unit_price"]})
            print(sold_items)

def get_cost():
    total_cost = sum([int(item["quantity"]) * int(item["unit_price"]) for item in items])
    return total_cost

def get_income():
    total_income = sum([int(item["quantity"]) * int(item["unit_price"]) for item in sold_items])
    return total_income

def show_revenue():
    print("Revenue breakdown (PLN):")
    print("Income:\t\t"+str(get_income()))
    print("Cost:\t\t"+str(get_cost()))
    print("------------------------")
    print("Revenue:\t"+str(get_income() - get_cost()))

menu = input("Hello. What do you want to do? [exit] [show] [add] [sell] [show_revenue]:")
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
        elif menu == "sell":
            print("What do you want to sell")
            name = input("Item name: ")
            quantity = input("Item quantity: ")
            sell_item(name,quantity)
        elif menu == "r":
            show_revenue()
        menu = input("What do you want to do?:")
    print("Ok. See you later..")
    
