"""
BLACKJACK CARD GAME
"""
from random import shuffle

#properties of cards
colors=("Spades","Hearts","Clubs","Diamonds")
figures=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
cards_and_values={'Two':2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,\
"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}


class Card():
    """
    CLASS CARD
    """
    def __init__(self,color_card,figure):
        self.color_card=color_card
        self.figure=figure
        #value of card,the higher card has higher the value
        self.value = cards_and_values[figure]

    def __str__(self):
        return f"{self.figure} {self.color_card}"

    def __repr__(self):
        """
        method showing name of object in the list
        """
        return self.__str__()

class Deck():
    """
    CLASS DECK
    """
    def __init__(self):
        self.all_of_cards =[]

    #how many cards are in the deck
    def __len__(self):
        return len(self.all_of_cards)

    def create_deck_cards(self):
        """
        create deck
        """
        for card_color in colors :
            for card_figure in figures:
                new_card=Card(card_color,card_figure)
                self.all_of_cards.append(new_card)

    def shuffle(self):
        """
        shuffle deck
        """
        shuffle(self.all_of_cards)

    def remove_cards(self):
        """
        remove card from the top of the deck
        """
        self.all_of_cards.pop(0)

class Player():
    """
    CLASS DECK
    """
    def __init__(self):
        self.player_cards=[]
        self.value_of_player_cards=0

    def __len__(self):
        """
        how many cards are in the player's hand
        """
        return len(self.player_cards)

    def add_card(self,card,deck):
        """
        deal card from the deck and remove this card from top in the deck
        """
        self.player_cards.append(card)
        self.value_of_player_cards+=card.value
        deck.remove_cards()

    def hit_or_stay(self,card,deck):
        """
        method HIT or STAY, if player selects HIT, he will draw a card from the deck
        if he selects STAY, he will stay with these cards that we have in hand
        """
        print("Player Cards: ")
        print(self.player_cards)
        result_hit_or_stay=""
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
                result_hit_or_stay=True
            elif choice=='STAY':
                #if we select STAY, we will stay with these cards that we have got in hand
                print("")
                print('You stay with those cards :')
                print(self.player_cards)
                print("")
                loop=False
                result_hit_or_stay=False
            else:
                print("Wrong text.Try again")
        return result_hit_or_stay

    def final_checking_cards(self):
        """
        check has player got aces in hand
        if player has got ace/s and value of cards in hand exceed 21
        reduce value of player's cards by 10
        """
        cards_list=[card.figure for card in self.player_cards if card.figure=="Ace"]
        ace_count=0
        while ace_count<=cards_list.count("Ace") and self.value_of_player_cards>21:
            self.value_of_player_cards-=10
            ace_count+=1

class Dealer():
    """
    CLASS DEALER
    """
    def __init__(self):
        self.dealer_cards=[]
        self.value_of_dealer_cards=0

    def add_card(self,card,deck):
        """
        deal card to player
        """
        self.dealer_cards.append(card)
        self.case_of_ace_in_dealer_cards()
        self.value_of_dealer_cards+=card.value
        deck.remove_cards()

    def case_of_ace_in_dealer_cards(self):
        """
        check has dealer got aces in hand
        if he has got more aces than one and we reduce value of dealer cards by 10
        """
        cards_list=[x.figure for x in self.dealer_cards]
        how_many_aces_in_dealer_cards=cards_list.count("Ace")
        if how_many_aces_in_dealer_cards>1:
            self.value_of_dealer_cards-=(how_many_aces_in_dealer_cards-1)*10

    def checking_cards(self,card,deck):
        """
        check Do value of dealer's cards exceed 16
        if value 0f dealer's cards is lower or equal to 16, dealer draw a card
        """
        while self.value_of_dealer_cards <= 16:
            print("Dealer hit")
            print("")
            self.add_card(card,deck)

class GameLogic():
    """
    CLASS GAME LOGIC
    """
    @staticmethod
    def who_win(player,dealer):
        """
        check who win
        if value of player's or dealer's cards exceed 21, they will lose
        if value of player's cards is closer 21 than value of dealer's cards, player win
        and exactly the same in backward
        if value of player's cards is equal to value of dealer's cards is draw
        """
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

    @staticmethod
    def play_again():
        """
        check does player wants to play again
        """
        play_or_not_play=""
        result_play_or_not_play=""
        while play_or_not_play not in ["Y","N"]:
            play_or_not_play=input("Do you want play again? Y or N : ")
            if play_or_not_play=="Y":
                result_play_or_not_play=True
            elif play_or_not_play=='N':
                print("Game over")
                result_play_or_not_play=False
            else:
                print("You enter unfamiliar character")
        return result_play_or_not_play

def main():
    """
    main function
    """
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
        hand=0
        #loop in which we deal cards
        while hand<2:
            print(f"{hand+1} hand")
            player.add_card(my_deck.all_of_cards[0],my_deck)
            print("Player Cards: ")
            print(player.player_cards)
            dealer.add_card(my_deck.all_of_cards[0],my_deck)
            #player see only first dealer's card but after the second hand
            if hand==1:
                print("")
                print("Dealer card:")
                print(dealer.dealer_cards[0])
                print('')
            hand+=1
        is_hit_or_stay=True
        #loop in which there is method HIT or STAY,if player selects HIT
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

main()
