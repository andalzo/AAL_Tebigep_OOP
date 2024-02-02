import math


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class ScientificCalculator(Calculator):
    def sin(self, value):
        return math.sin(value)

    def cos(self, value):
        return math.cos(value)

    def tan(self, value):
        return math.tan(value)


class BusinessCalculator(Calculator):
    def future_value(self, pv, r, n):
        return pv * (1 + r) ** n

    def monthly_payment(self, p, r, n):
        return p * (r * (1 + r) ** n) / (((1 + r) ** n) - 1)
