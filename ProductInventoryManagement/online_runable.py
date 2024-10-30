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

from enum import Enum
from decimal import Decimal

class ProductSortType(Enum):
    QUANTITY = "quantity"
    PRICE = "price"


class ProductInventory:
    def __init__(self, products: list[Product]):
        self.products = products
    
    def __str__(self) -> str:
        res = "Product List: \n\n"
        for product in self.products:
            res += str(product) + '\n'
        return res


    def totalInventoryValue(self) -> float:
        result = Decimal(0.0)
        for product in self.products:
            result += Decimal(product.price) * Decimal(product.quantity)
        
        return result
        
    def findMostExpensive(self) -> str | None:
        maxPrice = -1
        result = None

        for product in self.products:
            if product.price > maxPrice:
                maxPrice = product.price
                result = product.name
        
        return result

    def hasProduct(self, name: str) -> bool:
        for product in self.products:
            if product.name == name:
                return True
        
        return False

    def sortBy(self, sortBy: list[ProductSortType] = None, descending: bool = False):
        if sortBy is None:
            return

        def sortKey(product: Product):
            keys = []
            for sortType in sortBy:
                match (sortType):
                    case ProductSortType.PRICE:
                        keys.append(product.price)
                    case ProductSortType.QUANTITY:
                        keys.append(product.quantity)

            return tuple(keys)
        
        self.products.sort(key=sortKey, reverse=descending)

def main():
    products = [
        Product("Laptop", 999.99, 5),
        Product("Smartphone", 499.99, 10),
        Product("Tablet", 299.99, 0),
        Product("Smartwatch", 199.99, 3),
    ]

    inventory = ProductInventory(products=products)

    print("Actions: ")
    print("1. Show inventory")
    print("2. Total inventory value")
    print("3. Find most expensive product")
    print("4. Check product is in inventory")
    print("5. Sort")
    print("6. Exit")

    while True:
        try:
            action = int(input("Perform action: "))
            match action:
                case 1:
                    print(str(inventory))
                case 2:
                    print("Total iventory value: {:.2f}".format(inventory.totalInventoryValue()))
                case 3:
                    print("Most expensive product: {}".format(inventory.findMostExpensive()))
                case 4:
                    product_name = str(input("Type the product name: "))
                    print("{} is in inventory: {}".format(product_name, inventory.hasProduct(product_name)))
                case 5:
                    sortBy = None
                    for sortType in ProductSortType:
                        agree = str(input("Sort by {} (y/N): ".format(sortType.name)))
                        if agree == 'y' or agree == 'Y':
                            if sortBy is None:
                                sortBy = []
                            
                            sortBy.append(sortType)

                    agree = str(input("Descending sort? (y/N): "))
                    descending = False
                    if agree == 'y' or agree == 'Y':
                        descending = True


                    inventory.sortBy(sortBy=sortBy, descending=descending)
                    print(str(inventory))
                case 6:
                    break


        except RuntimeError:
            print("You mistyped, please try again")


main()
