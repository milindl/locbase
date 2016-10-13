from graph import Graph

class Location:
    def __init__(self, full_desc, intro):
        self.full_desc = full_desc
        self.intro = intro

g = Graph()
l1 = Location("A round room with a mysterious smell permeating the air", "A golden door")
l2 = Location("A small attic which smells musty", "A door above")
l3 = Location("A wide passageway surrounded by golden statues", "An open doorway")
l4 = Location("A park, with a fountain gushing water all over the central statue", "A rusted gate")
g.add_node(l1)
g.add_node(l2)
g.add_node(l3)
g.add_node(l4)
g.add_connection(l1,l2)
g.add_connection(l1,l3)
g.add_connection(l4, l2)
g.add_connection(l4, l3)

current_node = l1
prev_node = None
while True:
    print("You are in - " + current_node.full_desc)
    if prev_node:
        print("You've come here from " + prev_node.intro)
    print("\nYou are surrounded by - ")
    for i in range(len(g.connections[current_node])):
        print(str(i) + " : " + g.connections[current_node][i].intro)
    a = input("Where do you want to go? ")

    print("-------")


    prev_node = current_node
    current_node = g.connections[current_node][int(a)]
    
