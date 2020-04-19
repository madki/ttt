import numpy as np
import random

vertices = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 4, 8),
    (2, 4, 6),
    (0, 3, 6),
    (1, 4, 6),
    (2, 5, 8)
]

# 0, 1, 2
# 3, 4, 5
# 6, 7, 8

class Game:
    def __init__(self):
        self.state = [0]*10
        self.count = 0

    def makeMove(self, index, value):
        if (not (value == -1 or value == 1)): 
            raise ValueError("Invalid input for value should be -1 or 1")
        if (self.state[index] == 0):
            self.state[index] = value
            self.count = self.count + 1
            return True
        else:
            return False

    def result(self):
        return (self._winner(), self.result)
    
    def _winner(self):
        for (a, b, c) in vertices:
            if ((self.state[a] == self.state[b]) and (self.state[b] == self.state[c]) and (self.state[b] != 0)):
               return self.state[b]
        if (self.count == 9):
            return -2
        else:
            return 0
        
def possibleActions(state):
    return [i for i,x in enumerate(state) if x == 0]

def randomAction(state):
    actions = possibleActions(state)
    randIndex = random.randint(0, len(actions) - 1)
    return actions[randIndex]

def toXO(value):
    if (value == 1):
        return "X"
    elif value == -1:
        return "O"
    else:
        return " "
    

def printBoard(state):
    print("=========")
    print(toXO(state[0]) + " | " + toXO(state[1]) + " | " + toXO(state[2]))
    print(toXO(state[3]) + " | " + toXO(state[4]) + " | " + toXO(state[5]))
    print(toXO(state[6]) + " | " + toXO(state[7]) + " | " + toXO(state[8]))
    print("#########")

game = Game()
turn = 1
while game.result()[0] == 0:
    action = randomAction(game.state)
    game.makeMove(action, turn)
    turn = turn * -1
    printBoard(game.state)