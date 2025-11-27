class Ticket:
    def __init__(self, ticket_id: int, ticket_name: str, event_date: str, price: float, is_reserved: bool = False):
        self.ticket_id = ticket_id
        self.ticket_name = ticket_name
        self.event_date = event_date
        self.price = price
        self.is_reserved = is_reserved
