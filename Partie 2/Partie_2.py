
'''
#* Function returning an updated list of suspects after a death report
#* Obviously the adjacency list has to be updated between each murder

#? matrice_adjacence : Adjacency matrix of the 'Who saw Who' graph, list of list of 0 or 1
#? mort : the victim's number
#? ancienne_liste_suspects : an anterior list of suspect 
'''
def Trouver_Suspects(matrice_adjacence, mort, ancienne_liste_suspects = None):
    # We determine who has seen the victim
    suspects_courants = []
    for i in range(len(matrice_adjacence[mort])):
        if(matrice_adjacence[mort][i] == 1):
            # The victim has seen this player
            # We want to know who this player hasn't seen
            for j in range(len(matrice_adjacence[i])):
                if(matrice_adjacence[i][j] == 0 and i!=j and (j,i) not in suspects_courants):
                    # We check if the j player hasn't been seen by i, if they are different and if we don't already 
                    # have this set in a different order
                    suspects_courants.append((i,j))
    if ancienne_liste_suspects != None:
        # We already have a list of suspects from a previous crime, the correct set has to be in both the current
        # and the previous lists
        for suspects_set in suspects_courants.copy():
            if (suspects_set not in ancienne_liste_suspects):
                suspects_courants.remove(suspects_set)
    return suspects_courants

# Adjacency list based on the graph we created
adjacency_matrix = [
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
]
suspects = Trouver_Suspects(adjacency_matrix,0)

print(suspects)
