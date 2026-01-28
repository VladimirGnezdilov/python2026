from abc import ABC, abstractmethod
class DiscountPolicy(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def apply(self, price):
        pass
    def clamp_price(self, price):
        return max(price, 0)
class PercentDiscount(DiscountPolicy):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent
    def apply(self, price):
        clamped_price = self.clamp_price(price)
        return clamped_price * (1 - self.percent / 100)
class FixedDiscount(DiscountPolicy):
    def __init__(self, name, amount):
        self.amount = amount
    
    def apply(self, price):
        if price < 0:
            price = 0
        return price - self.amount
class PriceCalculator:
    def __init__(self, policies: list[PercentDiscount]):
        self.policies = policies
    def calculate(self, price: float) -> float:
        result = price
        for policy in self.policies:
            result = policy.apply(result)
        return result
class MinPriceDiscount(DiscountPolicy):
    def __init__(self, name, min_price, percent):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent
    
    def apply(self, price):
        if price < self.min_price:
            return price
        return price * (1 - self.percent)
if __name__ == "__main__":
    percent_discount = PercentDiscount("Процентная скидка", 7)  
    fixed_discount = FixedDiscount("Фиксированная скидка", 500)
    min_price_discount = MinPriceDiscount("Пороговая скидка", 1000, 15)
    calculator = PriceCalculator([percent_discount])
    prices = [-100, 1500]
    for price in prices:
        final_price = calculator.calculate(price)
        print(f"Исходная цена: {price}, итоговая: {final_price}")
    test_prices = [800, 1200]
    for price in test_prices:
        result = min_price_discount.apply(price)
        print(f"MinPriceDiscount: {price} -> {result}")
