# models.py

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False
        self.guest_name = None

    def check_in(self, guest_name):
        self.is_occupied = True
        self.guest_name = guest_name

    def check_out(self):
        self.is_occupied = False
        self.guest_name = None