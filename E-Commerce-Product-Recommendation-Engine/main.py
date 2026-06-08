from src.models import Product, User
from src.engine import RecommendationEngine

def main():
    print("🚀 Initializing E-Commerce Recommendation Engine...")
    engine = RecommendationEngine()

    # 1. Product Dataset Creation
    engine.add_product(Product("P1", "Wireless Mouse", "Electronics", 4.5))
    engine.add_product(Product("P2", "Mechanical Keyboard", "Electronics", 4.8))
    engine.add_product(Product("P3", "Theory of Machines Textbook", "Education", 4.2))
    engine.add_product(Product("P4", "Vegan Protein Bars", "Groceries", 4.7))
    engine.add_product(Product("P5", "Noise Cancelling Headphones", "Electronics", 4.9))
    engine.add_product(Product("P6", "Oat Milk 1L", "Groceries", 4.3))
    engine.add_product(Product("P7", "LED Desk Lamp", "Home", 4.0))

    # 2. User Creation
    user1 = User("U1", "Prisha")
    user2 = User("U2", "Priscilla")
    engine.add_user(user1)
    engine.add_user(user2)

    # 3. User Interaction Simulation
    print("\n[Simulating User Activity...]")
    # Prisha looks at electronics and buys a keyboard, views textbook
    user1.add_view("P1")
    user1.add_view("P3")
    user1.add_to_cart("P5")
    user1.add_purchase("P2")

    # Priscilla looks at groceries and buys oat milk
    user2.add_view("P4")
    user2.add_purchase("P6")

    # 4. Generate Recommendations
    print(f"\n--- Recommendations for {user1.name} (Bought: Mechanical Keyboard) ---")
    recs_prisha = engine.get_top_n_recommendations(user1.u_id, n=3)
    for i, (score, name) in enumerate(recs_prisha):
        print(f"{i+1}. {name} (Relevance Score: {score:.2f})")

    print(f"\n--- Recommendations for {user2.name} (Bought: Oat Milk) ---")
    recs_priscilla = engine.get_top_n_recommendations(user2.u_id, n=3)
    for i, (score, name) in enumerate(recs_priscilla):
        print(f"{i+1}. {name} (Relevance Score: {score:.2f})")

    # Output to report
    with open("outputs/recommendation_report.txt", "w") as f:
        f.write(f"Report for {user1.name}: {recs_prisha}\n")
        f.write(f"Report for {user2.name}: {recs_priscilla}\n")
    print("\n✅ Report saved to outputs/recommendation_report.txt")

if __name__ == "__main__":
    main()