# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals


def new_game():
    global DECK, exposed, state, turn

    # STATE
    DECK = []
    exposed = []
    state = 0
    card1 = 0
    card2 = 0
    turn = 0
    label.set_text("Turns = " + str(turn / 2))
    # CREATES DECK RANGE 0-7 DOUBLED
    for i in range(2):
        for i in range(0, 8):
            DECK.append(i)
            exposed.append(False)
    random.shuffle(DECK)

# define event handlers


def mouseclick(pos):
    global exposed, state, card1, card2, turn

    # add game state logic here
    # Changes False to true if clicked on
    if state == 0:
        # if state = 0 expose selected card
        state = 1
        card1 = pos[0]/50
        exposed[pos[0]/50] = True
    elif state == 1:
        # if state = 1 expose second selected card
        if exposed[pos[0]/50] == False:
            state = 2
            card2 = pos[0]/50
            exposed[pos[0]/50] = True
            turn += 1
    elif state == 2:
        if exposed[pos[0]/50] == False:
            # if state = 2 && exposed cards match reset state to 1
            if DECK[card1] == DECK[card2]:
                state = 1
                card1 = pos[0]/50
                exposed[pos[0]/50] = True
            elif DECK[card1] != DECK[card2]:
                # else if state = 2 && exposed cards do not match cover them reset state to 1
                state = 1
                exposed[card1] = False
                exposed[card2] = False
                card1 = pos[0]/50
                exposed[pos[0]/50] = True
    label.set_text("Turns = " + str(turn))


def draw(canvas):
    global turn
    # SETS CARD SIZES
    CARD_WIDTH = 50
    CARD_HEIGHT = 100

    # DRAWS CARDS ON FRAME
    for card in range(len(DECK)):
        card_pos = CARD_WIDTH * card

        # If card exposed = True draw Card else Draw square
        if exposed[card]:
            # Draw card
            canvas.draw_text(
                str(DECK[card]), (card_pos + 10, CARD_HEIGHT * .7), 50, "WHITE")
        else:
            # Draw green square
            canvas.draw_polygon([(card_pos, 0), (card_pos, CARD_HEIGHT), (
                card_pos + CARD_WIDTH, CARD_HEIGHT), (card_pos + CARD_WIDTH, 0)], 3, "Black", "green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
