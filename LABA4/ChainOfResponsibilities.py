#Вариант 1

'''

from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов

# Определяем абстрактный класс Handler
class Handler(ABC):  # Класс Handler наследует от ABC (абстрактного базового класса)
    def set_next(self, handler):  # Метод для установки следующего обработчика в цепочке
        self.next_handler = handler  # Устанавливаем следующий обработчик
        return handler  # Возвращаем установленный обработчик

    @abstractmethod  # Декоратор для обозначения абстрактного метода
    def handle(self, request):  # Абстрактный метод для обработки запроса
        if hasattr(self, 'next_handler'):  # Проверяем, есть ли следующий обработчик
            return self.next_handler.handle(request)  # Передаем запрос следующему обработчику
        return None  # Если нет следующего обработчика, возвращаем None

# Конкретный обработчик для обработки запросов типа A
class ConcreteHandlerA(Handler):  # Класс ConcreteHandlerA наследует от Handler
    def handle(self, request):  # Реализация метода handle для обработки запроса
        if request == "A":  # Проверяем, соответствует ли запрос типу A
            return "Обработано обработчиком A"  # Возвращаем сообщение об успешной обработке
        else:
            return super().handle(request)  # Если не A, передаем запрос следующему обработчику

# Конкретный обработчик для обработки запросов типа B
class ConcreteHandlerB(Handler):  # Класс ConcreteHandlerB наследует от Handler
    def handle(self, request):  # Реализация метода handle для обработки запроса
        if request == "B":  # Проверяем, соответствует ли запрос типу B
            return "Обработано обработчиком B"  # Возвращаем сообщение об успешной обработке
        else:
            return super().handle(request)  # Если не B, передаем запрос следующему обработчику

# Пример использования
handler_a = ConcreteHandlerA()  # Создаем экземпляр обработчика A
handler_b = ConcreteHandlerB()  # Создаем экземпляр обработчика B

handler_a.set_next(handler_b)  # Устанавливаем цепочку обработчиков: A -> B

print(handler_a.handle("A"))  # Вывод: Обработано обработчиком A (обработчик A обрабатывает запрос)
print(handler_a.handle("B"))  # Вывод: Обработано обработчиком B (обработчик B обрабатывает запрос через A)
print(handler_a.handle("C"))  # Вывод: None (запрос не обработан ни одним из обработчиков)

'''

#Вариант 2

from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов

# Абстрактный класс обработчика
class Handler(ABC):
    def set_next(self, handler):  # Метод для установки следующего обработчика
        self.next_handler = handler  # Устанавливаем следующий обработчик
        return handler  # Возвращаем установленный обработчик

    @abstractmethod  # Декоратор для обозначения абстрактного метода
    def handle(self, request):  # Абстрактный метод для обработки запроса
        if hasattr(self, 'next_handler'):  # Проверяем наличие следующего обработчика
            return self.next_handler.handle(request)  # Передаем запрос следующему обработчику
        return None  # Если нет следующего обработчика, возвращаем None

# Конкретный обработчик для обработки запросов типа "Технический"
class TechnicalHandler(Handler):
    def handle(self, request):  # Реализация метода handle
        if request == "Технический":  # Проверяем тип запроса
            return "Обработано техническим отделом"  # Возвращаем результат обработки
        else:
            return super().handle(request)  # Передаем запрос следующему обработчику

# Конкретный обработчик для обработки запросов типа "Финансовый"
class FinancialHandler(Handler):
    def handle(self, request):  # Реализация метода handle
        if request == "Финансовый":  # Проверяем тип запроса
            return "Обработано финансовым отделом"  # Возвращаем результат обработки
        else:
            return super().handle(request)  # Передаем запрос следующему обработчику

# Пример использования
technical_handler = TechnicalHandler()  # Создаем экземпляр технического обработчика
financial_handler = FinancialHandler()  # Создаем экземпляр финансового обработчика
technical_handler.set_next(financial_handler)  # Устанавливаем цепочку: Технический -> Финансовый

print(technical_handler.handle("Технический"))  # Вывод: Обработано техническим отделом
print(technical_handler.handle("Финансовый"))   # Вывод: Обработано финансовым отделом
print(technical_handler.handle("Маркетинговый"))  # Вывод: None (запрос не обработан)
