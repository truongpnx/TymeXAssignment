from product import Product
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


