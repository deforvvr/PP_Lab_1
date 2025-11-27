from models.user import User
from models.ticket import Ticket

class Booking:
    def __init__(self, booking_id: int, user: User, ticket: Ticket):
        self.booking_id = booking_id
        self.user = user
        self.ticket = ticket
