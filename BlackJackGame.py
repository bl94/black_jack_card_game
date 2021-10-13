from random import shuffle

color=("Spades","Hearts","Clubs","Diamonds")
figures=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
cards_and_values={'Two':2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":[1,11]}

class Card():
    def __init__(self,color_card,figure):
        self.color_card=color_card
        self.figure=figure
        #value of card,the higher card has higher the value
        self.value = cards_and_values[figure]

    def __str__(self):
        return f"{self.figure} {self.color_card}"
    
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
    
    def remove_cards(self):
       self

class Player():
    def __init__(self,name):
        self.name=name
        self.player_cards=[]
        self.value_of_player_cards=0
    
    def __str__(self):
        return f'{self.player_cards.__str__}'
    
    def __len__(self):
        return len(self.player_cards)
    
    def add_card(self,card,deck):
        self.player_cards.append(card)
        self.sum_value_of_cards()
        deck.pop(0)
    
    def sum_value_of_cards(self):
        sum_up=0
        for x in range(0,len(self.player_cards),1):
           sum_up+=self.player_cards[x].value
        self.value_of_player_cards=sum_up

    def hit_or_stay(self,card,deck):
        print(self.player_cards)
        loop=True
        while loop:
            choice=input("Do you hit or stay? Enter(HIT OR STAY) : ")
            if choice=="HIT":
                print('You added new card to your deck :')
                self.add_card(card,deck)
                loop=False
                return True
            elif choice=='STAY':
                print('You stay with those cards :')
                print(self.player_cards)
                loop=False
                return False
            else:
                print("Wrong text.Try again")

class Dealer():
    def __init__(self):
        self.dealer_cards=[]
        self.value_of_dealer_cards=0
    
    def add_card(self,card,deck):
        self.dealer_cards.append(card)
        self.sum_value_of_cards()
        deck.pop(0)
    
    def sum_value_of_cards(self):
        sum_up=0
        for y in range(0,len(self.dealer_cards),1):
            sum_up+=self.dealer_cards[y].value
        self.value_of_dealer_cards=sum_up

    def checking_cards(self,card,deck):
        if self.value_of_dealer_cards <= 16:
            print("Dealer hit")
            self.add_card(card,deck)
          
def main():
    my_deck = Deck()
    my_deck.create_deck_cards()
    my_deck.shuffle()
    player = Player("Bartek")
    dealer = Dealer()
    x=0
    while x<2:
        print(f"{x+1} hand")
        player.add_card(my_deck.all_of_cards[0],my_deck.all_of_cards)
        print("Player Cards: ")
        print(player.player_cards)
        print('')
        dealer.add_card(my_deck.all_of_cards[0],my_deck.all_of_cards)
        print("Dealer card:")
        print(dealer.dealer_cards[0])
        print('')
        x+=1
    is_hit_or_stay=True
    while is_hit_or_stay:    
        is_hit_or_stay=player.hit_or_stay(my_deck.all_of_cards[0],my_deck.all_of_cards)
    print(dealer.value_of_dealer_cards)
    dealer.checking_cards(my_deck.all_of_cards[0],my_deck.all_of_cards)
    print(dealer.dealer_cards)
    print(dealer.value_of_dealer_cards)
main()
