from models.ticket import Ticket
from exceptions.ticket_not_found import TicketNotFoundError
from exceptions.already_reserved import AlreadyReservedError

class TicketManager:

    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)
        print(f"Билет '{ticket.ticket_name}' добавлен.")

    def remove_ticket(self, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            self.tickets.remove(ticket)
            print(f"Билет '{ticket.ticket_name}' удалён.")
        else:
            raise TicketNotFoundError(f"Билет с id {ticket_id} не найден.")

    def list_tickets(self):
        if not self.tickets:
            print("Список билетов пуст.")
            return
        for ticket in self.tickets:
            status = "Забронирован" if ticket.is_reserved else "Доступен"
            print(f"{ticket.ticket_id}: {ticket.ticket_name} ({ticket.event_date}) - {ticket.price}₽ [{status}]")

    def get_ticket_by_id(self, ticket_id: int):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def reserve_ticket(self, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            if ticket.is_reserved:
                raise AlreadyReservedError(f"Билет '{ticket.ticket_name}' уже забронирован.")
            ticket.is_reserved = True
            print(f"Билет '{ticket.ticket_name}' забронирован.")
        else:
            raise TicketNotFoundError(f"Билет с id {ticket_id} не найден.")
