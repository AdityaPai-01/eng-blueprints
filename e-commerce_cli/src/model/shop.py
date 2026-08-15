class shop:
    def __init__(self, data):
        self.inventory = data

    def check_availability(self, category, item_name, quantity):
        for item in self.inventory[category]:
            if item_name in item:
                if quantity <= item['product_quantity']:
                    return f'Item: {item_name} of quantity: {quantity} is available'
                return f'Not enough {item_name} are available'
        else:
            return f'Item: {item_name} is not available'

    