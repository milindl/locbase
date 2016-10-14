
class Object:
    def __init__(self, desc, actions = {}):
    
        self.desc = desc
        self.actions = actions # Reserved for future use - will be a dictionary of "action_name" : action_method pairings
        self.rel_actions = {} # Resv for future use

    def parse_action(self, actn, gs):
        if actn not in self.actions:
            print("Sorry, action unavailable")
            return gs
        
        return self.actions[actn](gs)
