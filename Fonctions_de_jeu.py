from AVL_Class import *
import random

def Creation_Dummy_Tree(myTree):

    root = None
    root = myTree.insert(root, 30, ["Bob"]) 
    root = myTree.insert(root, 20, ["Markus"]) 
    root = myTree.insert(root, 15, ["Vadim"]) 
    root = myTree.insert(root, 50, ["Yao"]) 
    root = myTree.insert(root, 50, ["Henry"]) 
    root = myTree.insert(root, 10, ["Samuel"]) 
    root = myTree.insert(root, 10, ["Vinhed"]) 
    root = myTree.insert(root, 25, ["Pierre"])
    root = myTree.insert(root, 30, ["Raphael"])
    return root

def Creation_Blank_Dummy_Tree(myTree):

    root = None
    root = myTree.insert(root, 0, ["Bob"]) 
    root = myTree.insert(root, 0, ["Markus"]) 
    root = myTree.insert(root, 0, ["Vadim"]) 
    root = myTree.insert(root, 0, ["Yao"]) 
    root = myTree.insert(root, 0, ["Henry"]) 
    root = myTree.insert(root, 0, ["Samuel"]) 
    root = myTree.insert(root, 0, ["Vinhed"]) 
    root = myTree.insert(root, 0, ["Pierre"])
    root = myTree.insert(root, 0, ["Raphael"])
    root = myTree.insert(root, 0, ["Patrick"])
    return root

def Random_Games(root,myTree, nb_joueur_par_game = 10):
    liste_joueurs_score = myTree.liste_joueurs.copy()
    nb_games = int(len(liste_joueurs_score)/nb_joueur_par_game)
    
    liste_distribution_game = []
    for i in range(nb_games):
        liste_current_game = []
        for j in range (nb_joueur_par_game):
            joueur_score_random = random.choice(liste_joueurs_score)
            liste_current_game.append(joueur_score_random)
            liste_joueurs_score.remove(joueur_score_random)
        liste_distribution_game.append(liste_current_game)
    
    return liste_distribution_game

def Ranked_Games(root,myTree, nb_joueur_par_game=10):
    liste_joueurs_ranked = []
    myTree.ListInorder(root, liste_joueurs_ranked)
    nb_games = int(len(liste_joueurs_ranked)/nb_joueur_par_game)
    liste_games = []
    for i in range(nb_games):
        liste_current_game = []
        for j in range (nb_joueur_par_game):
            liste_current_game.append(liste_joueurs_ranked[0])
            liste_joueurs_ranked.remove(liste_joueurs_ranked[0])
        liste_games.append(liste_current_game)


    return liste_games

# Return a randomized score for each player
def Random_Score():
    return random.choice(range(13))

def Random_Score_Distribution(root, myTree, liste_distribution_game):
    for poule in liste_distribution_game:
        for joueur_score in poule:
            old_score = joueur_score[1]
            new_score = Random_Score() + old_score
            player_name = joueur_score[0]
            myTree,root = myTree.update(root,[player_name],new_score)
    return myTree,root

def Manche(root, myTree, nb_joueur_par_game,random_games= False):
    if(random_games):
        distribution_game = Random_Games(root,myTree, nb_joueur_par_game)
    else:
        distribution_game = Ranked_Games(root,myTree, nb_joueur_par_game)
    myTree,root = Random_Score_Distribution(root, myTree, distribution_game)
    return myTree,root

def Drop_Worst(root, myTree, nb_worst_players_to_drop):
    classement = []
    myTree.ListInorder(root, classement)
    players_to_be_deleted = classement[:nb_worst_players_to_drop]
    for player_score in players_to_be_deleted:
        myTree,root = myTree.delete([player_score[0]])
    return myTree,root

def Jeu(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop):
    nb_de_manches_ranked = int((len(myTree.liste_joueurs) - taille_top) / nb_worst_players_to_drop)
    print("Debut de competition !")
    print()
    for i in range(3):
        myTree,root = Manche(root, myTree, nb_joueur_par_game, random_games = True)
        print("Resultats game random n{}:".format(i+1))
        myTree.printInorder(root)
        print()
    for j in range(nb_de_manches_ranked):
        myTree,root = Manche(root, myTree, nb_joueur_par_game)
        print("Resultats game ranked n{}:".format(j+1))
        myTree.printInorder(root)
        myTree, root = Drop_Worst(root, myTree, nb_worst_players_to_drop)
        print()
        print("Resultats apres drop game ranked n{}:".format(j+1))
        myTree.printInorder(root)
        print()
    

    
            
            
