# 1. 클래스: MenuItem (모든 메뉴의 기본 부모 클래스)
# ======================================================================
# [초기화] (이름, 가격, 조리시간):
#     self.이름 = 이름
#     self.가격 = 가격
#     self.조리시간 = 조리시간 (초 단위)

# ======================================================================
# 2. 클래스: Burger (MenuItem 상속)
# ======================================================================
# [초기화] (이름, 가격, 패티종류, 패티개수, 패티_1개당_조리시간, 빵종류="일반참깨빵"):
#     계산: 총_조리시간 = (패티_1개당_조리시간 * 패티개수) + 60초 (기본 조립시간)
   
#     부모[MenuItem] 초기화 호출(이름, 가격, 총_조리시간)
   
#     self.패티종류 = 패티종류
#     self.패티개수 = 패티개수
#     self.빵종류 = 빵종류
#     self.공통재료 = ["양파", "양상추", "토마토", "피클"]
#     self.품절여부 = 거짓 (False)

# ======================================================================
# 3. 클래스: SpecialBurger (Burger 상속)
# ======================================================================
# [초기화] (이름, 가격, 패티종류, 패티개수, 패티_1개당_조리시간, 특수소스):
#     부모[Burger] 초기화 호출(이름, 가격, 패티종류, 패티개수, 패티_1개당_조리시간, 빵종류="브리오슈번")
#     self.특수소스 = 특수소스

# ======================================================================
# 4. 클래스: Side (MenuItem 상속)
# ======================================================================
# [초기화] (이름, 가격, 조리시간):
#     부모[MenuItem] 초기화 호출(이름, 가격, 조리시간)

# ======================================================================
# 5. 클래스: Drink (MenuItem 상속)
# ======================================================================
# [초기화] (이름, 가격):
#     부모[MenuItem] 초기화 호출(이름, 가격, 조리시간=30초)

# ======================================================================
# 6. 클래스: SetMenu (버거, 사이드, 음료의 조합)
# ======================================================================
# [초기화] (버거_객체, 사이드_객체, 음료_객체):
#     self.버거 = 버거_객체
#     self.사이드 = 사이드_객체
#     self.음료 = 음료_객체
#     self.이름 = 버거_객체.이름 + " 세트"
   
#     계산: 원가 = 버거_객체.가격 + 사이드_객체.가격 + 음료_객체.가격
#     self.가격 = 정수형변환(원가 * 0.8)  # 20% 할인 적용
   
#     계산: self.조리시간 = 최대값(버거_객체.조리시간, 사이드_객체.조리시간, 음료_객체.조리시간)
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
        super().__init__(name, price, patty_species, patty_amount, patty_time, bread="크림빵")
        self.special = special

class Side(MenuItem):
    def __init__(self, name, price, making_time):
        super().__init__(name, price, making_time)

class Drink(MenuItem):
    def __init__(self, name, price, making_time=30):
        super().__init__(name, price, making_time=30)

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
sid1 = Side("치킨너겟", 15000, 300)
dri1 = Drink("밀크셰이크", 3000, 130)
set1 = SetMenu(bur1, sid1, dri1)
print(set1.name)