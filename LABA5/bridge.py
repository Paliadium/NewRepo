'''
Вариант 1

# Определяем базовый класс Shape
class Shape:
    # Конструктор класса, принимает рендерер в качестве аргумента
    def __init__(self, renderer):
        self.renderer = renderer  # Сохраняем рендерер как атрибут экземпляра

    # Метод draw, который будет переопределен в подклассах
    def draw(self):
        pass  # Пустой метод, должен быть реализован в подклассах

# Определяем класс Circle, который наследует от Shape
class Circle(Shape):
    # Реализация метода draw для круга
    def draw(self):
        self.renderer.render_circle()  # Вызываем метод рендеринга круга

# Определяем класс Square, который наследует от Shape
class Square(Shape):
    # Реализация метода draw для квадрата
    def draw(self):
        self.renderer.render_square()  # Вызываем метод рендеринга квадрата

# Определяем базовый класс Renderer
class Renderer:
    # Метод для рендеринга круга, должен быть реализован в подклассах
    def render_circle(self):
        pass

    # Метод для рендеринга квадрата, должен быть реализован в подклассах
    def render_square(self):
        pass

# Определяем класс RasterRenderer, который наследует от Renderer
class RasterRenderer(Renderer):
    # Реализация метода рендеринга круга в растровом формате
    def render_circle(self):
        print("Рисую круг в растровом формате")  # Вывод сообщения о рендеринге круга

    # Реализация метода рендеринга квадрата в растровом формате
    def render_square(self):
        print("Рисую квадрат в растровом формате")  # Вывод сообщения о рендеринге квадрата

# Создаем экземпляр растрового рендерера
raster_renderer = RasterRenderer()

# Создаем экземпляр круга и передаем ему растровый рендерер
circle = Circle(raster_renderer)
circle.draw()  # Вывод: Рисую круг в растровом формате

# Создаем экземпляр квадрата и передаем ему растровый рендерер
square = Square(raster_renderer)
square.draw()  # Вывод: Рисую квадрат в растровом формате
'''

#Вариант 2

class NotificationSender:
    """Базовый интерфейс отправки уведомлений."""

    def send(self, message):
        pass  # Метод send, который будет реализован в подклассах


class EmailSender(NotificationSender):
    """Отправка уведомлений по электронной почте."""

    def send(self, message):
        print(f"Отправка email: {message}")  # Реализация метода send для отправки email


class SmsSender(NotificationSender):
    """Отправка уведомлений по SMS."""

    def send(self, message):
        print(f"Отправка SMS: {message}")  # Реализация метода send для отправки SMS


class Notification:
    """Абстракция уведомления."""

    def __init__(self, sender):  # Конструктор класса, принимает объект отправителя
        self.sender = sender  # Сохраняем отправителя как атрибут экземпляра

    def notify(self, message):  # Метод для уведомления
        print("Отправка уведомления...")  # Вывод сообщения о начале отправки
        self.sender.send(message)  # Вызываем метод send у отправителя для отправки сообщения


# Пример использования
email_sender = EmailSender()  # Создаем экземпляр EmailSender
sms_sender = SmsSender()  # Создаем экземпляр SmsSender

email_notification = Notification(email_sender)  # Создаем уведомление с использованием email-отправителя
sms_notification = Notification(sms_sender)  # Создаем уведомление с использованием SMS-отправителя

email_notification.notify("Это email-уведомление.")  # Отправляем email-уведомление
sms_notification.notify("Это SMS-уведомление.")  # Отправляем SMS-уведомление


