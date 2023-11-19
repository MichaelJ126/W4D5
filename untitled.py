# W4 Friday Project - OOP Calculation of Rental Income

class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Property:
    def __init__(self, name, purchase_price, expenses=None, incomes=None):
        self.name = name
        self.purchase_price = purchase_price
        self.expenses = expenses or []
        self.incomes = incomes or []

    def calculate_roi(self):
        total_income = sum(income.amount for income in self.incomes)
        total_expense = sum(expense.amount for expense in self.expenses)
        net_income = total_income - total_expense
        roi = (net_income / self.purchase_price) * 100
        return roi


class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)


def main():
    users = []

    while True:
        print("\n1. Create User\n2. Add Property\n3. Calculate ROI\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            user_name = input("Enter user name: ")
            user = User(user_name)
            users.append(user)
            print(f"User {user_name} created!")

        elif choice == '2':
            if not users:
                print("Please create a user first.")
                continue

            user_name = input("Enter user name: ")
            user = next((u for u in users if u.name == user_name), None)

            if user:
                property_name = input("Enter property name: ")
                purchase_price = float(input("Enter property purchase price: "))
                property = Property(property_name, purchase_price)
                user.add_property(property)
                print(f"Property {property_name} added to user {user_name}!")

            else:
                print(f"User {user_name} not found!")

        elif choice == '3':
            if not users:
                print("Please create a user first.")
                continue

            user_name = input("Enter user name: ")
            user = next((u for u in users if u.name == user_name), None)

            if user:
                property_name = input("Enter property name: ")
                property = next((p for p in user.properties if p.name == property_name), None)

                if property:
                    print(f"ROI for {property_name}: {property.calculate_roi()}%")
                else:
                    print(f"Property {property_name} not found!")

            else:
                print(f"User {user_name} not found!")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
