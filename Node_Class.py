class Node :

    '''
    #* Class used as a node in the AVL Tree

    #? Player: Player name
    #? Score: Player score
    '''
    def __init__(self,Player,Score):
        self.liste_joueurs_node = Player
        self.score = Score
        self.left = None
        self.right = None
        self.height = 1

