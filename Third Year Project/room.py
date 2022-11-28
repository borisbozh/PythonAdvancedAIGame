class Room:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.neighbours.append(self)

    def add_neighbour(self, room):
        self.neighbours.append(room)
        room.neighbours.append(self)

    def get_neighbours(self):
        return self.neighbours

    def get_name(self):
        return self.name

