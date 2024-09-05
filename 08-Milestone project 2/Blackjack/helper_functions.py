from player import Player
from deck import *

def show_hand(player):
    print(f"{player.name}'s hand:")
    for card in player.hand:
        print(card)
    print(f"Value of {player.name}'s hand is {player.value}")
    

def check_player_busts(player):
    return player.value > 21

def hit_or_stand():
    choice = ''
    while choice[0] not in ['H','S']:
        try:
            choice = input('Hit or Stand?(H/S) ').upper()
        except:
            print('Error occured try again!')
    return choice

def hit(deck,player):
    player.add_card(deck.deal_one())

def check_play_again():
    choice = ''
    while choice not in ['Y','N']:
        try:
            choice = input('Play again?(Y/N) ').upper()
        except:
            print('Error occured try again!')
    return choice == 'Y'