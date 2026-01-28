Дней на выполнение: 6

result: 55/100

1) **Сильные стороны**
- Использован абстрактный базовый класс `DiscountPolicy` с абстрактным методом `apply`, что соответствует требованию.
- Реализованы все три требуемых класса-наследника: `PercentDiscount`, `FixedDiscount`, `MinPriceDiscount`.
- В `PercentDiscount` и `MinPriceDiscount` корректно используется `super().__init__(name)` для инициализации имени.
- В `PercentDiscount.apply` используется `self.clamp_price(price)` для нормализации цены (хотя и не через `super()`).
- В конце программы есть блок проверки с созданием объектов и вызовом методов, включая тестирование `MinPriceDiscount`.
- Код в целом читаем, имена классов и методов соответствуют заданию.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- В классе `FixedDiscount`:
  1. Не вызван `super().__init__(name)` в `__init__`, поэтому атрибут `self.name` не будет установлен, что нарушает требование хранения имени. Это может привести к ошибкам, если код будет полагаться на наличие `name`.
  2. Метод `apply` не использует `super().clamp_price(price)` для нормализации цены, как явно требуется в условии. Вместо этого реализована своя проверка `if price < 0: price = 0`, что дублирует логику, но не использует наследование.
  3. Метод `apply` не гарантирует, что итоговая цена не будет меньше 0. Например, при `price = 100` и `amount = 150`, результат будет `-50`, что нарушает требование.
  Исправление:
  ```python
  class FixedDiscount(DiscountPolicy):
      def __init__(self, name, amount):
          super().__init__(name)  # Добавить вызов super
          self.amount = amount
      
      def apply(self, price):
          clamped_price = super().clamp_price(price)  # Использовать super
          return max(clamped_price - self.amount, 0)  # Гарантировать неотрицательность
  ```

- В классе `PriceCalculator`:
  1. Аннотация типа `policies: list[PercentDiscount]` ограничивает список только объектами `PercentDiscount`, что нарушает требование: "`PriceCalculator` работает через тип `DiscountPolicy`, а не через конкретные классы". Это делает невозможным передачу `FixedDiscount` или `MinPriceDiscount`, ломая полиморфизм и функциональность.
  Исправление:
  ```python
  class PriceCalculator:
      def __init__(self, policies: list[DiscountPolicy]):  # Исправить тип
          self.policies = policies
  ```

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В классе `PercentDiscount`: метод `apply` использует `self.clamp_price(price)` вместо `super().clamp_price(price)`. Хотя это технически работает (через наследование), условие явно требует использования `super()` в `apply` у наследников. Это может привести к проблемам, если в будущем `clamp_price` будет переопределён.
  Исправление: заменить на `clamped_price = super().clamp_price(price)`.

- В классе `MinPriceDiscount`:
  1. Метод `apply` не использует `super().clamp_price(price)` для нормализации цены, как требуется.
  2. В вычислении скидки `price * (1 - self.percent)` подразумевается, что `self.percent` — это доля (например, 0.15), но в `__init__` параметр назван `percent` (как в `PercentDiscount`), и в примере проверки передаётся 15, что, вероятно, означает проценты. Это приведёт к неверному расчёту (например, для 15% скидки результат будет `price * (1 - 15) = price * (-14)`).
  Исправление:
  ```python
  class MinPriceDiscount(DiscountPolicy):
      def __init__(self, name, min_price, percent):
          super().__init__(name)
          self.min_price = min_price
          self.percent = percent  # percent в процентах, например 15
      
      def apply(self, price):
          clamped_price = super().clamp_price(price)  # Использовать super
          if clamped_price < self.min_price:
              return clamped_price
          return clamped_price * (1 - self.percent / 100)  # Корректный расчёт процентов
  ```

- В блоке проверки (`if __name__ == "__main__"`):
  1. `PriceCalculator` инициализируется только с `percent_discount` (`calculator = PriceCalculator([percent_discount])`), но не проверяется работа с несколькими политиками (как минимум 2, как требуется). Также не передаётся `fixed_discount` и `min_price_discount`, что не позволяет проверить полную функциональность.
  2. Тестирование `MinPriceDiscount` проводится напрямую через `apply`, а не через `PriceCalculator`, что не соответствует требованию "Добавь `MinPriceDiscount` в `PriceCalculator` и проверь работу".

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- В `FixedDiscount.__init__` отсутствует вызов `super().__init__(name)`, что ухудшает читаемость и согласованность.
- В `PercentDiscount` и `MinPriceDiscount` можно добавить аннотации типов для методов (например, `apply(self, price: float) -> float`) для лучшей читаемости, хотя это не требуется явно.
- В блоке проверки можно добавить более разнообразные тесты, включая отрицательные цены и комбинации политик.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 25/50 (минус 25 за блокирующие ошибки: `FixedDiscount` не соответствует требованиям по `__init__`, `apply` и гарантии неотрицательности; `PriceCalculator` имеет неверный тип, что ломает полиморфизм; `MinPriceDiscount` имеет ошибку в расчёте процентов и не использует `super()`; проверка неполная).
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 20/30 (минус 10 за значимые недочёты: неправильное использование `super()` в `PercentDiscount` и `MinPriceDiscount`, дублирование логики в `FixedDiscount.apply`, неполная проверка).
- Стиль и тесты: 10/20 (минус 10 за минорные недочёты: отсутствие вызова `super()` в `FixedDiscount.__init__`, отсутствие аннотаций, неполные тесты в блоке проверки).
Итог: 25 + 20 + 10 = 55.

4) **Если задание выполнено не полностью**
- Отсутствует полная проверка работы `PriceCalculator` с несколькими политиками (требуется минимум 2 политики и 2 цены).
- Частично реализованы требования к использованию `super()` в методах `apply`.
- Частично реализована проверка: `MinPriceDiscount` не добавлен в `PriceCalculator`.

**Вариант полного решения (краткий код):**
```python
from abc import ABC, abstractmethod

class DiscountPolicy(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def apply(self, price: float) -> float:
        pass
    
    def clamp_price(self, price: float) -> float:
        return max(price, 0.0)

class PercentDiscount(DiscountPolicy):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent
    
    def apply(self, price: float) -> float:
        clamped_price = super().clamp_price(price)
        return clamped_price * (1 - self.percent / 100)

class FixedDiscount(DiscountPolicy):
    def __init__(self, name: str, amount: float):
        super().__init__(name)
        self.amount = amount
    
    def apply(self, price: float) -> float:
        clamped_price = super().clamp_price(price)
        return max(clamped_price - self.amount, 0.0)

class MinPriceDiscount(DiscountPolicy):
    def __init__(self, name: str, min_price: float, percent: float):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent
    
    def apply(self, price: float) -> float:
        clamped_price = super().clamp_price(price)
        if clamped_price < self.min_price:
            return clamped_price
        return clamped_price * (1 - self.percent / 100)

class PriceCalculator:
    def __init__(self, policies: list[DiscountPolicy]):
        self.policies = policies
    
    def calculate(self, price: float) -> float:
        result = price
        for policy in self.policies:
            result = policy.apply(result)
        return result

if __name__ == "__main__":
    percent = PercentDiscount("Процентная 10%", 10)
    fixed = FixedDiscount("Фиксированная 250", 250)
    min_price = MinPriceDiscount("Пороговая 1000/5%", 1000, 5)
    
    calculator = PriceCalculator([percent, fixed, min_price])
    
    test_prices = [-50, 500, 1200, 2000]
    for price in test_prices:
        final = calculator.calculate(price)
        print(f"Цена {price} -> {final:.2f}")
```
