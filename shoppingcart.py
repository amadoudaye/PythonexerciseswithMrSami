class ShoppingCart:
    def __init__(self):
        self.items = {}  # store items as: {"Apple": 1.50, "Milk": 3.20}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Added {name} for ${price}")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed {name}")
        else:
            print(f"{name} not found in the cart.")

    def calculate_total(self):
        total = sum(self.items.values())
        return round(total, 2)

cart = ShoppingCart()
cart.add_item("Apple", 1.50)
cart.add_item("Milk", 3.20)

print("Total =", cart.calculate_total())