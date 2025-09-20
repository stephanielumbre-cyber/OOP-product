class product:
    inventory = []
    product_counter = 0
    
    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully!"
    
    @classmethod
    def update_product(cls,product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if product is not None:
                    product.supplier = supplier
                return "Product Information Updated Successsfully!"
            return "Product not found."
    
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
            return "Product Deleted Successfully!"
        return "Product not found!"
    
class order:
    def __init__(self, order_id, product_id, quantity, customer_info = None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info
        
    def place_order(self):
        for product in product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    return f"Order placed successfully. Order ID:", {self.order_id}
                else:
                     return "Insufficient stock to place order"
                 
p1 = product.add_product("Laptop", "Electronics", "50", "1000", "Supplier A")
product.add_product("T-shirt", "Clothing", 100, 25, "Supplier B")
p2 = product.update_product(1, quantity=45, price=950)
p3 = product.delete_product(1)
p4 = order = order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(p1)
print(p2)
print(p3)
print(order.place_order())

    

    
    
    
