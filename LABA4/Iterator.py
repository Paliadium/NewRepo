
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
