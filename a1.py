class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category

def load_data(file_path):
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product = Product(int(data[0]), data[1], float(data[2]), data[3])
            products.append(product)
    return products

def insert_product(products, new_product):
    products.append(new_product)

def update_product(products, product_id, new_data):
    for product in products:
        if product.id == product_id:
            product.name = new_data['name']
            product.price = new_data['price']
            product.category = new_data['category']

def delete_product(products, product_id):
    products[:] = [product for product in products if product.id != product_id]

def search_product(products, key, value):
    result = []
    for product in products:
        if getattr(product, key) == value:
            result.append(product)
    return result

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

product_data = load_data('product_data.txt')

# Insert
new_product = Product(101, 'New Product', 49.99, 'Electronics')
insert_product(product_data, new_product)

# Update
update_data = {'name': 'Updated Product', 'price': 59.99, 'category': 'Electronics'}
update_product(product_data, 101, update_data)

# Delete
delete_product(product_data, 101)

# Search 
search_result = search_product(product_data, 'category', 'Electronics')

# Bubble Sort
bubble_sort(product_data)

# Print the sorted product data
for product in product_data:
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
