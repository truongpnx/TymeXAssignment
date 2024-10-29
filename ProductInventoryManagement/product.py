class Product:
    def __init__(self, name: str, price: float, quantity: int):

        if name == "":
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def __str__(self) -> str:
        return "{}: price: {}, quantity: {}".format(self.name, self.price, self.quantity)