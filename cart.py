class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def total(self):
        return sum(item["price"] for item in self.items)

    def apply_discount(self, percent):
        discount = self.total() * (percent / 100)
        return self.total() - discount

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False