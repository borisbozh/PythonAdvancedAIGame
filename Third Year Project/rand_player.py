from player import Player
import random


class RandomAI(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_guess(self):
        guesses = []
        for x in self.suspects:
            if self.information[x] == 2:
                guesses.append(x)
                break
        if len(guesses)==0:
            guesses.append(random.choice(self.suspects))
        for x in self.weapons:
            if self.information[x] == 2:
                guesses.append(x)
                break
        if len(guesses)==1:
            guesses.append(random.choice(self.weapons))

        guesses.append(self.room_location.get_name())

        return guesses

    def change_room(self):
        if self.information[self.room_location.get_name()] == 2:
            new_room = self.room_location
        else:
            new_room = random.choice(self.room_location.get_neighbours())
        self.room_location = new_room


