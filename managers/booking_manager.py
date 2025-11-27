from models.booking import Booking

class BookingManager:

    def __init__(self):
        self.bookings = []

    def add_booking(self, booking: Booking):
        self.bookings.append(booking)
        booking.ticket.is_reserved = True  # сразу ставим статус забронирован
        print(f"Бронирование #{booking.booking_id} добавлено: {booking.user.username} -> {booking.ticket.ticket_name}")

    def list_bookings(self):
        if not self.bookings:
            print("Список бронирований пуст.")
            return
        for booking in self.bookings:
            print(f"{booking.booking_id}: {booking.user.username} забронировал '{booking.ticket.ticket_name}'")
