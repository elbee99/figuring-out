import random 

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
    def show(self):
        print(self.rank + ' of ' + self.suit)
        
        
class Deck():
    
    cards = []
    
    def __init__(self):
        self.construct_deck()
        self.playing_deck = []
        self.discard_deck = []
        
    def construct_deck(self):
        for suit in ['Hearts','Diamonds','Clubs','Spades']:
            for rank in ['Ace', '2', '3','4','5','6','7','8','9','10','Jack','Queen','King']:
                self.cards.append(Card(suit,rank))
                
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def show(self):
        for card in self.cards:
            card.show()
            
    def draw(self):
        return self.cards.pop()
            
    
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
        
    def draw(self,deck):
        self.hand.append(deck.draw())
    
    def show_hand(self):
        for card in self.hand:
            card.show()
        
    def play(self,play_pile):
        play_pile.append(self.hand.pop(0))
        
bob = Player('Bob')
lar = Player('Larry')
deck = Deck()
deck.shuffle()
while len(deck.cards) > 0:
    bob.draw(deck)
    lar.draw(deck)
    deck.show()
            
playing_pile = []
while len(lar.hand) > 0 and len(bob.hand) > 0:
    bob.play(playing_pile)
    lar.play(playing_pile)
    print('Pile size:', len(playing_pile),
          'Top three cards are:',str(playing_pile[-1]),str(playing_pile[-2]),
          str(playing_pile[-1]))
    if playing_pile[-1].rank == playing_pile[-2].rank:
        lucky = random.randint(1,2)
        if lucky == 1:
            lar.hand += playing_pile
            print('Snap! Larry took a pile of',len(playing_pile),'cards')
            playing_pile = []
        else:
            bob.hand += playing_pile
            print('Snap! Bob took a pile of',len(playing_pile),'cards')
            playing_pile = []

if len(lar.hand) > len(bob.hand):
    print('Larry is the winner!')
elif len(lar.hand) == len(bob.hand):
    print('Wow, a tie! We all won')
else:
    print('Bob is the winner!')
    
    
