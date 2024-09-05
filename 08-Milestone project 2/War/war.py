from player import Player
from deck import Deck
from card import *

# Game Setup
p1 = Player('One')
p2 = Player('Two')

deck = Deck()
deck.shuffle()

for x in range(26):
    p1.add_cards(deck.deal_one())
    p2.add_cards(deck.deal_one())

game_on = True
round_counter = 0

while game_on:

    round_counter += 1
    print(f'Round {round_counter}')

    # Check winner
    if len(p1.all_cards) ==0 :
        print('Player One is out of cards! Player Two Wins!')
        game_on = False
        break

    if len(p2.all_cards) ==0 :
        print('Player Two is out of cards! Player One Wins!')
        game_on = False
        break
    
    # Start of the round
    p1_played_cards = []
    p1_played_cards.append(p1.remove_one())
    p2_played_cards = []
    p2_played_cards.append(p2.remove_one())

    at_war = True

    while at_war:

        if p1_played_cards[-1].value > p2_played_cards[-1].value:
            p1.add_cards(p1_played_cards)
            p1.add_cards(p2_played_cards)
            at_war = False
        elif p1_played_cards[-1].value < p2_played_cards[-1].value:
            p2.add_cards(p1_played_cards)
            p2.add_cards(p2_played_cards)
            at_war = False
            
        else:
            print('WAR!')
            if len(p1.all_cards) < 3:
                print('Player One is unable to declare war!')
                print('Player Two Wins!')
                game_on = False
                break
            elif len(p2.all_cards) < 3:
                print('Player Two is unable to declare war!')
                print('Player One Wins!')
                game_on = False
                break
            else:
                for i in range(3):
                    p1_played_cards.append(p1.remove_one())
                    p2_played_cards.append(p2.remove_one())
