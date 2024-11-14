#Вариант 1


# Абстрактный класс для кнопок
class Button:
    # Метод для отрисовки кнопки (будет переопределен в дочерних классах)
    def render(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Конкретная реализация кнопки для Windows
class WindowsButton(Button):
    # Реализация метода отрисовки для кнопки Windows
    def render(self):
        return "Отрисовка кнопки Windows"  # Возвращает строку с результатом отрисовки

# Конкретная реализация кнопки для MacOS
class MacOSButton(Button):
    # Реализация метода отрисовки для кнопки MacOS
    def render(self):
        return "Отрисовка кнопки MacOS"  # Возвращает строку с результатом отрисовки

# Абстрактный класс для чекбоксов
class Checkbox:
    # Метод для отрисовки чекбокса (будет переопределен в дочерних классах)
    def render(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Конкретная реализация чекбокса для Windows
class WindowsCheckbox(Checkbox):
    # Реализация метода отрисовки для чекбокса Windows
    def render(self):
        return "Отрисовка флажка Windows"  # Возвращает строку с результатом отрисовки

# Конкретная реализация чекбокса для MacOS
class MacOSCheckbox(Checkbox):
    # Реализация метода отрисовки для чекбокса MacOS
    def render(self):
        return "Отрисовка флажка MacOS"  # Возвращает строку с результатом отрисовки

# Абстрактный класс фабрики GUI
class GUIFactory:
    # Метод для создания кнопки (должен быть переопределен в дочерних классах)
    def create_button(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

    # Метод для создания чекбокса (должен быть переопределен в дочерних классах)
    def create_checkbox(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Конкретная реализация фабрики для Windows
class WindowsFactory(GUIFactory):
    # Реализация метода создания кнопки для Windows
    def create_button(self):
        return WindowsButton()  # Создает и возвращает экземпляр WindowsButton

    # Реализация метода создания чекбокса для Windows
    def create_checkbox(self):
        return WindowsCheckbox()  # Создает и возвращает экземпляр WindowsCheckbox

# Конкретная реализация фабрики для MacOS
class MacOSFactory(GUIFactory):
    # Реализация метода создания кнопки для MacOS
    def create_button(self):
        return MacOSButton()  # Создает и возвращает экземпляр MacOSButton

    # Реализация метода создания чекбокса для MacOS
    def create_checkbox(self):
        return MacOSCheckbox()  # Создает и возвращает экземпляр MacOSCheckbox

# Функция клиентского кода, использующая фабрику GUI
def client_code(factory: GUIFactory):
    button = factory.create_button()  # Создает кнопку через фабрику
    checkbox = factory.create_checkbox()  # Создает чекбокс через фабрику
    
    print(button.render())  # Вызывает метод отрисовки у кнопки и выводит результат на экран
    print(checkbox.render())  # Вызывает метод отрисовки у чекбокса и выводит результат на экран

# Пример использования фабрики Windows
client_code(WindowsFactory())  # Выведет: Отрисовка кнопки Windows и Отрисовка флажка Windows

# Пример использования фабрики MacOS
client_code(MacOSFactory())    # Выведет: Отрисовка кнопки MacOS и Отрисовка флажка MacOS



#Вариант 2

# Абстрактный класс для продукта A
class AbstractProductA:
    # Метод, который должен быть реализован в дочерних классах
    def useful_function_a(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Абстрактный класс для продукта B
class AbstractProductB:
    # Метод, который должен быть реализован в дочерних классах
    def useful_function_b(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Конкретная реализация продукта A1
class ConcreteProductA1(AbstractProductA):
    # Реализация метода полезной функции для продукта A1
    def useful_function_a(self):
        return "Результат продукта A1"  # Возвращает строку с результатом работы продукта A1

# Конкретная реализация продукта B1
class ConcreteProductB1(AbstractProductB):
    # Реализация метода полезной функции для продукта B1
    def useful_function_b(self):
        return "Результат продукта B1"  # Возвращает строку с результатом работы продукта B1

# Абстрактный класс фабрики, который создает продукты A и B
class AbstractFactory:
    # Метод для создания продукта A (должен быть переопределен в дочерних классах)
    def create_product_a(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

    # Метод для создания продукта B (должен быть переопределен в дочерних классах)
    def create_product_b(self):
        pass  # Заглушка, метод должен быть реализован в наследниках

# Конкретная реализация фабрики, создающая продукты A1 и B1
class ConcreteFactory1(AbstractFactory):
    # Реализация метода создания продукта A
    def create_product_a(self):
        return ConcreteProductA1()  # Создает и возвращает экземпляр ConcreteProductA1

    # Реализация метода создания продукта B
    def create_product_b(self):
        return ConcreteProductB1()  # Создает и возвращает экземпляр ConcreteProductB1

# Пример использования фабрики
factory = ConcreteFactory1()  # Создаем экземпляр конкретной фабрики

# Создаем продукт A через фабрику
product_a = factory.create_product_a()  
# Создаем продукт B через фабрику
product_b = factory.create_product_b()  

# Вызываем полезную функцию у продукта A и выводим результат на экран
print(product_a.useful_function_a())  # Вывод: Результат продукта A1
# Вызываем полезную функцию у продукта B и выводим результат на экран
print(product_b.useful_function_b())  # Вывод: Результат продукта B1
