# -------------------------------------------------
# This is a simple Python simulation of the Point Forest app.
# Save this file as test.py and run with Python (no React/JSX).
# -------------------------------------------------

import time

class PointForest:
    def __init__(self):
        self.points = 0
        self.trees = 0
        self.history = []
        self.TREE_COST = 100

    def earn_points(self, amount):
        self.points += amount
        print(f"Earned {amount} points. Total points: {self.points}")

    def plant_tree(self):
        if self.points < self.TREE_COST:
            print(f"Not enough points. Need {self.TREE_COST - self.points} more.")
            return
        self.points -= self.TREE_COST
        self.trees += 1
        event = {
            "when": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cost": self.TREE_COST
        }
        self.history.insert(0, event)
        print(f"Planted a tree! Trees: {self.trees}, Remaining points: {self.points}")

    def show_status(self):
        print("\n--- My Status ---")
        print(f"Points: {self.points}")
        print(f"Trees planted: {self.trees}")
        if not self.history:
            print("No planting history yet.")
        else:
            print("History:")
            for h in self.history:
                print(f"  {h['when']} - planted 1 tree ({h['cost']} points)")


def main():
    app = PointForest()
    while True:
        print("\nChoose an action:")
        print("1. Earn 10 points (mission)")
        print("2. Earn 50 points (challenge)")
        print("3. Earn 100 points (sponsor)")
        print("4. Plant a tree")
        print("5. Show status")
        print("0. Exit")
        choice = input("> ").strip()

        if choice == "1":
            app.earn_points(10)
        elif choice == "2":
            app.earn_points(50)
        elif choice == "3":
            app.earn_points(100)
        elif choice == "4":
            app.plant_tree()
        elif choice == "5":
            app.show_status()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
