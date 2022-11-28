from player import Player
import random
from rand_player import RandomAI
from user import User
from room import Room
from AdvancedAI import AdvancedAI
import time

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again: ")
       continue
    else:
       return userInput

suspects = ["Colonel Mustard", "Professor Plum",
                         "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White"]
weapons = ["Dagger", "Candlestick",
                        "Revolver", "Rope", "Lead piping", "Spanner"]
rooms = ["Hall", "Lounge", "Library", "Kitchen",
                      "Billiard Room", "Study", "Ballroom", "Conservatory", "Cellar"]

all_cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett",
                          "Mrs. White", "Dagger", "Candlestick",
                          "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen",
                          "Billiard Room", "Study", "Ballroom", "Conservatory", "Cellar"]

names = ["Lionel", "Atticus", "Fitzgerald", "Beatrix", "Mia", "Romulus"]

players = []
counter_pl = 0
user_pl = input("Enter y if you want to play: ")
if user_pl == 'y':
    players.append(User(names[0]))
    counter_pl = 1

adv_ai = inputNumber("Enter the number of Advanced AIs: ")
while not (0 <= adv_ai <= (6-counter_pl)):
    adv_ai = inputNumber("Enter a number which leaves the total players below 6: ")

for x in range(int(adv_ai)):
    players.append(AdvancedAI(names[x+counter_pl]))
print('')
simple_ai = inputNumber("Enter the number of Simple AIs: ")
while not (0 <= simple_ai <= (6-counter_pl - adv_ai)):
    simple_ai = inputNumber("Enter a number which leaves the total players below 6: ")

for x in range(int(simple_ai)):
    players.append(Player(names[x+adv_ai+counter_pl]))
    random.shuffle(players[x+adv_ai].weapons)
    random.shuffle(players[x+adv_ai].rooms)
    random.shuffle(players[x+adv_ai].suspects)
print('')
random_ai = inputNumber("Enter the number of Random AIs: ")
if counter_pl + adv_ai + simple_ai < 3:
    lower_lim = 3-(counter_pl + adv_ai + simple_ai)
else:
    lower_lim = 0
while not (lower_lim <= random_ai <= (6-counter_pl - adv_ai - simple_ai)):
    random_ai = inputNumber("Enter a number which makes the total players between 3 and 6: ")

for x in range(int(random_ai)):
    players.append(RandomAI(names[x+adv_ai+simple_ai + counter_pl]))

print('')

num_players = random_ai+adv_ai+simple_ai
if user_pl == 'y':
    num_players += 1

for pl in players:
    random.shuffle(pl.weapons)
    random.shuffle(pl.rooms)
    random.shuffle(pl.suspects)

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
conservatory = Room("Conservatory")
billiard_room = Room("Billiard Room")
library = Room("Library")
study = Room("Study")
hall = Room("Hall")
lounge = Room("Lounge")
cellar = Room("Cellar")

kitchen.add_neighbour(ballroom)
ballroom.add_neighbour(conservatory)
conservatory.add_neighbour(billiard_room)
billiard_room.add_neighbour(library)
library.add_neighbour(study)
study.add_neighbour(hall)
hall.add_neighbour(lounge)
lounge.add_neighbour(cellar)
cellar.add_neighbour(kitchen)
kitchen.add_neighbour(study)
conservatory.add_neighbour(lounge)

room_list = [kitchen, ballroom, conservatory, billiard_room, library, study, hall, lounge, cellar]



for x in players:
    for y in players:
        if players.index(y) > players.index(x):
            x.right_n.append(y)
    for z in players:
        if players.index(z) < players.index(x):
            x.right_n.append(z)

cards=[]

x=random.choice(suspects)
cards.append(x)
all_cards.remove(x)
x = random.choice(weapons)
cards.append(x)
all_cards.remove(x)
x = random.choice(rooms)
cards.append(x)
all_cards.remove(x)

player_order=0
for x in range(len(all_cards)):
    card = random.choice(all_cards)
    players[player_order % int(num_players)].cards.append(card)
    all_cards.remove(card)
    player_order += 1

for p in players:
    for card in p.cards:
        if card in p.information:
            p.information[card]=1

for p in players:
    p.set_room(random.choice(room_list))

game=True
turn=0
print("")
print(" WELCOME TO CLUEDO        ")
print("")
if user_pl != 'y':
    print("The correct cards are ", cards)
    for x in players:
        print(x.name, "has", x.cards)
else:
    for x in players:
        if isinstance(x, User):
            print("You have", x.cards)

