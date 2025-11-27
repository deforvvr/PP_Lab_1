from models.ticket import Ticket

class TicketManager:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def delete_ticket(self, ticket_id):
        self.tickets = [t for t in self.tickets if t.ticket_id != ticket_id]

    def get_ticket_by_id(self, ticket_id):
        for t in self.tickets:
            if t.ticket_id == ticket_id:
                return t
        return None

    def get_ticket_by_name(self, ticket_name):
        for t in self.tickets:
            if t.ticket_name == ticket_name:
                return t
        return None
