# Вариант 1

'''
# Базовый класс для всех типов уведомлений
class Notification:
    # Метод, который будет переопределен в дочерних классах
    def notify(self):
        pass  # Заглушка, метод не реализован

# Класс для уведомления по электронной почте, наследуется от Notification
class EmailNotification(Notification):
    # Реализация метода notify для email-уведомления
    def notify(self):
        return "Отправлено уведомление по электронной почте."  # Возвращает сообщение об отправке

# Класс для SMS-уведомления, также наследуется от Notification
class SMSNotification(Notification):
    # Реализация метода notify для SMS-уведомления
    def notify(self):
        return "Отправлено SMS-уведомление."  # Возвращает сообщение об отправке

# Базовый класс для фабрик уведомлений
class NotificationFactory:
    # Метод, который будет переопределен в дочерних классах
    def create_notification(self):
        pass  # Заглушка, метод не реализован

# Фабрика для создания email-уведомлений
class EmailNotificationFactory(NotificationFactory):
    # Реализация метода create_notification для создания email-уведомления
    def create_notification(self):
        return EmailNotification()  # Возвращает экземпляр EmailNotification

# Фабрика для создания SMS-уведомлений
class SMSNotificationFactory(NotificationFactory):
    # Реализация метода create_notification для создания SMS-уведомления
    def create_notification(self):
        return SMSNotification()  # Возвращает экземпляр SMSNotification

# Функция, демонстрирующая использование фабрики уведомлений
def client_code(factory: NotificationFactory):
    notification = factory.create_notification()  # Создает уведомление с помощью фабрики
    print(notification.notify())  # Вызывает метод notify и выводит результат на экран

# Пример использования фабрики email-уведомлений
client_code(EmailNotificationFactory())  # Выведет: Отправлено уведомление по электронной почте.
# Пример использования фабрики SMS-уведомлений
client_code(SMSNotificationFactory())     # Выведет: Отправлено SMS-уведомление.

'''

#Вариант 2
# Класс, представляющий продукт
class Product:
    # Метод, выполняющий операцию продукта
    def operation(self):
        return "Результат операции продукта"  # Возвращает строку с результатом операции

# Базовый класс для создателей продуктов
class Creator:
    # Метод фабрики, который должен быть переопределен в дочерних классах
    def factory_method(self):
        raise NotImplementedError("Вы должны переопределить этот метод")  # Генерирует ошибку, если метод не переопределен

# Конкретная реализация создателя, наследуется от Creator
class ConcreteCreator(Creator):
    # Реализация метода фабрики для создания продукта
    def factory_method(self):
        return Product()  # Создает и возвращает экземпляр класса Product

# Пример использования конкретного создателя
creator = ConcreteCreator()  # Создаем экземпляр ConcreteCreator
product = creator.factory_method()  # Вызываем метод фабрики для получения продукта
print(product.operation())  # Вызываем метод operation у продукта и выводим результат на экран
# Вывод: Результат операции продукта
