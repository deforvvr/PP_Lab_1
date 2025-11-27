import xml.etree.ElementTree as ET


class FileHandlerXML:

    def __init__(self, filename: str):
        self.filename = filename

    def save_data(self, data: list, root_name: str = "data", item_name: str = "item"):
        root = ET.Element(root_name)
        for obj in data:
            item_elem = ET.SubElement(root, item_name)
            for key, value in obj.__dict__.items():
                child = ET.SubElement(item_elem, key)
                child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        print(f"Данные сохранены в {self.filename}")

    def load_data(self, cls, root_name: str = "data", item_name: str = "item"):
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            result = []
            for item_elem in root.findall(item_name):
                kwargs = {child.tag: self._convert_type(child.text) for child in item_elem}
                result.append(cls(**kwargs))
            return result
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден, возвращаем пустой список.")
            return []

    def _convert_type(self, value):
        for cast in (int, float):
            try:
                return cast(value)
            except ValueError:
                continue
        return value
