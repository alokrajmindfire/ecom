class Product:
    def __init__(self, id, name, category, price, stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def calculate_price(self):
        return self.price * self.stock
    def calculate_total(self):
        return self.calculate_price()

class Electronics(Product):
    def calculate_total(self):
        base = self.calculate_price()
        tax = 0.15 * base
        return base + tax


class Clothing(Product):
    def calculate_total(self):
        base = self.calculate_price()
        discount = 0.10 * base
        return base - discount
    
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email