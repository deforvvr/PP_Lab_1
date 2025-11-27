class Event:

    def __init__(self, event_id: int, event_name: str, event_date: str):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.tickets = []  # список билетов на мероприятие
