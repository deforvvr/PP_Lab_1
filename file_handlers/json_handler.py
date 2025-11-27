import json
import os

class JsonHandler:
    def __init__(self, filename):
        self.filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def save_data(self, list_of_objects):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([self._obj_to_dict(obj) for obj in list_of_objects], f, ensure_ascii=False, indent=4)

    def load_data(self, cls):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            data_list = json.load(f)
        return [self._dict_to_obj(cls, data) for data in data_list]

    def _obj_to_dict(self, obj):
        if hasattr(obj, "__dict__"):
            d = {}
            for k, v in obj.__dict__.items():
                if hasattr(v, "__dict__"):
                    d[k] = self._obj_to_dict(v)
                else:
                    d[k] = v
            return d
        return obj

    def _dict_to_obj(self, cls, data):
        from models.user import User
        from models.ticket import Ticket
        from models.booking import Booking
        from models.event import Event

        for key, value in data.items():
            if key == "user" and isinstance(value, dict):
                data[key] = self._dict_to_obj(User, value)
            elif key == "ticket" and isinstance(value, dict):
                data[key] = self._dict_to_obj(Ticket, value)
        return cls(**data)
