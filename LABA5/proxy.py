

'''

Вариант 1

class LogProxy:

    def __init__(self, obj): #Конструктор класс LogProxy
        self._obj = obj  #Сохраняем переданный объект в атрибуте _obj для дальнейнего использования


    # Метод для перехвата вызовов к атрибутам объекта
    def __getattr__(self, attr):
        print(f"Вызывается метод {attr}")
        return getattr(self._obj, attr) #Возвращаем метод из реального объекта

# Использование класс LogProxy
class RealObject:
    def operation(self): # Метод, который будет вызываться через прокси
        print("Выполняется реальная операция")

obj = RealObject()
proxy = LogProxy(obj)
proxy.operation()

'''

#Вариант 2

class ExpensiveCalculator:
    """Класс, имитирующий ресурсоемкие вычисления."""

    def calculate(self, x):
        # Метод для выполнения сложного вычисления (в данном случае, вычисляем квадрат числа)
        print(f"Выполнение сложного вычисления для {x}...")
        return x * x  # Возвращаем квадрат числа


class CachingProxy:
    """Прокси, который кеширует результаты вычислений."""

    def __init__(self, calculator):  # Исправлено на __init__ для корректной работы конструктора
        # Сохраняем ссылку на объект калькулятора
        self.calculator = calculator
        # Инициализируем пустой словарь для кеша
        self.cache = {}

    def calculate(self, x):
        # Проверяем, есть ли результат в кеше
        if x in self.cache:
            # Если результат найден в кеше, выводим сообщение и возвращаем его
            print(f"Возврат закешированного результата для {x}")
            return self.cache[x]

        # Если результата нет в кеше, выводим сообщение о вычислении
        print(f"Результат для {x} отсутствует в кеше. Выполнение вычисления...")
        # Вызываем метод calculate у реального калькулятора
        result = self.calculator.calculate(x)
        # Сохраняем результат в кеш
        self.cache[x] = result
        # Возвращаем результат
        return result


# Пример использования

calculator = ExpensiveCalculator()  # Создаем экземпляр класса ExpensiveCalculator
proxy = CachingProxy(calculator)  # Создаем прокси-объект, передавая ему реальный калькулятор

print(proxy.calculate(5))  # Выполняем вычисление для 5 (результат не закеширован)
print(proxy.calculate(5))  # Используем кешированный результат для 5 (результат берется из кеша)
print(proxy.calculate(10))  # Выполняем новое вычисление для 10 (результат не закеширован)
print(proxy.calculate(10))  # Используем кешированный результат для 10 (результат берется из кеша)
