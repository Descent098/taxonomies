from taxonomies import *


# Setup taxonomies
## Setup top level terms
computers = Category("Computers",None, None, None)
phones = Category("phones",None, None, None)
brands = Category("Brands",None, None, None)

## Setup second level terms
### Setup second level computer terms
laptops = Category("Laptops", None , None, None)
desktops = Category("Desktops", None , None, None)

computers.add_child(laptops)
computers.add_child(desktops)

### Setup second level phone terms
android = Category("Android", None , None, None)
ios = Category("IOS", None , None, None)

phones.add_child(android)
phones.add_child(ios)

### Setup second level brand terms
apple = Category("Apple",None , None, None)
brands.add_child(apple)

apple_laptops = Category("Apple Laptops", None , None, None)
apple_desktops = Category("Apple Desktops", None , None, None)

laptops.add_child(apple_laptops)
desktops.add_child(apple_desktops)
apple.add_child(apple_laptops)
apple.add_child(apple_desktops)

## Add products
ios.add_product(Product("Iphone 12", None, 999.99, "It's a phone", "SDKA-5827-JFLS-6359"))
android.add_product(Product("Samsung S23 Ultra", None, 1299.99, "It's a phone", "SDKA-5827-JFLS-3321"))
apple_laptops.add_product(Product("M2 Macbook 13 inch", None, 1599.99, "It's a laptop", "SDKA-5827-JFLS-6356"))
apple_laptops.add_product(Product("M2 Macbook 16 inch", None, 2399.99, "It's a laptop", "SDKA-5827-JFLS-4516"))
apple_laptops.add_product(Product("M1 Macbook 13 inch", None, 1099.99, "It's a laptop", "SDKA-5827-JFLS-6358"))
apple_laptops.add_product(Product("M1 Macbook 16 inch", None, 1399.99, "It's a laptop", "SDKA-5827-JFLS-7365"))

if __name__ == "__main__": # Only run the below code if this file is being run
    print("All computer products:")
    print(*[
        f"\n\t{product.name}" 
        for product in computers.get_products()
    ])