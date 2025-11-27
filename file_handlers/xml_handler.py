import xml.etree.ElementTree as ET
from typing import List, Type

class XmlHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def save_data(self, list_of_objects: List):
        root_name = self._get_root_name(list_of_objects)
        root = ET.Element(root_name)

        for obj in list_of_objects:
            obj_elem = ET.SubElement(root, obj.__class__.__name__)
            for key, value in obj.__dict__.items():
                if hasattr(value, "__dict__"):
                    # Сериализуем вложенные объекты
                    sub_elem = ET.SubElement(obj_elem, key)
                    for sub_key, sub_value in value.__dict__.items():
                        child = ET.SubElement(sub_elem, sub_key)
                        child.text = str(sub_value)
                else:
                    child = ET.SubElement(obj_elem, key)
                    child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)

    def load_data(self, cls: Type):
        try:
            tree = ET.parse(self.filename)
        except FileNotFoundError:
            return []

        root = tree.getroot()
        objects = []

        for obj_elem in root:
            data = {}
            for field in obj_elem:
                if list(field):  # вложенный объект
                    sub_data = {sub.tag: self._convert_value(sub.text) for sub in field}
                    data[field.tag] = cls.__annotations__.get(field.tag, object)(**sub_data)
                else:
                    data[field.tag] = self._convert_value(field.text)
            objects.append(cls(**data))
        return objects

    def _convert_value(self, value):
        # Пробуем преобразовать к int или float, иначе оставляем str
        if value is None:
            return None
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    def _get_root_name(self, list_of_objects):
        if not list_of_objects:
            return "Data"
        return list_of_objects[0].__class__.__name__ + "s"
