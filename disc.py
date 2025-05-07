
class Deduction:
    def __init__(self, shopping_cart):
        self.shopping_cart = shopping_cart
    @property
    def shopping_cart(self):
        return self._shopping_cart
    @shopping_cart.setter
    def shopping_cart(self, shopping_cart):
        total = sum(shopping_cart.values())
        self._total = total
        if self._total >= 5000:
            self._discount = 20/100
        elif self._total < 5000:
            self._discount = 10/100
        new_total = self._total - (self._total * self._discount)
        print(new_total)

my_goods = Deduction({
    "watermelon":200,
    "apple":400,
    "kiwi":240,
    "pineapple":1969
},)
        