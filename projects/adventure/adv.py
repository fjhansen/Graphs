from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
print("Rooms: ",world.rooms)
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
visited = {}
backtrack = []

# we reverse the directions to traverse backwards. sorta like unwinding 
unwind = {'n': 's', 'e': 'w', 's': "n", "w": "e"}


# visited[0] = ['n']
# visited[0] == {0: ['n']}
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):
    #print("Length:",len(visited[player.current_room.id]))
    #print("Current:",player.current_room.id)
    #print("Visited:", visited)


    #print("Directions", visited[player.current_room.id])

    # Check if current room has been added to visited
    if player.current_room.id not in visited:
        # grab exits for curr room and put in dic
        visited[player.current_room.id] = player.current_room.get_exits()
        # we need to keep track of the previous direcion as well
        prev_move = backtrack[-1]

        # remove the direction from curr room we went to so it is not repeated
        visited[player.current_room.id].remove(prev_move)

    # maps after the first will start you off with an empty array due to removal so this must be accounted for
    # to keep going!
    if len(visited[player.current_room.id]) == 0:
           #print("EMPTY")
        
           # goes back in backtrack to keep looking for new paths
           # [w,w]
           # prev_move == 'w'
           prev_move = backtrack[-1]
           # popping once again but this time on backtrack
           # pop the old w ; ['w'] 
           backtrack.pop()
           # keeping track of the prev path
           # ['e','e'] now looks like ['e','e','w']
           traversal_path.append(prev_move)
           # keep on movin; prev_move == 'w'
           player.travel(prev_move)
           

    else:
        #print("ELSE")
        
        # current room has been marked as visited, now what?
        # we get the next place to visit!
        next_path = visited[player.current_room.id][-1]
        # pop based on current room id. ['n']
        visited[player.current_room.id].pop()
        # lets keep on movin; next_path == 'n'
        player.travel(next_path)
        # now we have to unwind to get to a new room to visit ; n -> s
        backtrack.append(unwind[next_path])
        # also append the next path to the traversal_path
        traversal_path.append(next_path)

    
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






player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "l":
        print(room.name)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")


# ideas for stretch
# maybe refractor into using an actual stack
# or maybe try to better impliment path finding with something like Dijkstra/Greedy alg
# would need a queue for ^^^
