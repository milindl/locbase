from graph import Graph
from loctest import Location
from obj import Object
from happening import Happening

class GameState:
    def __init__(self, inventory, score, curr_location, previous_location=None):
        self.inventory = inventory
        self.score = score
        self.curr_location = curr_location
        self.previous_location = previous_location
        self.events_triggered = []

    def cmp_gamestate(self, e_game):
        same = True
        if e_game.inventory != None:
            same = same and (set(e_game.inventory)<=set(self.inventory))
        if e_game.score != None:
            same = same and (e_game.score <= self.score)

        if e_game.curr_location != None:
            same = same and (e_game.curr_location == self.curr_location)

        return same
            
