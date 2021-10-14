from random import shuffle
import os
#properties of cards
color=("Spades","Hearts","Clubs","Diamonds")
figures=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
cards_and_values={'Two':2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,\
"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

class Card():
    def __init__(self,color_card,figure):
        self.color_card=color_card
        self.figure=figure
        #value of card,the higher card has higher the value
        self.value = cards_and_values[figure]

    def __str__(self):
        return f"{self.figure} {self.color_card}"

    #method showing name of object in the list
    def __repr__(self):
        return self.__str__()

class Deck():
    def __init__(self):
        self.all_of_cards =[]

    #how many cards are in the deck
    def __len__(self):
        return len(self.all_of_cards)

    #create deck
    def create_deck_cards(self):
        for x in color :
            for y in figures:
                new_card=Card(x,y)
                self.all_of_cards.append(new_card)

    #shuffle deck
    def shuffle(self):
        shuffle(self.all_of_cards)

    #remove card from the top of the deck
    def remove_cards(self):
        self.all_of_cards.pop(0)

class Player():
    def __init__(self):
        self.player_cards=[]
        self.value_of_player_cards=0

    #how many cards are in the player's hand
    def __len__(self):
        return len(self.player_cards)

    #deal card to player
    #and removce card from the deck
    def add_card(self,card,deck):
        self.player_cards.append(card)    
        self.value_of_player_cards+=card.value
        deck.remove_cards()

    #method HIT or STAY, if player selects HIT, he will draw a card from the deck
    #if he selects STAY, he will stay with these cards that we have in hand
    def hit_or_stay(self,card,deck):
        print("Player Cards: ")
        print(self.player_cards)
        loop=True
        while loop:
            #player select from 2 options(HIT OR STAY)
            choice=input("Do you hit or stay? Enter (HIT OR STAY) : ")
            print("")
            if choice=="HIT":
                print('You added new card to your deck :')
                #if we select HIT, we will draw a card from the deck
                self.add_card(card,deck)
                loop=False
                return True
            elif choice=='STAY':
                #if we select STAY, we will stay with these cards that we have got in hand
                print("")
                print('You stay with those cards :')
                print(self.player_cards)
                print("")
                loop=False
                return False
            else:
                print("Wrong text.Try again")

    #check has player got aces in hand
    #if player has got ace/s and value of cards in hand exceed 21
    #reduce value of player's cards by 10
    def final_checking_cards(self):
        cards_list=[x.figure for x in self.player_cards if x.figure=="Ace"]
        x=0
        while x<=cards_list.count("Ace") and self.value_of_player_cards>21:
            self.value_of_player_cards-=10
            x+=1

class Dealer():
    def __init__(self):
        self.dealer_cards=[]
        self.value_of_dealer_cards=0

    #deal card to player
    def add_card(self,card,deck):
        self.dealer_cards.append(card)
        self.case_of_ace_in_dealer_cards()
        self.value_of_dealer_cards+=card.value
        deck.remove_cards()

    #check has dealer got aces in hand
    #if he has got more aces than one and we reduce value of dealer cards by 10
    def case_of_ace_in_dealer_cards(self):
        cards_list=[x.figure for x in self.dealer_cards]
        how_many_aces_in_dealer_cards=cards_list.count("Ace")
        if how_many_aces_in_dealer_cards>1:
            self.value_of_dealer_cards-=(how_many_aces_in_dealer_cards-1)*10

    #check Do value of dealer's cards exceed 16
    #if value 0f dealer's cards is lower or equal to 16, dealer draw a card
    def checking_cards(self,card,deck):
        while self.value_of_dealer_cards <= 16:
            print("Dealer hit")
            print("")
            self.add_card(card,deck)

class GameLogic():

    #check who win
    #if value of player's or dealer's cards exceed 21, they will lose
    #if value of player's cards is closer 21 than value of dealer's cards, player win
    #and exactly the same in backward
    #if value of player's cards is equal to value of dealer's cards is draw
    def who_win(player,dealer):
        if player.value_of_player_cards > 21:
            print("Buzz. Value of your cards exceed 21. Dealer win")
        elif dealer.value_of_dealer_cards > 21:
            print("Buzz. Value of dealer cards exceed 21. Player win")
        else:
            if  player.value_of_player_cards > dealer.value_of_dealer_cards:
                print("Player win")
            elif player.value_of_player_cards < dealer.value_of_dealer_cards:
                print("Player lose. Dealer win")
            else:
                print("Draw")

    #check does player wants to play again
    def play_again():
        play_or_not_play=""
        while play_or_not_play not in ["Y","N"]:
            play_or_not_play=input("Do you want play again? Y or N : ")
            if play_or_not_play=="Y":
                return True
            elif play_or_not_play=='N':
                print("Game over")
                return False
            else:
                print("You enter unfamiliar character")

def main():
    game_on=True
    while game_on:
        my_deck = Deck()
        #create deck of cards
        my_deck.create_deck_cards()
        #shuffle deck
        my_deck.shuffle()
        #create player and dealer
        player = Player()
        dealer = Dealer()
        x=0
        #loop in which we deal cards
        while x<2:
            print(f"{x+1} hand")
            player.add_card(my_deck.all_of_cards[0],my_deck)
            print("Player Cards: ")
            print(player.player_cards)
            dealer.add_card(my_deck.all_of_cards[0],my_deck)
            #player see only first dealer's card but after the second hand
            if x==1:
                print("")
                print("Dealer card:")
                print(dealer.dealer_cards[0])
                print('')
            x+=1
        is_hit_or_stay=True
        #loop in which there is method HIT or STAY,if player selects HIT, 
        #he will draw a card from the deck
        #if he selects STAY,he will stay with these cards that we have in hand
        while is_hit_or_stay:
            is_hit_or_stay=player.hit_or_stay(my_deck.all_of_cards[0],my_deck)
        #check Do value of dealer's cards exceed 16
        #if value 0f dealer's cards is lower or equal to 16, dealer draw a card
        dealer.checking_cards(my_deck.all_of_cards[0],my_deck)
        print("Dealer cards: ")
        print(dealer.dealer_cards)
        #check has player got aces in hand
        player.final_checking_cards()
        print("")
        #Game Logic check who win
        GameLogic.who_win(player,dealer)
        print("")
        #Game Logic check Does player want to play again?
        game_on=GameLogic.play_again()

#main()
old_name = r"C:\Users\Bartlomiej Lepa\Desktop\Projects\BlackJackGame\BlackJackGame.py"
new_name = r"C:\Users\Bartlomiej Lepa\Desktop\Projects\BlackJackGame\black_jack_game.py"

# Renaming the file
os.rename(old_name, new_name)