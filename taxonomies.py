from __future__ import annotations # Allows type definitions to work properly
from dataclasses import dataclass

@dataclass
class Category: # The taxonomy term
    name: str
    parent: list[Category] | None
    children: list[Category] | None
    products: list[Product] | None

    def get_products(self:Category) -> list[Product]:
        """Returns a recursively generated list of Product's

        Returns
        -------
        list[Product]
            A list of all products in the category, and all subcategories
        """
        result = []

        if self.children: # If category has a child
            for child in self.children:
                for product in child.get_products():
                    result.append(product)

        if self.products: # If category has products
            for product in self.products:
                result.append(product)
        return result

    def add_child(self:Category, category:Category):
        """Adds a Category as a child of the current category

        Parameters
        ----------
        category : Category
            The Category to set as a child of the current category
        """
        if self.children:
            self.children.append(category)
        else:
            self.children = [category]
        
        if category.parent:
            category.parent.append(self)
        else:
            category.parent = [self]

    def add_product(self:Category, product:Product):
        """Adds a product to the current Category

        Parameters
        ----------
        product : Product
            The product to add to the current category
        """
        if self.products:
            self.products.append(product)
        else:
            self.products = [product]
            
        product.category = self

@dataclass
class Product: # The nodes to add to a term
    name: str
    category: Category|None
    price: float
    description: str
    product_id: str

