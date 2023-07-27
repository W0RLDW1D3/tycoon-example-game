import random

class Business:
    def __init__(self, name, base_income):
        self.name = name
        self.base_income = base_income
        self.level = 1
        self.income = base_income * self.level

    def upgrade(self):
        self.level += 1
        self.income = self.base_income * self.level

    def collect_income(self):
        return self.income

class TycoonGame:
    def __init__(self):
        self.businesses = []
        self.money = 0

    def add_business(self, business):
        self.businesses.append(business)

    def upgrade_business(self, index):
        if index < len(self.businesses):
            business = self.businesses[index]
            cost = business.base_income * business.level
            if self.money >= cost:
                business.upgrade()
                self.money -= cost
                print(f"{business.name} upgraded to level {business.level}")
            else:
                print("Not enough money to upgrade")

    def collect_income(self):
        total_income = 0
        for business in self.businesses:
            total_income += business.collect_income()
        self.money += total_income
        print(f"Collected income: ${total_income}")

    def play(self):
        while True:
            print("1. Add business")
            print("2. Upgrade business")
            print("3. Collect income")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter business name: ")
                base_income = int(input("Enter base income: "))
                business = Business(name, base_income)
                self.add_business(business)
                print(f"Added {name} with base income ${base_income}")
            elif choice == "2":
                index = int(input("Enter business index: "))
                self.upgrade_business(index)
            elif choice == "3":
                self.collect_income()
            elif choice == "4":
                print(f"Game Over! Total money earned: ${self.money}")
                break
            else:
                print("Invalid choice. Please try again.")

# Creating and running the game
game = TycoonGame()
game.play()
