from player import Player
import random

class AdvancedAI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.other_inf = [{},{},{},{},{}]
        self.prints = 0  #change to 1 for prints of adv ai
        for x in self.other_inf:
            for card in self.all_cards:
                x.update({card: 0})

        self.unknown_pairs = [[],[],[],[],[]]
        self.unknown_three = [[], [], [], [], []]


    def update_other(self, card):
        for person in self.right_n:
            if self.other_inf[self.right_n.index(person)][card] == 0 and self.right_n.index(person) != (self.information[card]-3):
                self.other_inf[self.right_n.index(person)][card] = 1
                self.test_func(card, person)
        if self.prints == 1:
            print("because he has it we enter that the rest dont")
            for player in self.right_n:
                print(self.other_inf[self.right_n.index(player)][card])



    def test_func(self, card, person):
        for num in range(len(self.unknown_pairs[self.right_n.index(person)])):
            for x in self.unknown_pairs[self.right_n.index(person)]:
                if card in x:
                    for car in x:
                        if car != card and (self.right_n.index(person) != (self.information[card]-3) or self.other_inf[self.right_n.index(person)][card] == 1):
                            self.information[car] = 3 + self.right_n.index(person)
                            if self.prints == 1:
                                print(self.unknown_pairs)
                                print("")
                                print("333333333333 LEARNED", car, "FROM", person.name)
                                print("")
                            self.update_other(car)
                        if self.right_n.index(person) == (self.information[car]-3):
                            if x in self.unknown_pairs[self.right_n.index(person)]:
                                self.unknown_pairs[self.right_n.index(person)].remove(x)
                                if self.prints == 1:
                                    print("$$$$$$ REMOVED $$$$$$")
                                    print(self.unknown_pairs)
        self.test_func2(card, person)

    def test_func2(self, card, person):
        for num in range(len(self.unknown_three[self.right_n.index(person)])):
            for x in self.unknown_three[self.right_n.index(person)]:
                if card in x:
                    cards = []
                    counter = 0
                    new_card = ''
                    for car in x:
                        if car != card and (self.right_n.index(person) != (self.information[card] - 3) or
                                            self.other_inf[self.right_n.index(person)][card] == 1):
                            cards.append(car)
                    for cardd in cards:
                        if (self.right_n.index(person) != (self.information[cardd] - 3) or self.other_inf[self.right_n.index(person)][cardd] == 1) and self.information[cardd] != 0:
                            counter += 1
                        else :
                            new_card = cardd
                    if counter == 1:
                        self.information[new_card] = 3 + self.right_n.index(person)
                        if self.prints == 1:
                            print(self.unknown_three)
                            print("777777")
                            print("7777777777 LEARNED", new_card, "FROM", person.name)
                            print("7777777")
                        self.update_other(new_card)
                    for car in x:
                        if self.right_n.index(person) == (self.information[car] - 3):
                            if x in self.unknown_three[self.right_n.index(person)]:
                                self.unknown_three[self.right_n.index(person)].remove(x)
                                if self.prints == 1:
                                    print("7777777 REMOVED $77")
                                    print(self.unknown_three)

    def env_check(self, card):
        count = 0
        for person in self.right_n:
            if self.other_inf[self.right_n.index(person)][card] == 1:
                count +=1
        if count == len(self.right_n):
            if self.information[card] != 2 and self.information[card] != 1:
                self.information[card] = 2
                self.update_other(card)
                if self.prints == 1:
                    print("/////////////// LEARNED ENVELOPE CARD", card)




    def advanced_info3(self, guess, person):
        for card in guess:
            if self.other_inf[self.right_n.index(person)][card] != 1:
                self.other_inf[self.right_n.index(person)][card] = 1
                self.test_func(card, person)
                self.env_check(card)



    def info_update(self, card, person):
        if card in self.information.keys():
            self.information[card] = 3+self.right_n.index(person)
            self.test_func(card, person)
            self.update_other(card)


    def advanced_info(self, guess, person, current_player):
        count = 0
        new_card= ''
        for card in guess:
            if card in self.cards or (self.information[card] != (3+self.right_n.index(person)) and self.information[card] !=0 ) or self.other_inf[self.right_n.index(person)][card] == 1:
                count +=1
            else:
                new_card = card
        if count == 2:
            if self.information[new_card] != 3+self.right_n.index(person):
                self.information[new_card] = 3+self.right_n.index(person)
                self.test_func(new_card, person)
                self.update_other(new_card)
                if self.prints == 1:
                    print('')
                    print("!!!!!!!!!!!!!! The AI learned ", new_card)
                    print('')

        counter = 0
        unknown = []
        for card in guess:
            if self.other_inf[self.right_n.index(person)][card] == 1 or (self.information[card] != (3+self.right_n.index(person)) and self.information[card] !=0 ):
                counter+=1
            elif self.information[card] == (3+self.right_n.index(person)):
                counter += 18
            else:
                unknown.append(card)
        if counter == 1:
            if current_player != self:
                if unknown not in self.unknown_pairs[self.right_n.index(person)]:
                    self.unknown_pairs[self.right_n.index(person)].append(unknown)
                    if self.prints == 1:
                        print(self.unknown_pairs)

        counter = 0
        unknown = []
        for card in guess:
            if self.other_inf[self.right_n.index(person)][card] == 1 or (
                    self.information[card] != (3 + self.right_n.index(person)) and self.information[card] != 0):
                counter += 1
            elif self.information[card] == (3 + self.right_n.index(person)):
                counter += 18
            else:
                unknown.append(card)
        if counter == 0:
            if current_player != self:
                if unknown not in self.unknown_three[self.right_n.index(person)]:
                    self.unknown_three[self.right_n.index(person)].append(unknown)
                    # if self.prints == 1:
                    print(self.unknown_three)

        count = 0
        env_card = ''
        for card in self.weapons:
            if self.information[card] == 0:
                count +=1
                env_card = card
            if self.information[card] == 2:
                count +=100
        if count == 1:
            self.information[env_card] = 2
            self.test_func(env_card, person)
            if self.prints == 1:
                print("THE AI LEARNED", env_card)
            self.update_other(env_card)

        count = 0
        env_card = ''
        for card in self.suspects:
            if self.information[card] == 0:
                count += 1
                env_card = card
            if self.information[card] == 2:
                count +=100
        if count == 1:
            self.information[env_card] = 2
            self.test_func(env_card, person)
            if self.prints == 1:
                print("THE AI LEARNED", env_card)
            self.update_other(env_card)

        count = 0
        env_card = ''
        for card in self.rooms:
            if self.information[card] == 0:
                count += 1
                env_card = card
            if self.information[card] == 2:
                count +=100
        if count == 1:
            self.information[env_card] = 2
            self.test_func(env_card, person)
            if self.prints == 1:
                print("THE AI LEARNED", env_card)
            self.update_other(env_card)

        return



    def advanced_info2(self, guess):
        count = 0
        new_card= ''
        for card in guess:
            if self.information[card]!=2 and self.information[card]!=0:
                count +=1
            else:
                new_card = card
        if count == 2:
            self.information[new_card] = 2
            if self.prints == 1:
                print('')
                print("!!!!!!!!!!!!!! The AI learned ", new_card, " from the deck")
                print('')
            self.update_other(new_card)
        return

    def change_room(self):
        for x in self.room_location.get_neighbours():
            if self.information[x.name] == 2:
                new_room = x
                self.room_location = new_room
                return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                if self.information[y.name] == 2:
                    new_room = x
                    self.room_location = new_room
                    return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                for z in y.get_neighbours():
                    if self.information[z.name] == 2:
                        new_room = x
                        self.room_location = new_room
                        return

        for x in self.room_location.get_neighbours():
            if self.information[x.name] == 0:
                new_room = x
                self.room_location = new_room
                return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                if self.information[y.name] == 0:
                    new_room = x
                    self.room_location = new_room
                    return

        for x in self.room_location.get_neighbours():
            for y in x.get_neighbours():
                for z in y.get_neighbours():
                    if self.information[z.name] == 0:
                        new_room = x
                        self.room_location = new_room
                        return

        self.room_location = random.choice(self.room_location.get_neighbours)

    def make_guess(self):
        guesses=[]
        for x in self.suspects:
            if self.information[x]==2:
                guesses.append(x)
                break

        if len(guesses) == 0:
            for x in self.suspects:
                if self.information[x] == 0:
                    guesses.append(x)
                    break

        for x in self.weapons:
            if self.information[x]==2:
                guesses.append(x)
                break


        if len(guesses) == 1:
            for x in self.weapons:
                if self.information[x] == 0:
                    guesses.append(x)
                    break
        guesses.append(self.room_location.get_name())
        return guesses

    def make_accusation(self):
        accusation = []
        for x in self.suspects:
            if self.information[x] == 2:
                accusation.append(x)
        for x in self.weapons:
            if self.information[x] == 2:
                accusation.append(x)
        for x in self.rooms:
            if self.information[x] == 2:
                accusation.append(x)
        if len(accusation) == 3:
            return accusation



