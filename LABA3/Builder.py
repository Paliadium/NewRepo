# Класс Car представляет автомобиль
class Car:
    # Метод инициализации класса Car
    def __init__(self):  # Исправлено: должно быть __init__, а не init
        self.parts = []  # Инициализация списка для хранения частей автомобиля

    # Метод для добавления части автомобиля
    def add_part(self, part: str):
        self.parts.append(part)  # Добавление переданной части в список

    # Метод для отображения всех частей автомобиля
    def show_parts(self):
        return f"Автомобиль состоит из: {', '.join(self.parts)}"  # Формирование строки с перечислением частей

# Класс CarBuilder отвечает за создание автомобиля
class CarBuilder:
    # Метод инициализации класса CarBuilder
    def __init__(self):  # Исправлено: должно быть __init__, а не init
        self.car = Car()  # Создание нового экземпляра автомобиля

    # Метод для сборки двигателя
    def build_engine(self):
        self.car.add_part("Двигатель")  # Добавление части "Двигатель" в автомобиль

    # Метод для сборки колес
    def build_wheels(self):
        self.car.add_part("Колеса")  # Добавление части "Колеса" в автомобиль

    # Метод для сборки кузова
    def build_body(self):
        self.car.add_part("Кузов")  # Добавление части "Кузов" в автомобиль

    # Метод для получения готового автомобиля
    def get_car(self) -> Car:
        return self.car  # Возврат экземпляра автомобиля

# Пример использования класса CarBuilder
def client_code():
    builder = CarBuilder()  # Создание экземпляра сборщика автомобиля

    builder.build_engine()  # Сборка двигателя
    builder.build_wheels()  # Сборка колес
    builder.build_body()    # Сборка кузова
    
    car = builder.get_car()  # Получение готового автомобиля
    print(car.show_parts())  # Вывод на экран: Автомобиль состоит из: Двигатель, Колеса, Кузов

client_code()  # Вызов функции client_code для запуска примера
