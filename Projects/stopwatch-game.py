# template for "Stopwatch: The Game"
import simplegui

# define global variables

# set game state
time_laps = 0
game_state = True
times_stopped = 0
stopped_on_zero = 0
d = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D


def format(t):
    """formats seconds into minutes 0:00.0"""

    global d
    a = t // 600
    b = (t - a * 600) / 100
    c = (t - ((a * 600) + (b * 100))) / 10
    d = (t - ((a * 600) + (b * 100) + (c * 10)))
    return str(a) + ":" + str(b) + str(c) + "." + str(d)


def start():
    """starts timer"""
    global game_state
    game_state = False
    timer.start()


def stop():
    """stops timer, records stops and wins"""
    global game_state, times_stopped
    if game_state == False:
        game_state = True
        times_stopped += 1
        timer.stop()
        win_check()


def win_check():
    """ checks if stopped on zero """
    global stopped_on_zero
    if d == 0:
        stopped_on_zero += 1


def reset():
    """ resets game state"""

    global game_state, time_laps, times_stopped, stopped_on_zero, d

    game_state = True
    time_laps = 0
    times_stopped = 0
    stopped_on_zero = 0
    d = 0

# define event handler for timer with 0.1 sec interval


def timer_handler():
    """ increments timer variable """
    global time_laps
    time_laps += 1

# define draw handler


def draw_handler(canvas):
    canvas.draw_text(str(times_stopped) + "/" +
                     str(stopped_on_zero), [10, 10], 10, "white")
    canvas.draw_text(str(format(time_laps)), [30, 50], 20, 'white')


# create frame
frame = simplegui.create_frame("stopwatch game", 150, 150)
start_button = frame.add_button('Start', start, 50)
stop_button = frame.add_button('Stop', stop, 50)
reset_button = frame.add_button('Reset', reset, 50)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
