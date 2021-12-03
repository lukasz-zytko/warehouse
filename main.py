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
    for item in items:
        print(item["name"]+"\t"+item["quantity"]+"\t\t"+item["unit"]+"\t\t"+item["unit_price"])

menu = input("Hello. What do you want to do?[exit][show]:")
if __name__ == "__main__":
    while menu != "e":
        if menu == "s":
            show()
        menu = input("What do you want to do?:")
    print("Ok. See you later..")
    
