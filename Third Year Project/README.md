Cluedo game

The zip file contains two separate files that can be run.

The file main.py is used to be able to play a single game be it either with or without a player. The first thing the code ask is whether you want to play yourself. If the answer is 'y' you will be added to the game and play with the different AIs, the number and type of AIs is also inputted, but the total number of users must be kept between 3 and 6.

The file main_testing.py is used to simulate a large number of games between an Advanced AI and Simple AIs. It takes as input the number of total games you want to run, the type of AIs the Advanced AI will be facing, the number of AIs playing and the position of the Advaned AI.


The AIs briefly:
1. Random - ask random queries until it finds cards in the envelope (done by asking about 1 or 2 cards it owns and other cards which happen to be in the envelope, but the chance of a random query being like this is still very low). Once it finds such it always asks for them. Better than a fully random player, but still not a great strategy.
2. Simple AI - always ask about cards it doesn't know the location of securing at least one new information per turn. It keeps asking about the same card if no one shows it which is a good way of finding cards in the envelope.
3. Advanced AI - uses numerous functions and data structures to keep track of information and learn the far more than 1 new information per rotation.

The user has an information card where the information of a certain object is 1 if he knows that it is in a player or 2 if he knows it is in the envelope. The thing he has to do during the game are changing his room, making and answering guesses, making accusations or changing the information he currently has with whichever number he wants to which could be used to create a strategy. (example: type 12 in the information card if the card is either in player 1 or 2)