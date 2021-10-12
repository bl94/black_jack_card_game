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

class Player():
    def __init__(self,name):
        self.name=name
        self.player_cards=[]
        self.value_of_player_cards=0
    
    def __str__(self):
        return f'{self.player_cards.__str__}'
    
    def __len__(self):
        return len(self.player_cards)
    
    def add_card(self,card):
        if type(card)== type([]):
            self.player_cards.extend(card)
            self.value_of_player_cards=self.sum_value_of_cards()
        else:
            self.player_cards.append(card)
            self.value_of_player_cards=self.sum_value_of_cards()
    
    def sum_value_of_cards(self):
        sum_up = 0
        for x in range(0,len(self.player_cards),1):
            sum_up=self.player_cards[x].value
        return sum_up

    def checking_cards(self,card):
        if type(card)== type([]):
            self.player_cards.extend(card)
            self.value_of_player_cards=self.sum_value_of_cards()
        else:
            self.player_cards.append(card)
            self.value_of_player_cards=self.sum_value_of_cards()

    def hit_or_stay(self,card):
        print(self.player_cards)
        choice=input("Do you hit or stay ?").upper
        loop =True
        while loop:
            if choice=="HIT":
                self.add_card(card)
                self.sum_value_of_cards()
                loop=False
                return True
            elif choice=='STAY':
                self.sum_value_of_cards()
                loop=False
                return False
            else:
                print("Wrong text.Try again")

class Dealer():
    def __init__(self):
        self.player_cards=[]
        self.value_of_dealer_cards=0
    
    def add_card(self,card):
        if type(card)== type([]):
            self.player_cards.extend(card)
            self.value_of_player_cards=self.sum_value_of_cards()
        else:
            self.player_cards.append(card)
            self.value_of_player_cards=self.sum_value_of_cards()
    
    def sum_value_of_cards(self):
        sum_up = 0
        for x in range(0,len(self.player_cards),1):
            sum_up=self.player_cards[x].value
        return sum_up

    def checking_cards(self,card):
        if self.value_of_dealer_cards <=16:
            print("Dealer hit")
            self.add_card(card)
            
def main():
    my_deck = Deck()
    my_deck.create_deck_cards()
    my_deck.shuffle()
    player = Player(input('Input your name'))
    player.add_card(my_deck.all_of_cards[:2])
    player

main()
