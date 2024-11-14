#Вариант 1

'''
from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов

# Определяем интерфейс стратегии
class Strategy(ABC):  # Класс Strategy наследует от ABC (абстрактного базового класса)
    @abstractmethod  # Декоратор для обозначения абстрактного метода
    def execute(self, a, b):  # Определяем абстрактный метод execute, который принимает два аргумента
        pass  # Метод не имеет реализации

# Конкретная стратегия для сложения
class ConcreteStrategyAdd(Strategy):  # Класс ConcreteStrategyAdd наследует от Strategy
    def execute(self, a, b):  # Реализация метода execute для сложения
        return a + b  # Возвращаем сумму a и b

# Конкретная стратегия для вычитания
class ConcreteStrategySubtract(Strategy):  # Класс ConcreteStrategySubtract наследует от Strategy
    def execute(self, a, b):  # Реализация метода execute для вычитания
        return a - b  # Возвращаем разность a и b

# Контекст, который использует стратегию
class Context:
    def __init__(self, strategy: Strategy):  # Метод инициализации класса Context
        self.strategy = strategy  # Устанавливаем стратегию при создании контекста

    def set_strategy(self, strategy: Strategy):  # Метод для изменения стратегии
        self.strategy = strategy  # Меняем стратегию на новую

    def execute_strategy(self, a, b):  # Метод для выполнения текущей стратегии
        return self.strategy.execute(a, b)  # Выполняем метод execute выбранной стратегии

# Пример использования
context = Context(ConcreteStrategyAdd())  # Создаем контекст с конкретной стратегией сложения
print(context.execute_strategy(5, 3))  # Вывод: 8 (результат сложения)

context.set_strategy(ConcreteStrategySubtract())  # Меняем стратегию на вычитание
print(context.execute_strategy(5, 3))  # Вывод: 2 (результат вычитания)

'''


#Вариант 2

from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов

# Определяем интерфейс стратегии
class Strategy(ABC):
    @abstractmethod  # Декоратор для обозначения абстрактного метода
    def execute(self, data):  # Абстрактный метод для выполнения стратегии
        pass  # Метод будет реализован в подклассах

# Конкретная стратегия для сортировки по возрастанию
class SortAsc(Strategy):
    def execute(self, data):  # Реализация метода execute
        return sorted(data)  # Возвращаем отсортированный по возрастанию список

# Конкретная стратегия для сортировки по убыванию
class SortDesc(Strategy):
    def execute(self, data):  # Реализация метода execute
        return sorted(data, reverse=True)  # Возвращаем отсортированный по убыванию список

# Контекст, использующий стратегию
class Context:
    def __init__(self, strategy: Strategy):  # Инициализируем контекст с конкретной стратегией
        self.strategy = strategy  # Сохраняем стратегию

    def set_strategy(self, strategy: Strategy):  # Метод для изменения стратегии
        self.strategy = strategy  # Устанавливаем новую стратегию

    def execute_strategy(self, data):  # Метод для выполнения стратегии
        return self.strategy.execute(data)  # Вызываем метод execute стратегии

# Пример использования
data = [5, 2, 9, 1]  # Исходные данные
context = Context(SortAsc())  # Создаем контекст с стратегией сортировки по возрастанию
print(context.execute_strategy(data))  # Вывод: [1, 2, 5, 9]

context.set_strategy(SortDesc())  # Меняем стратегию на сортировку по убыванию
print(context.execute_strategy(data))  # Вывод: [9, 5, 2, 1]
