from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#-------------------------------------------------------------------------------------

traversal_path = []

opposites = {"n": "s", "s": "n", "w": "e", "e": "w"}

previous_steps = []
room_path = {}
visited = set()

# keep going until visit all rooms
while len(visited) < len(room_graph):
    room_id = player.current_room.id

    # if this is the first time visiting the room
    if room_id not in room_path:
        # save it in 'visited' (no duplicates)
        visited.add(room_id)
        # save all possible directions for this room
        room_path[room_id] = player.current_room.get_exits()

    # if there's no directions left, go back
    if len(room_path[room_id]) < 1:
        previous_direction = previous_steps.pop()
        traversal_path.append(previous_direction)

        # move user
        player.travel(previous_direction)
    else:
        # take a possible direction from the end of the list
        next_direction = room_path[room_id].pop()

        # record it
        traversal_path.append(next_direction)

        # save directions for later, so that I can go back
        previous_steps.append(opposites[next_direction])

        # move user to another room
        player.travel(next_direction)



#-------------------------------------------------------------------------------------

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
