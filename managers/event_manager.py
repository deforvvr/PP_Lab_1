from models.event import Event

class EventManager:

    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)
        print(f"Мероприятие '{event.event_name}' добавлено.")

    def remove_event(self, event_id: int):
        event = self.get_event_by_id(event_id)
        if event:
            self.events.remove(event)
            print(f"Мероприятие '{event.event_name}' удалено.")
        else:
            print("Мероприятие не найдено.")

    def list_events(self):
        if not self.events:
            print("Список мероприятий пуст.")
            return
        for event in self.events:
            print(f"{event.event_id}: {event.event_name} ({event.event_date})")

    def get_event_by_id(self, event_id: int):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None
