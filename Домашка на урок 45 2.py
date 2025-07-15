class  BurgerShop:
    def __init__(self):
        self.ingredient_burger = {"Булочка":15,
                                  "Лук":10,
                                  "Помидор":20,
                                  "Сыр":30,
                                  "Котлета":50,
                                  "Соус":7,
                                  "Огурец":30,
                                  "Острый соус":50,
                                  }
        self.burger = []


    def add_ingredient(self, ingredient):
        self.burger.append(ingredient)
        print(F"Ингредиент:{ingredient}")


    def remove_ingredient(self , ingredient):
        if ingredient in self.burger:
            self.burger.remove(ingredient)
            print(f"Ингредиент {ingredient}")
        else:
            print(f"Ингредиент {ingredient} не найден")


    def show(self):
        if not self.burger:
            print("Пусто")
        else:
            for i in range(len(self.burger)):
                print(f"{self.burger[i]}:{i}")


    def summa_burger(self):
        summ = 0
        bing = self.ingredient_burger()
        for i in self.burger:
            summ+=bing[i]
        print(f"Общая стоимость: {summ} руб.")


burger = BurgerShop()
burger.add_ingredient("Булкочка")
burger.add_ingredient("Соус")
burger.add_ingredient("Котлета")
burger.add_ingredient("Сыр")
burger.add_ingredient("Лук")

burger.show()

print(burger.remove_ingredient("Лук"))
print(burger.remove_ingredient("Чеснок"))

burger.summa_burger()