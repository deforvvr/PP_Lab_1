from models.event import Event

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event_name, event_date):
        event_id = len(self.events) + 1
        event = Event(event_id, event_name, event_date)
        self.events.append(event)
        return event

    def get_event_by_id(self, event_id):
        for e in self.events:
            if e.event_id == event_id:
                return e
        return None

    def get_event_by_name(self, event_name):
        for e in self.events:
            if e.event_name == event_name:
                return e
        return None
