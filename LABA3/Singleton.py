class Singleton:
    _instance = None  # Хранит единственный экземпляр класса

    def __new__(cls):
        if cls._instance is None:  # Проверяем, существует ли экземпляр
            cls._instance = super(Singleton, cls).__new__(cls)  # Создаем новый экземпляр
        return cls._instance  # Возвращаем единственный экземпляр

# Пример использования
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Вывод: True, оба объекта - это один и тот же экземпляр
