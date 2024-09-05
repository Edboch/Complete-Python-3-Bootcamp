
from player import Player
from deck import *
from helper_functions import *

# Game setup
dealer = Player('dealer',0)
player = Player('Ed',1000)
deck = Deck()
deck.shuffle()

game_on = True
while game_on:
    # Game Start
    print(player)
    if player.balance == 0:
        print('You dont have enough money!')
        break
    
    bet = player.place_bet()
    
    # deal cards
    for i in range(2):
        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

    dealer.hand[0].hide_card()
    winner = False

    # Player Turn
    player_turn = True
    while player_turn:
        print(' ------------------------ ')
        show_hand(dealer)
        show_hand(player)
        # Check the players cards first
        if player.value == 21:
            player_turn = False
            break
        if player.aces > 0:
            player.adjust_aces()
        if check_player_busts(player):
            player_turn = False
            winner = True
            break
        else:
            # HIT OR STAND
            player_choice = hit_or_stand()
            if player_choice == 'H':
                hit(deck,player)
            else:
                player_turn = False
    
    dealer_turn = True
    dealer.hand[0].show_card()
    while dealer_turn and not winner :
        print(' ------------------------ ')
        show_hand(dealer)
        show_hand(player)
        if dealer.value == 21:
            dealer_turn = False
            break
        if dealer.aces > 0:
            dealer.adjust_aces()
        if check_player_busts(dealer):
            dealer_turn = False
            winner = True
            break
        elif dealer.value >= 17:
            dealer_turn = False
        else:
            hit(deck,dealer)
    
    # Check Winner
    print('=== RESULT ===')
    show_hand(dealer)
    show_hand(player)
    if player.value > 21 or (dealer.value > player.value and dealer.value <= 21):
        print(f'PLAYER HAS LOST! SCORE: {player.value}')
        print(f'YOU HAVE LOST ${bet}')
    elif player.value == dealer.value:
        print(f'IT WAS A TIE')
        player.add_balance(bet)
    else:
        print(f'PLAYER HAS WON! SCORE: {player.value}')
        print(f'YOU HAVE WON ${bet*2}')
        player.add_balance(bet*2)

    play_again = check_play_again()
    if not play_again:
        game_on = False
    else:
        player.reset()
        dealer.reset()
    
            

    

    



# turn start
# check winner if any 21

# player starts
# while loop, check if bust first then show options
# simplicity: Hit or Stay options
# case: hits, check if he is bust if not, show hit or stay options, end game if bust
# case: stay, moves onto dealer turn.

# dealer turn
# while loop 
# show facedown card
# check if bust, if bust then dealer lose
# then check if over 16, if over 16 stick, otherwise draw card and loop


# if either player or dealer bust, the loop breaks so this part is not reached
# if not then both players have cards to compare
# compare them to determine winner.

# optional ask if want to play again.

# additional note:
# ace = 11/1 
# king/queen/jack = 10
