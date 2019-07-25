# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    # canvas and beginning position
    def draw(self, canvas, pos):
        # finds card in image to be drawn
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # draws that specific card
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        ans = ""
        for card in range(len(self.hand)):
            ans += " " + str(self.hand[card])
        return "Hand contains " + ans

    def add_card(self, card):

        self.hand.append(card)

    def get_value(self):

        hand_value = 0
        ace = 0
        
        for card in self.hand:
            
            #adds value of every card (1 for aces)
            hand_value += VALUES[card.rank]
            
            #if card is A
            if card.rank == "A":
                
                #increment ace
                ace +=1
                    
        #decrement ace, increment hand_value
        while ace > 0 and (hand_value + 10) <= 21:
            ace -= 1
            hand_value += 10
                    
        return hand_value
    
    def draw(self, canvas, pos):
        for card in range(len(self.hand)):
            self.hand[card].draw(canvas, ((pos[0] * card) + 25, pos[1]))

# define deck class 
class Deck:
    def __init__(self):
        self.suits = SUITS
        self.ranks = RANKS
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(suit + rank)
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        suit = card[0]
        rank = card[1]
        return Card(suit, rank)
    
    def __str__(self):
        ans = ""
        for card in range(len(self.deck)):
            ans += " " + str(self.deck[card])
        return "Deck contains " + ans

#define event handlers for buttons
def deal():
    global dealer, player, new_deck, score, outcome
    global outcome, in_play
    
    if in_play:
        score -= 1
        in_play = False
        outcome = "Forfeit hand, Player loses." 
        return
    
    # Create new deck and shuffle it.
    outcome = ""
    new_deck = Deck()
    new_deck.shuffle()
    
    # Create Dealers hand and draw two cards
    dealer = Hand()
    for i in range(2):
        dealer.add_card(new_deck.deal_card())

    # Create Plyers hand and draw two cards
    player = Hand()
    for i in range(2):
        player.add_card(new_deck.deal_card())
    in_play = True

def hit():
    global score, in_play, outcome
    
    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(new_deck.deal_card())
        
    # if busted, assign a message to outcome, update in_play and score
    if in_play and player.get_value() > 21:
        outcome = "Player busts. Dealer wins."
        in_play = False
        score -= 1
        
def stand():
    global outcome, in_play, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while in_play and dealer.get_value() <= 17:
        dealer.add_card(new_deck.deal_card())

        if dealer.get_value() > 21:
            outcome = "Dealer busts. Player Wins!"
            in_play = False
            score += 1
        
    # assign a message to outcome, update in_play and score
    if in_play and player.get_value() > dealer.get_value():
        outcome = "Player Wins!"
        in_play = False
        score += 1
        
    if in_play and player.get_value() <= dealer.get_value():
        outcome = "Dealer Wins"
        in_play = False
        score -= 1
        
# draw handler    
def draw(canvas):
    
    # Draw hands
    if in_play == False:
        dealer.draw(canvas, [75, 250])
        player.draw(canvas, [75, 450])
    else:
        dealer.draw(canvas, [75, 250])
        canvas.draw_image(card_back, CARD_BACK_CENTER , CARD_BACK_SIZE, [25 + CARD_CENTER[0], 250 + CARD_CENTER[1]], CARD_BACK_SIZE)
        player.draw(canvas, [75, 450])
        
    # Draw static text
    canvas.draw_text("Blackjack", [100, 100], 48, "White")
    canvas.draw_text("Dealer", [50, 225], 24, "Black")
    canvas.draw_text("Player", [50, 425], 24, "Black")
    fin_score = canvas.draw_text("Score " + str(score), [400, 100], 24, "Black")
    
    # Draw game play text
    if outcome == "":
        canvas.draw_text("Hit or stand?", [225, 425], 24, "White")
    else:
        canvas.draw_text("New Deal?", [225, 425], 24, "White")
        canvas.draw_text(outcome, [225, 225], 24, "White")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand ", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric