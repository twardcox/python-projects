"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # create new array
    new_list = list(line)

    # move all zeros to end of new_list
    for num in range(len(new_list)-1, -1, -1):
        if new_list[num] == 0:
            new_list.pop(num)
            new_list.append(0)

    # decides if numbers need to be combined
    for num in range(len(new_list)-1):

        # numbers need to be combined
        if num < len(new_list)-1 and new_list[num] == new_list[num+1]:
            new_list.insert(num, new_list[num] * 2)
            new_list.pop(num+1)
            new_list.pop(num+1)
            new_list.append(0)

    return new_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._board = []
#        self.reset()

        self._init_tiles = {
            UP: [[0, x] for x in range(self._grid_width)],
            DOWN: [[self._grid_height - 1, x] for x in range(self._grid_width)],
            LEFT: [[x, 0] for x in range(self._grid_height)],
            RIGHT: [[x, self._grid_width - 1] for x in range(self._grid_height)],
        }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        self._board = [[0 for x in range(self._grid_width)]
                       for y in range(self._grid_height)]
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._board[0]) + "\n" + str(self._board[1]) + "\n" + str(self._board[2]) + "\n" + str(self._board[3]) + "\n\n"

    def get_grid_height(self):
        """
        Get the height of the board.
        """

        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        # ternary operator setting dimension variable
        dim = self.get_grid_width() if (direction == "LEFT" or direction ==
                                        "RIGHT") else self.get_grid_height()
        self.get_row(direction, dim)
        self.new_tile()

    def get_row(self, direction, dim):
        """
        creates a new list of values for merging
        """

        # itterates over the number of entries on init_tiles for the given direction
        for cell in self._init_tiles[direction]:

            # first pass over this cell location
            first_pass = True

            # when the while loop ends merges line into new line
            merged = self.set_new_line(cell, direction, dim, first_pass)
            first_pass = False
            # new_tile now contains the merged gird
            self.set_new_line(cell, direction, dim, first_pass, merged)

    def set_new_line(self, cell, direction, dim, first, merged=0):
        """
        handler funtion that retreives or replaces tiles on the board
        depending on direction input
        """

        test = list(cell)
        new_tiles = []

        # repeats while cell is within the dimensions of the grid
        # dimension is now a single number
        # while test[0] < dim[0] and test[0] > 0 and test[1] < dim[1] and test[1]> 0:
        for tile in range(dim):

            if first == True:

                # appends contents of tile to new_tiles for eventual merging
                new_tiles.append(self.get_tile(test[0], test[1]))
            else:
                self._board[test[0]][test[1]] = merged[tile]

                # uses direction dictionary to increment new cell locatin
            test[0] += OFFSETS[direction][0]
            test[1] += OFFSETS[direction][1]

        if first == True:
            new_tiles = merge(new_tiles)

        return new_tiles

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        count = 0
        tot_count = self.get_grid_width() * self.get_grid_height()

        while count < 2 and tot_count > 0:
            # my_list = 4 10% of the time and a 2 90%
            my_list = [4] * 10 + [2] * 90
            new_tile = random.choice(my_list)

            # Selects a random number from 0 to width * height -1

            spot = random.randint(0, self._grid_height * self._grid_width - 1)

            # sets location to random selection from spot
            loc = [spot / self._grid_width, spot % self._grid_width]
            # if loc is empty ( == 0 ) sets number, else repeats process.

            if self._board[loc[0]][loc[1]] == 0:
                # sets radom selected board tile to new_tile number
                self._board[loc[0]][loc[1]] = new_tile
                count += 1
            tot_count -= 1

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """

        return self._board[row][col]


"""
Merge function for 2048 game.
"""


#my_grid = TwentyFortyEight(4, 4)
# my_grid.reset()
#
# print "start: " + str(my_grid)
# my_grid.move(DOWN)
# print "D" + str(my_grid)
# my_grid.move(UP)
# print "U" + str(my_grid)
# my_grid.move(LEFT)
# print "L" + str(my_grid)
# my_grid.move(RIGHT)
# print "R" + str(my_grid)
# my_grid.move(DOWN)
# print "D" + str(my_grid)
# my_grid.move(UP)
# print "U" + str(my_grid)
#
# my_grid.move(DOWN)
# print "D" + str(my_grid)
# my_grid.move(UP)
# print "U" + str(my_grid)
# my_grid.move(LEFT)
# print "L" + str(my_grid)
# my_grid.move(RIGHT)
# print "R" + str(my_grid)
# my_grid.move(DOWN)
# print "D" + str(my_grid)
# my_grid.move(UP)
# print "U" + str(my_grid)


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
