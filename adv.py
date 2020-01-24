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
# opposite_directions = {"n": "s", "e": "w", "s": "n", "w": "e"}


def search():
    explored_rooms = {}
    stack = Stack()
    stack.push([starting_vertex])
    visited = set()
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            if vertex == destination_vertex:
                return path
            # print(vertex)
            visited.add(vertex)
            for next_vert in self.get_neighbors(vertex):
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)


# TRAVERSAL TEST
search()


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
