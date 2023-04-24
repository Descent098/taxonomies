# Taxonomies

A repository demonstrating taxonomies, it is meant to accompany [this article](https://schulichignite.com/blog/taxonomical-ordering/).

## Taxonomy structure

```mermaid
flowchart TD
    Z{{Categories}} & A{Computers} & B{Phones} & C{Brands} & D{Laptops} & E{Desktops} & F{Android} & G{IOS} & H{Apple} & J{Apple_laptops} & K{Apple_desktops}
    Z --> A & B & C
    A --> D & E 
    B --> F & G
    D --> J
    E --> K
    C --> H
    H --> J & K
    F --> Q((Samsung S23 Ultra))
    G --> R((Iphone 12))
    J --> S((M2 Macbook 13 inch)) & V((M2 Macbook 16 inch)) & FV((M1 Macbook 13 inch)) & FF((M1 Macbook 16 inch))
```

## Files

`taxonomies.py`; A file that defines the taxonomies

`simple_example.py`; A file you can run to test the taxonomies

`web_example.py`; A file that shows a more practical use case for taxonomies. Requires you to install jinja `pip install jinja`
