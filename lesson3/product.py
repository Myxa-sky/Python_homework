class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_product_info(self):
        return f"Product: {self.name}, Price: {self.price}"


