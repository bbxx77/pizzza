from base import PizzaBase
from toppings import CheeseDecorator, TomatoDecorator

if __name__ == "__main__":
    pizza = PizzaBase() 
    toppings = []

    while True:
        print("ТОппинг таңдаңыз: (1) Ірімшік, (2) Қызанақ, (3) Аяқтау")
        choice = input("Енгізіңіз: ")

        if choice == "1":
            toppings.append(CheeseDecorator)
        elif choice == "2":
            toppings.append(TomatoDecorator)
        elif choice == "3":
            break
        else:
            print("error")
    for topping in toppings:
        pizza = topping(pizza)
    print("Сипаттамасы: " + pizza.get_description())
    print("Бағасы: " + str(pizza.get_cost()))
