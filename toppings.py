from pizza import Pizza

class CheeseDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description() + ", ірімшік"

    def get_cost(self):
        return self._pizza.get_cost() + 2.0

class TomatoDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description() + ", қызанақ"

    def get_cost(self):
        return self._pizza.get_cost() + 1.5
