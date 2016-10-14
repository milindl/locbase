from graph import Graph
from loctest import Location
from obj import Object
from happening import Happening,Trigger
from gamestate import GameState
from chapter import Chapter


class CakeChapter(Chapter):
    def start_game(self,init_state):
        print("Hi, the basic commands you need to know are go <number>, take <number>, use and inventory")
        input("Press return to continue...")
        gs = init_state # game_state
        while not gs.cmp_gamestate(self.end_gamestate):
            if gs.curr_location.full_desc != "":
                print("\n\n\nYou are in " + gs.curr_location.full_desc)


            # Need to trigger any events here
            for hap in gs.curr_location.happenings:
                gs = hap.action_call(hap, gs.curr_location.happenings, gs)
                if gs.cmp_gamestate(self.end_gamestate): break
            input("..")

            
            i = 0

            # Populate with objects

            if gs.curr_location.objects and len(gs.curr_location.objects) != 0:
                print("\nAround you, you see: ")
                for obj in gs.curr_location.objects:
                    print(str(i) + " : " + obj.desc)
                    i += 1
            
                    
            # Printing next location(s)
            i = 0
            if gs.previous_location: print("\nYou came here from " + gs.previous_location.intro)
            print("\nYou can choose to move towards...: ")
            for neighbour in self.loc_graph.connections[gs.curr_location]:
                print(str(i) + " : " + neighbour.intro)
                i += 1

            a = input("\n>>")

            if a.startswith("take "):
                gs.inventory.append(gs.curr_location.objects[int(a[5:])])
                gs.curr_location.objects.remove(gs.inventory[-1])

            if a.startswith("use"):
                self.use_object(gs)

            if a.startswith("inventory"):
                for item in inventory:
                    print(item.desc)
                
            # Now, we need to go somewhere
            if a.startswith("go "):
                gs.previous_location = gs.curr_location
                gs.curr_location = self.loc_graph.connections[gs.curr_location][int(a[3:])]



    
def Main():
    # Make Starting Graph
    loc_g = Graph()
    start = Location("a futuristic looking chamber, colored gray, with blue LED stripes lighting the way to a door, which leads to a fork.", "The starting chamber")
    loc_g.add_node(start)
    dec1 = Location("a passageway. There is nothing here except a fork. You need to decide where to go -- another fork, or a penumatic door", "fork1")
    loc_g.add_node(dec1)
    dec2 = Location("another passageway. the LED strips on the ground work fine, but the ones on the roof are not working. There is slight sparking. You need to decide where to go -- the dark room, or the nice-smelling one.", "fork2")
    loc_g.add_node(dec2)
    cakeroom = Location("a room which smells like fresh baked cake. There is a pedestal in the center, which you approach", "A door which smells nice")
    loc_g.add_node(cakeroom)
    gladosroom = Location("a chamber which is full of broken machinery and electronics. You try approachign it, but the residual, high voltage sparking discourages you.", "A dark, doorless room in which you can hear some static")
    loc_g.add_node(gladosroom)
    tmachine_initial = Location("a sophisticated, high tech room. In the middle, there's a strange looking machine, a faded label identifying it as 'Brand New Remote Controlled Teleportation Machine'", "Pneumatic door")
    loc_g.add_node(tmachine_initial)
    tmachine_final = Location("a sophisticated, high tech room. In the middle, there's a teleportation machine.", "Another pneumatic door from teleportation machine to passageway.")
    loc_g.add_node(tmachine_final)
    middle_room = Location("a passageway. The LED strips look lacklustre as a strange medley of blue and orange light dances across the room. You can explore the glowing rooms, go back, or go ahead", "Strangely lit passageway")
    loc_g.add_node(middle_room)
    blue_room = Location("", "a room glowing blue")
    loc_g.add_node(blue_room)
    orange_room = Location("", "a room glowing orange")
    loc_g.add_node(orange_room)
    end_room = Location("a blackness in which you cannot see. The words 'What is the passphrase' seems to echo around your mind, somehow typed in monospace. You seem to be able to type, however", "The door ahead")
    loc_g.add_node(end_room)

    #Start Location Linking

    loc_g.add_connection(start, dec1)
    loc_g.add_connection(dec1, dec2)
    loc_g.add_connection(dec2, cakeroom)
    loc_g.add_connection(dec2, gladosroom)
    loc_g.add_connection(dec1, tmachine_initial)
    loc_g.add_connection(tmachine_final, middle_room)
    loc_g.add_connection(middle_room, blue_room)
    loc_g.add_connection(middle_room, orange_room)
    loc_g.add_connection(middle_room, end_room)


    # Start adding objects to rooms
    def tp_action(gs1):
    # Action for teleportation
        if gs1.curr_location == tmachine_initial:
            gs1.curr_location = tmachine_final
        elif gs1.curr_location == tmachine_final:
            gs1.curr_location = tmachine_initial
        else:
            print("The device shows an error: No Teleporting Machine Nearby")
            input()
            return gs1
        print("You feel a strange sensation. You body is broken down and suddenly you black out")
        input()
        gs1.previous_location = None
        return gs1

    cake_obj = Object("A cake covered with pink frosting. It was baked freshly.")
    teleporter_obj = Object("A strange remote.. It has a big button labelled 'TELEPORT ME'", {"push button": tp_action, "press button": tp_action, "press":tp_action})
    
    cakeroom.objects.append(cake_obj)
    gladosroom.objects.append(teleporter_obj)

    #Start making events
    def cake_away(hap, haplist, gs1):
        if cake_obj in gs1.inventory: gs1.inventory.remove(cake_obj)
        else: return gs1
        haplist.remove(hap)
        print(hap.nature)
        return gs1
    def blueorange_move(hap, haplist, gs1):
        gs1.curr_location = middle_room
        gs1.previous_location = None
        print(hap.nature)
        input()
        return gs1
    def final_pass(hap, haplist, gs1):
        print("Enter the final passphrase. It's not delicious, but it'll get you out of here.")
        passp = ""
        passp = input()
        while passp != "cakeisalie":
            passp = input("Enter the final passphrase to escape. Or, stay here forever\n")
        gs1.score = 100
        return gs1
    
    cake_dis_hap = Happening("Suddenly, a feeling of gloom comes over you. You check your backpack. The cake has disappeared!", Trigger.location_based, cake_away)
    dec2.happenings.append(cake_dis_hap)

    whisper_hap = Happening("You hear a voice whisper from the rubble in front of you.\nWelcome [static] Aperture Science computer [static] center.", Trigger.location_based)
    gladosroom.happenings.append(whisper_hap)

    blueorange_room_hap = Happening("After several flashes of bright blue and orange light, you find that you are back at the same position!", Trigger.location_based, blueorange_move)

    final_hap = Happening("It's time to type!", Trigger.location_based, final_pass)
    

    blue_room.happenings.append(blueorange_room_hap)
    orange_room.happenings.append(blueorange_room_hap)
    end_room.happenings.append(final_hap)
    # Start main loop of the game

    ch = CakeChapter(loc_g, {}, GameState(score = 50, inventory = [], curr_location = None))
    init_gamestate = GameState(score = 0, inventory = [], curr_location = start)
    ch.start_game(init_gamestate)

Main()
