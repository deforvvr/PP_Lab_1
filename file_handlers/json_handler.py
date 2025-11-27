import json


class FileHandlerJSON:

    def __init__(self, filename: str):
        self.filename = filename

    def save_data(self, data: list):
        with open(self.filename, "w", encoding="utf-8") as f:
            # Преобразуем объекты в словари
            json.dump([obj.__dict__ for obj in data], f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {self.filename}")

    def load_data(self, cls):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data_list = json.load(f)
            return [cls(**item) for item in data_list]
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден, возвращаем пустой список.")
            return []
