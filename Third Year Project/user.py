from player import Player


class User(Player):
    def __init__(self, name):
        super().__init__(name)

    def inputNumber(slef, message):
        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not an integer! Try again: ")
                continue
            else:
                return userInput

    def change_info(self):
        index = 1
        for x in self.all_cards:
            print(index, ".", x, " has information ", self.information[x])
            index += 1
        choice = self.inputNumber("Enter the index of the card you want to change: ")
        info = self.inputNumber("Enter the number you want as information: ")
        if self.all_cards[choice-1] in self.information.keys():
            self.information[self.all_cards[choice-1]] = info

    def make_guess(self):

        guesses = []
        guess = []

        print('')
        print("Pick your suspect: ")
        print('')
        index=1
        for x in self.suspects:
            guess.append(x)
            print(index, "." , x, " has information ", self.information[x])
            index+=1
        choice = self.inputNumber("Enter the index of the suspect: ")
        while not (choice >= 0 and choice <= index - 1):
            choice = self.inputNumber("Enter the correct index of the suspect: ")
        guesses.append(guess[choice-1])
        guess.clear()
        print("Pick your weapon: ")
        print('')
        index = 1
        for x in self.weapons:
            guess.append(x)
            print(index, "." , x, " has information ", self.information[x])
            index += 1
        choice = self.inputNumber("Enter the index of the weapon: ")
        while not (choice >= 0 and choice <= index - 1):
            choice = self.inputNumber("Enter the correct index of the weapon: ")
        guesses.append(guess[choice-1])
        guess.clear()
        guesses.append(self.room_location.get_name())
        return guesses

    def ans_guess(self, guess):
        index = 1
        check = 0
        new_guess = []
        for x in guess:
            if x in self.cards:
                check=1
                new_guess.append(x)
                print(index, ".", x, " has been searched ")
                index+=1
        if check ==0:
            answer = False
        else:
            choice = self.inputNumber("Enter the index of the card you want to show: ")
            while not (choice >= 0 and choice <= index-1):
                choice = self.inputNumber("Enter a valid index of a card: ")
            answer = new_guess[choice - 1]
        return answer

    def change_room(self):
        print("User ", self.name, "'s turn")
        print("")
        for x in self.rooms:
            print(x, " has information ", self.information[x])
        print("...........................")
        print("          Room Map         ")
        print("...........................")
        print("Kitchen   Ballroom   Conservatory")
        print("")
        print("                     Billiard Room")
        print("Cellar")
        print("                     Library")
        print("")
        print("Lounge    Hall       Study")
        print("")
        print("Possible rooms : ")
        num=1
        for x in self.room_location.get_neighbours():
            print(num, ".", x.get_name())
            num+=1
        choice = self.inputNumber("Enter the index of the room: ")
        while not (choice >= 0 and choice <= num - 1):
            choice = self.inputNumber("Enter correct index of a room: ")
        self.room_location = self.room_location.get_neighbours()[choice-1]

    def make_accusation(self):
        accusation = []
        guess=[]
        print('')
        print("Pick your suspect: ")
        print('')
        index = 1
        for x in self.suspects:
            guess.append(x)
            print(index, ".", x, " has information ", self.information[x])
            index += 1
        choice = self.inputNumber("Enter the index of the card you want to use: ")
        while not (choice >= 0 and choice <= index - 1):
            choice = self.inputNumber("Enter the correct index of the card you want to use: ")
        accusation.append(guess[choice - 1])
        guess.clear()
        print("Pick your weapon: ")
        print('')
        index = 1
        for x in self.weapons:
            guess.append(x)
            print(index, ".", x, " has information ", self.information[x])
            index += 1
        choice = self.inputNumber("Enter the index of the card you want to use: ")
        while not (choice >= 0 and choice <= index - 1):
            choice = self.inputNumber("Enter the correct index of the card you want to use: ")
        accusation.append(guess[choice - 1])
        guess.clear()
        print("Pick your room: ")
        print('')
        index = 1
        for x in self.rooms:
            guess.append(x)
            print(index, ".", x, " has information ", self.information[x])
            index += 1
        choice = self.inputNumber("Enter the index of the card you want to use: ")
        while not (choice >= 0 and choice <= index - 1):
            choice = self.inputNumber("Enter the correct index of the card you want to use: ")
        accusation.append(guess[choice - 1])
        guess.clear()
        return accusation


