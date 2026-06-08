class Product:
    def __init__(self, p_id, name, category, rating):
        self.p_id = p_id
        self.name = name
        self.category = category
        self.rating = rating

class User:
    def __init__(self, u_id, name):
        self.u_id = u_id
        self.name = name
        self.views = set()
        self.cart = set()
        self.purchases = set()

    def add_view(self, p_id):
        self.views.add(p_id)

    def add_to_cart(self, p_id):
        self.cart.add(p_id)

    def add_purchase(self, p_id):
        self.purchases.add(p_id)
        if p_id in self.cart:
            self.cart.remove(p_id) # Remove from cart once bought