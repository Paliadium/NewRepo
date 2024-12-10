
'''
 Вариант 1
class JsonData:
    """Класс для работы с JSON."""
    def get_data(self):
        return '{"name": "Alice", "age": 30}' #Возвращает строку в формате JSOn


class XmlData:
    """Класс для работы с XML."""
    def get_data(self):
        return "<person><name>Alice</name><age>30</age></person>" #Возвращает строку в формате XML


class DataAdapter:
    """Адаптер для работы с данными в едином формате."""
    def __init__(self, data_provider):
        self.data_provider = data_provider #Сохраняем переданный провайдер данных как атрибут

    # Метод для получения адаптированный данных
    def get_data(self):
        raw_data = self.data_provider.get_data()  #Получаем необрабоданные данные от провайдера
        print("Адаптация данных...")
        # Преобразуем данные в общий формат (например, словарь Python)
        if raw_data.startswith('{'):  # JSON  # Если данные начинаются с '{', это JSON
            import json # Импортируем модуль json для работы с JSON
            return json.loads(raw_data)  # Преобразуем JSON-строку в словарь Python и возвращаем
        elif raw_data.startswith('<'):  # XML # Если данные начинаются с '<', это XML
            import xml.etree.ElementTree as ET  # Импортируем модуль для работы с XML
            tree = ET.ElementTree(ET.fromstring(raw_data)) # Парсим XML-строку в дерево элементов
            root = tree.getroot()   # Получаем корневой элемент дерева
            return {child.tag: child.text for child in root}  # Создаем словарь из тегов и их текстов


# Пример использования
json_provider = JsonData()
xml_provider = XmlData()

json_adapter = DataAdapter(json_provider)
xml_adapter = DataAdapter(xml_provider)

print(json_adapter.get_data())
print(xml_adapter.get_data())

'''

#Вариант 2

class OldSystem:
    """Старый интерфейс системы."""
    def specific_request(self):
        return "Old system response."


class NewSystem:
    """Новый интерфейс системы."""
    def request(self):
        return "New system response."


class Adapter:
    """Адаптер для совместимости старой и новой системы."""
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system  # Сохраняем старую систему

    def request(self):  # Приводим старый интерфейс к новому
        return self.old_system.specific_request()


# Пример использования
old_system = OldSystem()
adapter = Adapter(old_system)  # Создаем адаптер для старой системы

print(adapter.request())  # Вызываем метод адаптера, который использует старую систему
