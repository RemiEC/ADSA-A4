from AVL_Class import *
import random

def Creation_Dummy_Tree(myTree):

    root = None
    
    root = myTree.insert(root, 30, ["Bob"]) 
    root = myTree.insert(root, 20, ["Markus"]) 
    root = myTree.insert(root, 15, ["Vadim"]) 
    root = myTree.insert(root, 50, ["Henry"]) 
    root = myTree.insert(root, 10, ["Samuel"]) 
    root = myTree.insert(root, 10, ["Vinhed"]) 
    root = myTree.insert(root, 25, ["Pierre"])
    root = myTree.insert(root, 30, ["Raphael"])

    return root

def Random_Games(myTree, nb_joueur_par_game = 10):
    root = Creation_Dummy_Tree(myTree)
    liste_joueurs = myTree.liste_joueurs
    nb_games = int(len(liste_joueurs)/nb_joueur_par_game)
    
    liste_distribution_game = []
    for i in range(nb_games):
        liste_current_game = []
        for j in range (nb_joueur_par_game):
            joueur_random = random.choice(liste_joueurs)
            liste_current_game.append(joueur_random)
            liste_joueurs.remove(joueur_random)
        liste_distribution_game.append(liste_current_game)
    
    return liste_distribution_game