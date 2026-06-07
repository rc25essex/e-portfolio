class Coffee:
    def __init__(self, name, price):
        self.name=name
        self.price=price
        
    def description(self):
        return self.name
    
    def cost(self):
        return self.price

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee


class MilkDecorator(CoffeeDecorator):
    def description(self):
        return self.coffee.description() + " + Milk"

    def cost(self):
        return self.coffee.cost() + 0.50


class SugarDecorator(CoffeeDecorator):
    def description(self):
        return self.coffee.description() + " + Sugar"

    def cost(self):
        return self.coffee.cost() + 0.20


class MenuComponent:
    def print_menu(self):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def print_menu(self):
        print("  - " + self.name)


class MenuCategory(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def print_menu(self):
        print(self.name)
        for item in self.items:
            item.print_menu()


# Demo
coffee_menu = MenuCategory("Local Café Menu")
coffee_menu.add(MenuItem("House Coffee"))
coffee_menu.add(MenuItem("Latte"))
coffee_menu.add(MenuItem("Cappuccino"))
coffee_menu.add(MenuItem("Tea"))

coffee_menu.print_menu()

print("\nCustomer asks for House Coffee:")
order = Coffee("House Coffee", 2.50)
order = MilkDecorator(order)
order = SugarDecorator(order)

print(order.description())
print(f"£{order.cost():.2f}")

print("\nCustomer asks for Latte with milk only:")
order = Coffee("Latte", 3.50)
order = MilkDecorator(order)

print(order.description())
print(f"£{order.cost():.2f}")
