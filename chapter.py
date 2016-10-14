from graph import Graph
from loctest import Location
from obj import Object
from happening import Happening
from gamestate import GameState

class Chapter:
    def __init__(self, loc_graph, event_checkers, end_gamestate):
        '''
        event_checkers is a dictionary full of methods returning a boolean pointing to certain events that need to be triggered when the boolean is true

        '''
        self.loc_graph = loc_graph
        self.event_checkers = event_checkers
        self.end_gamestate = end_gamestate

    def use_object(self, gs):
        i = 0
        print("You currently have: ")
        for item in gs.inventory:
            print(str(i) + " : " + item.desc)
            i+=1
        i = input("To use an item, type 'actionName:itemNumber' \n>>")
        return gs.inventory[int(i.split(':')[1])].parse_action(i.split(':')[0], gs)
        
    def start_game(self, init_gamestate):
        game_state = init_gamestate
        while not game_state.cmp_gamestate(self.end_gamestate):
            print("You are in " + game_state.curr_location.full_desc)

            print("You are near: (go #)")
            i=0
            for neighbour in self.loc_graph.connections[game_state.curr_location]:
                print(str(i) + " " + neighbour.intro)
                i += 1

            nex = input("\n>")

            if nex.startswith("go "):
                nex = nex[3:]
                game_state.previous_location = game_state.curr_location
                game_state.curr_location = self.loc_graph.connections[game_state.curr_location][int(nex)]

        print("Ended game")


# End class here

def Main():
    loc_g = Graph()
    loc_a = Location("Location A", "A door")
    loc_b = Location("Location B", "A door")
    loc_g.add_node(loc_a)
    loc_g.add_node(loc_b)
    loc_g.add_connection(loc_a, loc_b)
    
    e_gamestate = GameState(None, score = 50, curr_location = None)
    event_checkers = {}

    c = Chapter(loc_g, event_checkers, e_gamestate)

    new_game = GameState([], 0, curr_location = loc_a)
    c.start_game(new_game)
    

