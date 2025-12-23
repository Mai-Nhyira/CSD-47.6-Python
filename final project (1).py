# main.py

from models import Room
from billing import calculate_total_cost
from utils import find_available_room, suggest_next_room

# Indexing: room numbers
room_numbers = [101, 102, 103, 104, 105]
rooms = [Room(number) for number in room_numbers]

PRICE_PER_NIGHT = 250  # GHS


def check_availability():
    for room in rooms:
        status = "Occupied" if room.is_occupied else "Available"
        print(f"Room {room.room_number}: {status}")
    print()


def check_in():
    guest_name = input("Enter guest name: ")
    index = find_available_room(rooms)

    if index is not None:
        rooms[index].check_in(guest_name)
        print(f" {guest_name} checked into Room {rooms[index].room_number}\n")
    else:
        print("No rooms available.\n")


def check_out():
    room_number = int(input("Enter room number to check out: "))

    for index, room in enumerate(rooms):
        if room.room_number == room_number:
            if room.is_occupied:
                nights = int(input("Number of nights stayed: "))
                total = calculate_total_cost(nights, PRICE_PER_NIGHT)

                room.check_out()
                print(f" Checked out successfully.")
                print(f" Total Bill: GHS {total:.2f}\n")
            else:
                suggestion = suggest_next_room(rooms, index)
                print(" Room is not occupied.")
                if suggestion:
                    print(f"➡ Try Room {suggestion}\n")
            return

    print(" Room not found.\n")


def main():
    while True:
        print("AKWAABA HOTEL MANAGEMENT SYSTEM")
        print("1. Check Room Availability")
        print("2. Check In Guest")
        print("3. Check Out Guest")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_availability()
        elif choice == "2":
            check_in()
        elif choice == "3":
            check_out()
        elif choice == "4":
            print(" Thank you for using Akwaaba Hotel System")
            break
        else:
            print(" Invalid choice\n")


if __name__ == "__main__":
    main()