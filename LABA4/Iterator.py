#Вариант 1

'''

from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection  # Храним коллекцию
        self._index = 0  # Начальный индекс

    def next(self):
        item = self._collection[self._index]  # Получаем текущий элемент
        self._index += 1  # Переходим к следующему элементу
        return item

    def has_next(self):
        return self._index < len(self._collection)  # Проверяем, есть ли еще элементы

class Collection:
    def __init__(self):
        self._items = []  # Инициализируем пустую коллекцию

    def add_item(self, item):
        self._items.append(item)  # Добавляем элемент в коллекцию

    def create_iterator(self):
        return ConcreteIterator(self._items)  # Возвращаем итератор для коллекции

# Пример использования
collection = Collection()
collection.add_item("Элемент 1")
collection.add_item("Элемент 2")
collection.add_item("Элемент 3")

iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())  # Вывод: Элемент 1, Элемент 2, Элемент 3

'''

#Вариант 2

from collections.abc import Iterable, Iterator  # Импортируем интерфейсы Iterable и Iterator

# Класс коллекции
class MyCollection(Iterable):
    def __init__(self):
        self.items = []  # Инициализируем пустой список для хранения элементов

    def add_item(self, item):  # Метод для добавления элемента в коллекцию
        self.items.append(item)  # Добавляем элемент в список

    def __iter__(self):  # Метод для получения итератора
        return MyIterator(self.items)  # Возвращаем экземпляр итератора с элементами коллекции

# Класс итератора
class MyIterator(Iterator):
    def __init__(self, items):
        self._items = items  # Сохраняем элементы коллекции
        self._index = 0  # Инициализируем индекс для итерации

    def __next__(self):  # Метод для получения следующего элемента
        if self._index < len(self._items):  # Проверяем, есть ли еще элементы
            result = self._items[self._index]  # Получаем текущий элемент
            self._index += 1  # Увеличиваем индекс для следующей итерации
            return result  # Возвращаем текущий элемент
        raise StopIteration()  # Если элементов больше нет, вызываем исключение StopIteration

# Пример использования
collection = MyCollection()  # Создаем экземпляр коллекции
collection.add_item("Элемент 1")  # Добавляем элементы в коллекцию
collection.add_item("Элемент 2")
collection.add_item("Элемент 3")

for item in collection:  # Используем цикл for для итерации по коллекции
    print(item)  # Выводим каждый элемент на экран
