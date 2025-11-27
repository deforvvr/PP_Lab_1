class Ticket:

    def __init__(self, ticket_id: int, ticket_name: str, event_date: str, price: float):
        self.ticket_id = ticket_id      # уникальный идентификатор билета
        self.ticket_name = ticket_name  # название мероприятия
        self.event_date = event_date    # дата события
        self.price = price              # цена билета
        self.is_reserved = False        # статус бронирования (по умолчанию False)

