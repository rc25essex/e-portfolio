from cafe_patterns import Coffee, MilkDecorator, SugarDecorator


def test_black_coffee_description_and_cost():
    coffee = Coffee("Tea", 1)

    assert coffee.description() == "Tea"
    assert coffee.cost() == 1.00


def test_decorator_adds_milk():
    coffee = MilkDecorator(Coffee("House Coffee", 2))

    assert coffee.description() == "House Coffee + Milk"
    assert coffee.cost() == 2.50


def test_multiple_decorators_add_milk_and_sugar():
    coffee = SugarDecorator(MilkDecorator(Coffee("House Coffee", 3)))

    assert coffee.description() == "House Coffee + Milk + Sugar"
    assert coffee.cost() == 3.70
