import heapq
from collections import defaultdict

class RecommendationEngine:
    def __init__(self):
        # HashMaps for O(1) lookups
        self.products = {} 
        self.users = {}

    def add_product(self, product):
        self.products[product.p_id] = product

    def add_user(self, user):
        self.users[user.u_id] = user

    def calculate_score(self, user, product):
        score = 0
        
        # Base score from rating
        score += product.rating * 0.5 

        # Gather user's preferred categories based on interactions
        preferred_categories = defaultdict(int)
        
        for p_id in user.views:
            if p_id in self.products:
                preferred_categories[self.products[p_id].category] += 1
        for p_id in user.cart:
            if p_id in self.products:
                preferred_categories[self.products[p_id].category] += 3 # Cart shows higher intent
        for p_id in user.purchases:
            if p_id in self.products:
                preferred_categories[self.products[p_id].category] += 5 # Purchase shows highest intent

        # Boost score if product is in a preferred category
        if product.category in preferred_categories:
            score += preferred_categories[product.category]

        return score

    def get_top_n_recommendations(self, u_id, n=3):
        if u_id not in self.users:
            return []

        user = self.users[u_id]
        min_heap = [] # Priority Queue to keep top N

        for p_id, product in self.products.items():
            # Don't recommend already purchased products
            if p_id in user.purchases:
                continue
            
            score = self.calculate_score(user, product)
            
            # Push to heap (score, product_name)
            heapq.heappush(min_heap, (score, product.name))
            
            # Maintain only Top N in the heap
            if len(min_heap) > n:
                heapq.heappop(min_heap)
        
        # Sort in descending order before returning
        return sorted(min_heap, key=lambda x: x[0], reverse=True)