'''
#* Function updating the list of possible paths

#? connections : dictonnary of all the rooms (keys) and their connections to other rooms (list of rooms)
#? start : room from which we begin the path
#? visited : dictonnary of all the rooms (keys) and a boolean value to indicate if they were visited or not
#? path : current path we are looking at 
#? N : maximum of vertices
#? list_paths : list in which we put all the possible hamiltonian paths
'''
def Hamiltonian_Paths(connections, start, visited, path, N, list_paths):
 
    # if all the vertices are visited, then hamiltonian path exists
    if len(path) == N:
        # append hamiltonian path to the list of possible path
        print(path)
        list_paths.append(path.copy())
        return
 
    # Check if every edge starting from vertex v leads to a solution or not
    for room in connections[start]:
 
        # process only unvisited vertices as hamiltonian
        # path visits each vertex exactly once
        if not visited[room]:
            visited[room] = True
            path.append(room)
 
            # check if adding vertex w to the path leads to solution or not
            Hamiltonian_Paths(connections, room, visited, path, N, list_paths)
 
            # Backtrack
            visited[room] = False
            path.pop()
 
 
if __name__ == '__main__':
    print()

    # Declare our variable
    list_paths = []

    # Set number of vertices in the graph
    N = 14
 
    # Create a graph from edges
    connections = {
        "Upper E" : ["Reactor","Lower E","Security","Medbay","Cafeteria"],
        "Reactor" : ["Upper E","Security","Lower E"],
        "Lower E" : ["Reactor","Upper E","Security","Electrical","Storage"],
        "Security" : ["Upper E","Reactor","Lower E"],
        "Medbay" : ["Upper E","Cafeteria"],
        "Cafeteria" : ["Upper E","Medbay","Storage","Between Cafet-Storage","Weapons"],
        "Between Cafet-Storage" : ["Cafeteria","Storage"],
        "Electrical" : ["Lower E","Storage"],
        "Storage" : ["Lower E","Electrical","Cafeteria","Between Cafet-Storage","Shield","Between Storage-Shield"],
        "Between Storage-Shield" : ["Storage","Shield"],
        "Shield" : ["Storage","Between Storage-Shield","O2","Weapons","Navigation"],
        "O2" : ["Weapons","Shield","Navigation"],
        "Weapons" : ["Cafeteria","Shield","Navigation","O2"],
        "Navigation" : ["O2","Weapons","Shield"]
    }

    # Starting rooms
    starting_rooms = ["Upper E","Medbay","Between Storage-Shield","Weapons"]

    for start in starting_rooms:
        # add starting room to the path
        path = [start]

        # Declare all visited rooms to false when changing the starting room
        visited = {
            "Upper E" : False,
            "Reactor" : False,
            "Lower E" : False,
            "Security" : False,
            "Medbay" : False,
            "Cafeteria" : False,
            "Between Cafet-Storage" : False,
            "Electrical" : False,
            "Storage" : False,
            "Between Storage-Shield" : False,
            "Shield" : False,
            "O2" : False,
            "Weapons" : False,
            "Navigation" : False
        }

        # Mark start room as visited
        visited[start] = True

        # Do the algorithm
        Hamiltonian_Paths(connections, start, visited, path, N, list_paths)


    # Declare our list of penalities associated to the different paths
    list_penalities = []

    # Apply a penaltie on each room because of their dangerosity
    penalties_room = {
        "Upper E" : 0.6,
        "Reactor" : 0.8,
        "Lower E" : 0.4,
        "Security" : 0.3,
        "Medbay" : 0.8,
        "Cafeteria" : 0.35,
        "Between Cafet-Storage" : 0.8,
        "Electrical" : 0.8,
        "Storage" : 0.45,
        "Between Storage-Shield" : 0.8,
        "Shield" : 0.5,
        "O2" : 0.55,
        "Weapons" : 0.4,
        "Navigation" : 0.85
    }

    # We apply the penalty on each path to determine the best
    for path in list_paths:
        sum = 0
        for order in range(len(path)):
            sum += (1+order/10) * penalties_room[path[order]]
        list_penalities.append(sum)

    # We get the index of the min value
    min_index = list_penalities.index(min(list_penalities))

    # The best hamiltonian path is at the same index so we just get it and print it
    best_hamiltonian_path = list_paths[min_index]
    print()
    print(best_hamiltonian_path)