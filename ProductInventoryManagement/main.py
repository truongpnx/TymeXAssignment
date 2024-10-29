from product import Product
from product_inventory import *

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


if __name__ == "__main__":
    main()