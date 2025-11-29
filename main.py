from models.user import User
from models.ticket import Ticket
from models.booking import Booking
from models.event import Event
from managers.user_manager import UserManager
from managers.ticket_manager import TicketManager
from managers.booking_manager import BookingManager
from managers.event_manager import EventManager
from file_handlers.json_handler import JsonHandler
from file_handlers.xml_handler import XmlHandler
from exceptions.user_not_found import UserNotFoundError
from exceptions.event_not_found import EventNotFoundError
from exceptions.ticket_not_found import TicketNotFoundError
from exceptions.booking_not_found import BookingNotFoundError
from exceptions.already_reserved import AlreadyReservedError
import os

def main():
    # --- Менеджеры ---
    user_manager = UserManager()
    event_manager = EventManager()
    ticket_manager = TicketManager()
    booking_manager = BookingManager()

    # --- Хендлеры файлов ---
    users_json = JsonHandler("data/users.json")
    tickets_json = JsonHandler("data/tickets.json")
    bookings_json = JsonHandler("data/bookings.json")
    events_json = JsonHandler("data/events.json")

    users_xml = XmlHandler("data/users.xml")
    tickets_xml = XmlHandler("data/tickets.xml")
    bookings_xml = XmlHandler("data/bookings.xml")
    events_xml = XmlHandler("data/events.xml")

    # --- Создаем папку data, если нет ---
    os.makedirs("data", exist_ok=True)

    # --- Загрузка данных из JSON при старте ---
    user_manager.users = users_json.load_data(User)
    ticket_manager.tickets = tickets_json.load_data(Ticket)
    booking_manager.bookings = bookings_json.load_data(Booking)
    event_manager.events = events_json.load_data(Event)

    while True:
        print("\nМеню:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Добавить билет")
        print("4. Удалить билет")
        print("5. Добавить бронирование")
        print("6. Удалить бронирование")
        print("7. Показать всех пользователей")
        print("8. Показать все билеты")
        print("9. Показать все бронирования")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                username = input("Введите имя пользователя: ")
                email = input("Введите email пользователя: ")
                if not username or not email:
                    raise ValueError("Имя пользователя и email не могут быть пустыми.")
                user = user_manager.add_user(username, email)
                print(f"Пользователь '{user.username}' добавлен.")
                users_json.save_data(user_manager.users)
                users_xml.save_data(user_manager.users)
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")

        elif choice == "2":
            try:
                user_id = int(input("Введите ID пользователя для удаления: "))
                user = user_manager.get_user_by_id(user_id)
                if not user:
                    raise UserNotFoundError(f"Пользователь с ID {user_id} не найден.")
                user_manager.delete_user(user_id)
                print(f"Пользователь с ID {user_id} удалён.")
                users_json.save_data(user_manager.users)
                users_xml.save_data(user_manager.users)
            except UserNotFoundError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")

        elif choice == "3":
            try:
                ticket_name = input("Введите название билета: ")
                price = float(input("Введите цену билета: "))
                event_id = int(input("Введите ID события для билета: "))
                event = event_manager.get_event_by_id(event_id)
                if not event:
                    raise EventNotFoundError(f"Событие с ID {event_id} не найдено.")
                ticket = Ticket(ticket_id=len(ticket_manager.tickets)+1,
                                ticket_name=ticket_name,
                                event_date=event.event_date,
                                price=price)
                ticket_manager.add_ticket(ticket)
                event.tickets.append(ticket)
                print(f"Билет '{ticket.ticket_name}' добавлен.")
                tickets_json.save_data(ticket_manager.tickets)
                tickets_xml.save_data(ticket_manager.tickets)
            except EventNotFoundError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректные данные (числа для ID и цены).")

        elif choice == "4":
            try:
                ticket_id = int(input("Введите ID билета для удаления: "))
                ticket = ticket_manager.get_ticket_by_id(ticket_id)
                if not ticket:
                    raise TicketNotFoundError(f"Билет с ID {ticket_id} не найден.")
                ticket_manager.delete_ticket(ticket_id)
                print(f"Билет с ID {ticket_id} удалён.")
                tickets_json.save_data(ticket_manager.tickets)
                tickets_xml.save_data(ticket_manager.tickets)
            except TicketNotFoundError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")

        elif choice == "5":
            try:
                user_id = int(input("Введите ID пользователя: "))
                ticket_id = int(input("Введите ID билета: "))
                user = user_manager.get_user_by_id(user_id)
                if not user:
                    raise UserNotFoundError(f"Пользователь с ID {user_id} не найден.")
                ticket = ticket_manager.get_ticket_by_id(ticket_id)
                if not ticket:
                    raise TicketNotFoundError(f"Билет с ID {ticket_id} не найден.")
                if ticket.is_reserved:
                    raise AlreadyReservedError(f"Билет с ID {ticket_id} уже забронирован.")
                booking = booking_manager.add_booking(user, ticket)
                print(f"Бронирование #{booking.booking_id} добавлено: {user.username} -> {ticket.ticket_name}")
                bookings_json.save_data(booking_manager.bookings)
                bookings_xml.save_data(booking_manager.bookings)
            except (UserNotFoundError, TicketNotFoundError, AlreadyReservedError) as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректные ID (числа).")

        elif choice == "6":
            try:
                booking_id = int(input("Введите ID бронирования для удаления: "))
                booking = None
                for b in booking_manager.bookings:
                    if b.booking_id == booking_id:
                        booking = b
                        break
                if not booking:
                    raise BookingNotFoundError(f"Бронирование с ID {booking_id} не найдено.")
                booking_manager.delete_booking(booking_id)
                print(f"Бронирование с ID {booking_id} удалено.")
                bookings_json.save_data(booking_manager.bookings)
                bookings_xml.save_data(booking_manager.bookings)
            except BookingNotFoundError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")

        elif choice == "7":
            print("Пользователи:")
            for u in user_manager.users:
                print(f"ID {u.user_id} | {u.username} | {u.email}")

        elif choice == "8":
            print("Билеты:")
            for t in ticket_manager.tickets:
                print(f"ID {t.ticket_id} | {t.ticket_name} | {t.event_date} | {t.price}р. | Забронирован: {t.is_reserved}")

        elif choice == "9":
            print("Бронирования:")
            for b in booking_manager.bookings:
                print(f"ID {b.booking_id} | {b.user.username} -> {b.ticket.ticket_name}")

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
