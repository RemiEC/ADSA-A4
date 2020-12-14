import math
import pandas as pd

inf = math.inf


# We set the value infinite to represent an impossible movement between 2 rooms
adjacency_matrix_crewmate = [
    [0, 7, 5.5, 5.5, 9, 7,inf,inf,inf,inf,inf,inf,inf,inf],
    [7,0, 5.5, 5.5,inf,inf,inf,inf,inf,inf, 10, 8.5,inf,inf],
    [5.5, 5.5,0, 4,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [5.5, 5.5, 4,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [9,inf,inf,inf,0, 7, 5.5,inf,inf,inf, 8.5,inf, 7.5,inf],
    [7,inf,inf,inf, 7,0,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf, 5.5,inf,0, 4.5, 7.5, 10,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf, 4.5,0, 7, 9.5,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf, 7.5, 7,0, 8.5,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf, 10, 9.5, 8.5,0, 6,inf,inf, 4],
    [inf, 10,inf,inf, 8.5,inf,inf,inf,inf, 6,0, 7.5, 7, 6],
    [inf, 8.5,inf,inf,inf,inf,inf,inf,inf,inf, 7.5,0,inf,inf],
    [inf,inf,inf,inf, 7.5,inf,inf,inf,inf,inf, 7,inf,0,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf, 4, 6,inf,inf,0]
]

Room_list_crewmate = [
    "Upper E",
    "Lower E",
    "Reactor",
    "Security",
    "Cafeteria",
    "Medbay",
    "Weapons",
    "O2",
    "Navigation",
    "Shield",
    "Storage",
    "Electrical",
    "Between Cafet-Storage",
    "Between Storage-Shield"
]


# We created this adjacency matrix by taking the shortest path available between 2 adjacent rooms when 2 options were available : regular path and vent
adjacency_matrix_impostor = [
    [0, 7, 0, 5.5, 9, 7, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [7,0, 0, 5.5, inf, inf, inf, inf, inf,inf, 10, 8.5,inf,inf,inf],
    [0,0,0, 4,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [5.5, 5.5, 4,0,inf,0,inf,inf,inf,inf,inf,0,inf,inf,inf],
    [9,inf,inf,inf,0, 7, 5.5,inf,inf,inf, 8.5,inf,0,inf,0],
    [7,inf,inf,0, 7,0,inf,inf,inf,inf,inf,0,inf,inf,inf],
    [inf,inf,inf,inf, 5.5,inf,0, 4.5,0, 10,inf,inf,inf,inf, 6.5],
    [inf,inf,inf,inf,inf,inf, 4.5,0, 7, 9.5,inf,inf,inf,inf, 6],
    [inf,inf,inf,inf,inf,inf,0, 7,0,0,inf,inf,inf,inf, 5],
    [inf,inf,inf,inf,inf,inf, 10, 9.5,0,0, 6,inf,inf, 4, 3.5],
    [inf, 10,inf,inf, 8.5,inf,inf,inf,inf, 6,0, 7.5, 7, 6,inf],
    [inf, 8.5,inf,0,inf,0,inf,inf,inf,inf, 7.5,0,inf,inf,inf],
    [inf,inf,inf,inf,0,inf,inf,inf,inf,inf, 7,inf,0,inf,0],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf, 4, 6,inf,inf,0,inf],
    [inf,inf,inf,inf,0,inf, 6.5, 6, 5, 3.5,inf,inf,0,inf,0],
]

Room_list_impostor = [
    "Upper E",
    "Lower E",
    "Reactor",
    "Security",
    "Cafeteria",
    "Medbay",
    "Weapons",
    "O2",
    "Navigation",
    "Shield",
    "Storage",
    "Electrical",
    "Between Cafet-Storage",
    "Between Storage-Shield",
    "Vent btwn Shield-Nav"
]


'''
#* Function printing a dataframe containing the travel time between each pair of room for crewmate or impostor

#? adjacency_matrix : Adjacency matrix of impostor or crewmate created from the png graph in the report
#? Room_list : List of the Rooms
'''
def Floyd_Warshall_Algorithm(adjacency_matrix, Room_list):
    taille_matrix = len(adjacency_matrix)
    for k in range (taille_matrix):
        for i in range (taille_matrix):
            for j in range(taille_matrix):
                if(adjacency_matrix[i][j] > adjacency_matrix[i][k] + adjacency_matrix[k][j]):
                    adjacency_matrix[i][j] = adjacency_matrix[i][k] + adjacency_matrix[k][j]

    #Now we display the result
    dataframe = pd.DataFrame(adjacency_matrix)
    dataframe.columns = Room_list
    dataframe.index = Room_list
    pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.width', None)
    print()
    print(dataframe)
    return dataframe
        

def interval_time_impostor(dataframe_crewmate, dataframe_impostor):
    dataframe_interval = dataframe_crewmate.copy()
    #We use the length of the crewmate dataframe because we don't want to affect the 'Vent btwn Shield-Nav' row and column
    for i in range (dataframe_crewmate.shape[0]):
        for j in range(dataframe_crewmate.shape[0]):
            dataframe_interval.iloc[i,j] = str("[{},{}[".format(dataframe_impostor.iloc[i,j],dataframe_crewmate.iloc[i,j]))
    print(dataframe_interval)

if __name__ == "__main__":
    # USING THE ALGORITHM

    # CREWMATE
    dataframe_crewmate = Floyd_Warshall_Algorithm(adjacency_matrix_crewmate, Room_list_crewmate)

    # IMPOSTOR
    dataframe_impostor = Floyd_Warshall_Algorithm(adjacency_matrix_impostor, Room_list_impostor)

    print()
    interval_time_impostor(dataframe_crewmate, dataframe_impostor)


