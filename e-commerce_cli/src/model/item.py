class Item:
    def __init__(self, id, name, quantity, price):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price

    def todict(self):
        return {"Product_ID": self.id,
                "Product_Name": self.name,
                "Product_Quantity": self.quantity,
                "Product_Price": self.price}

    