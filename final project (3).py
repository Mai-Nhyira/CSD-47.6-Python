# utils.py

def find_available_room(rooms):
    for index, room in enumerate(rooms):
        if not room.is_occupied:
            return index
    return None


def suggest_next_room(rooms, current_index):
    if current_index + 1 < len(rooms):
        return rooms[current_index + 1].room_number
    return None





