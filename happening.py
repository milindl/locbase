from enum import Enum

class Trigger(Enum):
    location_based = 1
    call_based = 2

def _default_action(happening, hap_list, game_state):
    print(happening.nature)
    hap_list.remove(happening)
    return game_state

    
class Happening:
    def __init__(self, nature, trigger = Trigger.location_based, action_call = _default_action):
        '''Conventionally, the action_call will be structured like this :
        action_call(happening, hap_list, game_state) -> game_state_modified
        where game state can be anything you want changed
        '''
        self.nature = nature
        self.trigger = trigger
        self.action_call = action_call
