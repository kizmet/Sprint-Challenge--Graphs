from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import sys

sys.path.append("./graph")
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
directions = ["n", "e", "s", "w"]
opposite_directions = {"n": "s", "e": "w", "s": "n", "w": "e"}

# graph the rooms visited and their exits
visited_rooms_graph = {}
# all the room Id's that have been visited
visited_rooms_track = set()

# add the current room to the visited rooms graph
# create directions objects "n:?,s:?"
# add to visited rooms set
def add_to_visited_rooms(visited_rooms_graph, current_room):
    if current_room.id not in visited_rooms_graph:
        exits = current_room.get_exits()
        current_exits = visited_rooms_graph[current_room.id] = {exit: "?" for exit in exits}
        visited_rooms_track.add(current_room.id)
        return current_exits


# >>> visited_rooms_graph
# {0: {'n': '?'}}


# loop through the rooms until all visited
while len(visited_rooms_graph) < len(room_graph):
    if player.current_room.id not in visited_rooms_track:
        # add room to graph and set if not already there
        current_exits = add_to_visited_rooms(visited_rooms_graph, player.current_room)
    # find new/unexplored exits
    exits = player.current_room.get_exits()
    unexplored_exits = [e for e in exits if visited_rooms_graph[player.current_room.id][e] == "?"]

    # if there are unexplored exits add it to the q
    if len(unexplored_exits) > 0:
        next_move = random.choice(unexplored_exits)
    # if all exits are explored, last room in visited rooms (go back to it)
    elif len(visited_rooms_track) > 0:
        # visited_rooms.add(visited_rooms)
        next_move = visited_rooms_track.pop()

    # go to next room
    prev_room = player.current_room
    traversal_path.append(next_move)
    player.travel(next_move)

    if player.current_room.id not in visited_rooms_track:
        # add room to graph and set if not already there
        add_to_visited_rooms(visited_rooms_graph, player.current_room)


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
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