print('')
if user_pl != 'y':
    while game:
        print('turn '+ str(turn+1))
        if players[turn % num_players].status == True:
            room1=players[turn % num_players].room_location.get_name()
            players[turn % num_players].change_room()
            if room1 == players[turn % num_players].room_location.get_name():
                print(players[turn % num_players].name, 'stayed in', room1)
            else:
                print(players[turn % num_players].name, " changed room from", room1, "to", players[turn % num_players].room_location.get_name())
            gue = players[turn % num_players].make_guess()
            print(players[turn % num_players].name, " makes a guess for ", gue)
            if gue == cards:
                print(players[turn % num_players].name, ' wins')
                game = False
                break
            answer=True

            for x in players[turn % num_players].right_n:
                answ = x.ans_guess(gue)
                if answ == False:
                    print(x.name, ' doesnt have a card to show')
                    for p in players:
                        if isinstance(p, AdvancedAI) and x != p:
                            p.advanced_info3(gue, x)

                else:
                    print(x.name, ' shows ', answ)
                    # if isinstance(x, AdvancedAI):
                    #     x.advanced_info4(answ, players[turn % num_players])
                    if isinstance(players[turn % num_players], AdvancedAI):
                        players[turn % num_players].info_update(answ, x)
                    else:
                        players[turn % num_players].info_update(answ)
                    for p in players:
                        if isinstance(p, AdvancedAI) and x != p:
                            p.advanced_info(gue, x, players[turn % num_players])
                    answer=False
                    break
            if answer == True:
                for x in gue:
                    if x in cards:
                        answer = False
                        if players[turn % num_players].information[x] != 2:
                            print(players[turn % num_players].name, " sees ", x, " from the deck")
                            for pl in players:
                                if isinstance(pl, AdvancedAI):
                                    pl.advanced_info2(gue)
                            players[turn % num_players].info_update2(x)

            if isinstance(players[turn % num_players], AdvancedAI):
                acc = players[turn % num_players].make_accusation()
                if acc:
                    if len(acc) == 3:
                        print(players[turn % num_players].name, " makes an accusation for ", acc)
                        if acc == cards:
                            print(players[turn % num_players].name, ' wins')
                            game = False
                            break
                        else:
                            players[turn % num_players].status = False
                            print(players[turn % num_players].name, ' loses')

            if isinstance(players[turn % num_players], User):
                choice = input("Do you want to make an accusation: y/n ")
                if choice == 'y':
                    acc = players[turn % num_players].make_accusation()
                    print(players[turn % num_players].name, " makes an accusation for ", acc)
                    if acc == cards:
                        print(players[turn % num_players].name, ' wins')
                        game = False
                        break
                    else:
                        players[turn % num_players].status = False
                        print(players[turn % num_players].name, ' loses')
        else:
            print(players[turn % num_players].name, ' already lost')
        if isinstance(players[turn % num_players], AdvancedAI):
            if players[turn % num_players].prints == 1:
                print(players[turn % num_players].information)
        turn += 1
        print('')
else:
    while game:
        print('turn ' + str(turn + 1))
        if players[turn % num_players].status == True:
            room1 = players[turn % num_players].room_location.get_name()
            players[turn % num_players].change_room()
            if room1 == players[turn % num_players].room_location.get_name():
                print(players[turn % num_players].name, 'stayed in', room1)
            else:
                print(players[turn % num_players].name, " changed room from", room1, "to",
                      players[turn % num_players].room_location.get_name())
            gue = players[turn % num_players].make_guess()
            print(players[turn % num_players].name, " makes a guess for ", gue)
            if gue == cards:
                print(players[turn % num_players].name, ' wins')
                game = False
                break
            answer = True

            for x in players[turn % num_players].right_n:
                answ = x.ans_guess(gue)
                if answ == False:
                    print(x.name, ' doesnt have a card to show')
                    for p in players:
                        if isinstance(p, AdvancedAI) and x != p:
                            p.advanced_info3(gue, x)

                else:
                    if isinstance(players[turn % num_players], User) or isinstance(x, User):
                        print(x.name, 'shows', answ)
                    else:
                        print(x.name, ' shows a card')
                    # if isinstance(x, AdvancedAI):
                    #     x.advanced_info4(answ, players[turn % num_players])
                    if isinstance(players[turn % num_players], AdvancedAI):
                        players[turn % num_players].info_update(answ, x)
                    else:
                        players[turn % num_players].info_update(answ)
                    for p in players:
                        if isinstance(p, AdvancedAI) and x != p:
                            p.advanced_info(gue, x, players[turn % num_players])
                    answer = False
                    break
            if answer == True:
                for x in gue:
                    if x in cards:
                        answer = False
                        if players[turn % num_players].information[x] != 2:
                            print(players[turn % num_players].name, " sees a card from the deck")
                            for pl in players:
                                if isinstance(pl, AdvancedAI):
                                    pl.advanced_info2(gue)
                            players[turn % num_players].info_update2(x)

            if isinstance(players[turn % num_players], AdvancedAI):
                acc = players[turn % num_players].make_accusation()
                if acc:
                    if len(acc) == 3:
                        print(players[turn % num_players].name, " makes an accusation for ", acc)
                        if acc == cards:
                            print(players[turn % num_players].name, ' wins')
                            game = False
                            break
                        else:
                            players[turn % num_players].status = False
                            print(players[turn % num_players].name, ' loses')

            if isinstance(players[turn % num_players], User):
                choice = input("Do you want to change the information of a card: y/n ")
                if choice == 'y':
                    players[turn % num_players].change_info()
                    while choice == 'y':
                        choice = input("Do you want to do it again: y/n ")
                        if choice == 'y':
                            players[turn % num_players].change_info()

            if isinstance(players[turn % num_players], User):
                choice = input("Do you want to make an accusation: y/n ")
                if choice == 'y':
                    acc = players[turn % num_players].make_accusation()
                    print(players[turn % num_players].name, " makes an accusation for ", acc)
                    if acc == cards:
                        print(players[turn % num_players].name, ' wins')
                        game = False
                        break
                    else:
                        players[turn % num_players].status = False
                        print(players[turn % num_players].name, ' loses')
        else:
            print(players[turn % num_players].name, ' already lost')
        if isinstance(players[turn % num_players], AdvancedAI):
            if players[turn % num_players].prints == 1:
                print(players[turn % num_players].information)
        turn += 1
        time.sleep(3)
        print('')
