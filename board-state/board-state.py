import os
import sys
import numpy as np
import enum

#
class X_O(enum.Enum):
    def __str__(self):
        return self.value
    _X = -1
    _XO = 0
    _O = 1


class BoardSate:
    def __init__(self):
        self.grid = np.zeros((3,3))
        self.curr_input = None
        self.start = None
        self.curr_turn = None
        

        return
    
    def _SetNextState(self):

        return

    
    #DO I/O input here
    def _GetInput(self):
        pos = None
        return pos, self.curr_input

    #Validate input
    def _ValidateInput(self, pos):


        if self.curr_input != self.curr_turn:
            print("Enter the correct move:")
            self._GetInput()

        if self.grid[pos[0]][pos[1]] != X_O._X or self.grid[pos[0][pos[1]]] != X_O._O:
            print("Enter valid position:")
        return

    #Check Terminal
    # Do I need a seperate method for CheckTerminal Winner state
    def _CheckTerminal(self):
        return

    def _CheckWinningState(self):
        #return either won or lost and the player won
        return
    