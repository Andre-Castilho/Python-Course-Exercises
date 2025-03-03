import random
import os
import copy
import art

deck_of_cards = {
    "Hearts":   ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "Jack", "King"],
    "Diamonds": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "Jack", "King"],
    "Clubs":    ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "Jack", "King"],
    "Spades":   ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "Jack", "King"]
}

current_deck = copy.deepcopy(deck_of_cards)
hidden_card = None

def deal_card():
    suit = random.choice(list(current_deck.keys()))
    if len(current_deck[suit]) == 0:
        del current_deck[suit]
        suit = random.choice(list(current_deck.keys()))
    card = random.choice(current_deck[suit])
    current_deck[suit].remove(card)
    return suit, card

def calculate_score(hand):
    cards_score = list(range(len(hand)))
    for i in range(len(hand)):
        if hand[i] == "Queen" or hand[i] == "Jack" or hand[i] == "King":
            cards_score[i] = 10
        elif hand[i] == "Ace":
            cards_score[i] = 11
        else:
            cards_score[i] = hand[i]

    if sum(cards_score) == 21 and len(cards_score) == 2:
        return 0
    
    if 11 in cards_score and sum(cards_score) > 21:
        cards_score.remove(11)
        cards_score.append(1)

    return sum(cards_score)

def deal_to_player():
    drawn_card = deal_card()
    player_hand.append(drawn_card[1])
    print(f"You drew {drawn_card[1]} of {drawn_card[0]}")

def deal_to_dealer():
    drawn_card = deal_card()
    dealer_hand.append(drawn_card[1])
    print(f"Dealer drew {drawn_card[1]} of {drawn_card[0]}\n")
    

def play_blackjack():
    
    for _ in range(2): 
        deal_to_player()

    hidden_card = deal_card()
    dealer_hand.append(hidden_card[1])
    print("\nDealer drew a hidden card")
    deal_to_dealer()
    

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    while(player_score != 0 and player_score < 21):
        print(f"\nYour current score is: {player_score}")
        print(f"Dealer's visible card is: {dealer_hand[1]}")
        action = input("Do you want to hit or stand? ")
        if action == "hit":
            deal_to_player()
            player_score = calculate_score(player_hand)
        elif action == "stand":
            break

    if player_score == 21:
        print("\n**************************************** You got a blackjack! ****************************************\n")
    elif player_score > 21:
        print("\n**************************************** You busted! ****************************************\n")
        return

    
    print(f"\nDealer's hidden card was {hidden_card[1]} of {hidden_card[0]}")

    while(dealer_score < 17):
        deal_to_dealer()
        dealer_score = calculate_score(dealer_hand)
    
    print(f"\n**************************************** Dealer's score is: {dealer_score} ****************************************")
    print(f"**************************************** Your score is: {player_score} ****************************************\n")

    if dealer_score == player_score:
        print("**************************************** It's a tie! ****************************************")
    elif dealer_score > 21:
        print("**************************************** Dealer busted! You win! ****************************************")
    elif dealer_score > player_score:
        print("**************************************** You lose! ****************************************")
    else:
        print("**************************************** You win! ****************************************")


art.casino_greeting()

times_played = 0
while(keep_playing := input("\n\nDo you want to play blackjack? (yes/no) ")) == "yes":
    os.system('cls||clear')

    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    if times_played == 8:
        print("played 5 times, reshuffling the deck")
        current_deck = copy.deepcopy(deck_of_cards)
        times_played = 0
    
    play_blackjack()
    
    times_played += 1
    
art.casino_goodbye()