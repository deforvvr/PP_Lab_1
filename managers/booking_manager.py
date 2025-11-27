from models.booking import Booking
from exceptions.booking_not_found import BookingNotFoundError
from exceptions.already_reserved import AlreadyReservedError

class BookingManager:

    def __init__(self):
        self.bookings = []

    def add_booking(self, booking: Booking):
        if booking.ticket.is_reserved:
            raise AlreadyReservedError(f"Билет '{booking.ticket.ticket_name}' уже забронирован.")
        booking.ticket.is_reserved = True
        self.bookings.append(booking)
        print(f"Бронирование #{booking.booking_id} добавлено: {booking.user.username} -> {booking.ticket.ticket_name}")

    def list_bookings(self):
        if not self.bookings:
            print("Список бронирований пуст.")
            return
        for booking in self.bookings:
            print(f"{booking.booking_id}: {booking.user.username} забронировал '{booking.ticket.ticket_name}'")

    def get_booking_by_id(self, booking_id: int):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        raise BookingNotFoundError(f"Бронирование с id {booking_id} не найдено.")

    def remove_booking(self, booking_id: int):
        booking = self.get_booking_by_id(booking_id)
        self.bookings.remove(booking)
        booking.ticket.is_reserved = False
        print(f"Бронирование #{booking.booking_id} удалено.")
