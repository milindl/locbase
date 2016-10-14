from graph import Graph
from obj import Object
from happening import Happening, Trigger

class Location:
    def __init__(self, full_desc, intro, objects = [], happenings = []):
        self.full_desc = full_desc
        self.intro = intro
        self.objects = objects
        self.happenings = happenings

    def remove_object(self,ob):
        assert ob in self.objects
        self.objects.remove(ob)

    def add_object(self,ob):
        self.objects.append(ob)

    def add_happening(self,hap):
        assert hap.trigger is Trigger.location_based
        self.happenings.append(hap)

    def remove_happening(self,hap):
        assert hap in self.happenings
        self.happenings.remove(hap)

def take_item(hap,haplist,inv):
    haplist.remove(hap)
    inv = []
    return inv

def strange_whispers(hap, haplist, game_state):
    return game_state
    
g = Graph()
o1 = Object("A golden CD")
o2 = Object("A red shirt")
o31 = Object("A dead mouse")
o32 = Object("A dead mouse")
o33 = Object("A dead mouse")
o34 = Object("A dead mouse")
o35 = Object("A dead mouse")
o4 = Object("A smelly, round chocolate")
h1 = Happening("A strange voice whispers in your ear", trigger = Trigger.location_based, action_call = strange_whispers)
h = Happening("All your items are taken away magically", trigger = Trigger.location_based, action_call = take_item)
l1 = Location("A round room with a mysterious smell permeating the air", "A golden door")
l1.add_object(o4)
''' '''
l2 = Location("A small attic which smells musty", "A door above", [o31, o32, o33, o34, o35], [h1])
l3 = Location("A wide passageway surrounded by golden statues", "An open doorway", [o1], [h])
l4 = Location("A park, with a fountain gushing water all over the central statue", "A rusted gate", [o2])
g.add_node(l1)
g.add_node(l2)
g.add_node(l3)
g.add_node(l4)
g.add_connection(l1,l2)
g.add_connection(l1,l3)
g.add_connection(l4, l2)
g.add_connection(l4, l3)

inventory = []
current_node = l1
prev_node = None
while True:
    for hap in current_node.happenings:
        print("Something has happened! " + hap.nature) 
        inventory = hap.action_call(hap,current_node.happenings, inventory)
    print("You are in - " + current_node.full_desc)
    if prev_node:
        print("You've come here from " + prev_node.intro)
    print("\nYou are surrounded by (go #)")
    for i in range(len(g.connections[current_node])):
        print(str(i) + " : " + g.connections[current_node][i].intro)
    if len(current_node.objects) != 0: print("Near you are also several objects(take #): ")
    for i in range(len(current_node.objects)):
        print(str(i) + " : " + current_node.objects[i].desc)
        

    a = input("\n>")
            
    while a.startswith("inventory"):
        print([x.desc for x in inventory])
        a = input("\n>")
            

    if a.startswith("go"):
        a = a[3:]
        prev_node = current_node
        current_node = g.connections[current_node][int(a)]
    elif a.startswith("take"):
        a = a[5:]
        inventory.append(current_node.objects[i])
        current_node.objects.remove(current_node.objects[i])
        
    
    print("\n\n")
