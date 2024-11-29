
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
