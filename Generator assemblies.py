
# Задача 1: Фабрика Функций
def create_operation(operation):
    if operation == "multiply":
        return lambda x, y: x * y
    elif operation == "divide":
        return lambda x, y: x / y if y != 0 else "Error: Division by zero"

operation_multiply = create_operation("multiply")
operation_divide = create_operation("divide")

print(operation_multiply(2, 3))
print(operation_divide(6, 3))
print(operation_divide(10, 0))


# Задача 2: Лямбда-Функции
square_lambda = lambda x: x**2

def square_def(x):
    return x**2

print(square_lambda(4))
print(square_def(4))


# Задача 3: Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call(self):
        return self.a * self.b

rect = Rect(2, 4)
print("Стороны:", rect.a, ",", rect.b)
print("Площадь:", rect.call())

