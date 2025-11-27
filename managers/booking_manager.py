from models.booking import Booking

class BookingManager:
    def __init__(self):
        self.bookings = []

    def add_booking(self, user, ticket):
        if ticket.is_reserved:
            return None
        booking_id = len(self.bookings) + 1
        booking = Booking(booking_id, user, ticket)
        self.bookings.append(booking)
        ticket.is_reserved = True
        return booking

    def delete_booking(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                b.ticket.is_reserved = False
        self.bookings = [b for b in self.bookings if b.booking_id != booking_id]

    def get_booking(self, user, ticket):
        for b in self.bookings:
            if b.user == user and b.ticket == ticket:
                return b
        return None
