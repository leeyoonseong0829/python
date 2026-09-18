class MenuItem:
    def __init__(self, name, price, making_time):
        self.name = name
        self.price = price
        self.making_time = making_time
class Burger(MenuItem):
    def __init__(self, name, price, patty_species, patty_amount, patty_time, bread="참깨빵"):
        total = (patty_time * patty_amount) + 60
        super().__init__(name, price, total)
        self.patty_species = patty_species
        self.patty_amount = patty_amount
        self.bread = bread
        self.common = ["치즈", "피클", "양파"]
        self.sold_out = False
class SpecialBurger(Burger):
    def __init__(self, name, price, patty_species, patty_amount, patty_time, special):
        super().__init__(self, name, price, patty_species, patty_amount, patty_time, bread="크림빵")
        self.special = special
class Side(MenuItem):
    def __init__(self, name, price, making_time):
        super().__init__(self, name, price, making_time)
class Drink(MenuItem):
    def __init__(self, name, price):
        super().__init__(self, name, price, making_time=30)
class SetMenu:
    def __init__(self, burger, side, drink):
        self.burger = burger
        self.side = side
        self.drink = drink
        self.name = burger.name + " 세트"
        original = burger.price + side.price + drink.price
        self.price = int(original * 0.8)
        self.making_time = max(burger.making_time, side.making_time, drink.making_time)
bur1 = Burger("치킨버거", 6000, "양상추패티", 3, 120, "단팥빵")
sid1 = Side("코울슬로", 1500, 100)
dri1 = Drink("밀크셰이크", 3000, 130)
set1 = SetMenu(bur1, sid1, dri1)
print(set1.name)