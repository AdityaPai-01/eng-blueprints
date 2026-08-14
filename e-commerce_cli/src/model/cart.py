class cart:
    def __init__(self):
        self.shopping_cart = {}

    def add_item(self, item_ID, item_quantity):
        if not item_ID in self.shopping_cart:
            self.shopping_cart.update({item_ID:item_quantity})
            return "Item added to your cart"
        else:
            self.shopping_cart[item_ID] += item_quantity
            return f"Item quantity updated to: {self.shopping_cart[item_ID]}"

    def delete_item(self, item_ID):
        if item_ID in self.shopping_cart:
            self.shopping_cart.pop(item_ID)
            return "Item deleted from your cart"
        return "Item not in your cart."

    def update_quantity(self, item_ID, new_quantity):
        if item_ID in self.shopping_cart:
            self.shopping_cart.update({item_ID, new_quantity})
            return "Item quantity updated"
        return "Item not in your cart."