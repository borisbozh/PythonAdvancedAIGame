import random
class Player:
    def __init__(self, name):
        self.status = True
        self.room_location = None
        self.name = name
        self.right_n = []
        self.cards=[]
        self.suspects = ["Colonel Mustard", "Professor Plum",
                         "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White"]
        self.weapons = ["Dagger", "Candlestick",
                        "Revolver", "Rope", "Lead piping", "Spanner"]
        self.rooms = ["Hall", "Lounge", "Library", "Kitchen",
                      "Billiard Room", "Study", "Ballroom", "Conservatory", "Cellar"]

        self.all_cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett",
                          "Mrs. White", "Dagger", "Candlestick",
                          "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen",
                          "Billiard Room", "Study", "Ballroom", "Conservatory", "Cellar"]
        self.information = {}
        for card in self.all_cards:
            self.information.update({card:0})

    def make_guess(self):
        guesses=[]
        for x in self.suspects:
            if self.information[x]==0 or self.information[x]==2:
                guesses.append(x)
                break
        for x in self.weapons:
            if self.information[x]==0 or self.information[x]==2:
                guesses.append(x)
                break
        guesses.append(self.room_location.get_name())
        return guesses

    def ans_guess(self, guess):
        for x in guess:
            if x in self.cards:
                answer = x
                break
            else:
                answer = False
        return answer



    def info_update(self, card):
        if card in self.information.keys():
            self.information[card] = 1

    def info_update2(self, card):
        if card in self.information.keys():
            self.information[card] = 2

    def set_room(self, room):
        self.room_location = room

    def change_room(self):
        if self.information[self.room_location.get_name()] == 2:
            return

        for x in self.room_location.get_neighbours():
            if self.information[x.name] == 0 or self.information[x.name] == 2:
                new_room = x
                self.room_location = new_room
                return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                if self.information[y.name] == 0 or self.information[y.name] == 2:
                    new_room = x
                    self.room_location = new_room
                    return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                for z in y.get_neighbours():
                    if self.information[z.name] == 0 or self.information[z.name] == 2:
                        new_room = x
                        self.room_location = new_room
                        return

        self.room_location = random.choice(self.room_location.get_neighbours)
#