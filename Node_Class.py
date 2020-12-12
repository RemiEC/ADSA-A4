class Node :

    '''
    #* Classe utilisée en tant que node dans l'AVL Tree

    #? Player : Nom du player
    #? Score : Score du player
    '''
    def __init__(self,Player,Score):
        self.list_player = Player
        self.score = Score
        self.left = None
        self.right = None
        self.height = 1

