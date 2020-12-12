from AVL_Class import *
from Fonctions_de_jeu import *

def Test_Delete(root,myTree):
    print(myTree.liste_joueurs)
    myTree.printInorder(root)
    myTree,root = myTree.delete("Vadim")
    myTree,root = myTree.delete("Bob")
    myTree,root = myTree.delete("Yao")
    print()
    print ("Nouvelle version apres Delete")
    print()
    print(myTree.liste_joueurs)
    myTree.printInorder(root)

def Test_Update(root,myTree):
    myTree.printInorder(root)
    myTree,root = myTree.update(root, "Bob", 5)
    myTree,root = myTree.update(root, "Raphael", 15)
    print()
    print ("Nouvelle version apres Update")
    print()
    myTree.printInorder(root)

def Test_Distribution_Random_Games(root,myTree, nb_joueur_par_game):
    distribution_game = Random_Games(root,myTree, nb_joueur_par_game)
    i=1
    for game in distribution_game:
        print("Poule {} : ".format(i))
        print(game)
        print()
        i+=1

def Test_Distribution_Ranked_Games(root,myTree, nb_joueur_par_game):
    distribution_game = Ranked_Games(root,myTree, nb_joueur_par_game)
    
    i=1
    for game in distribution_game:
        print("Poule {} : ".format(i))
        print(game)
        print()
        i+=1

def Test_Random_Game_Score_Distribution(root, myTree, liste_distribution_game, random_games, nb_joueur_par_game):
    if(random_games):
        distribution_game = Random_Games(root,myTree, nb_joueur_par_game)
    else:
        distribution_game = Ranked_Games(root,myTree, nb_joueur_par_game)
    return distribution_game

def Test_Manche():
    myTree = AVL_Tree()
    root = Creation_Dummy_Tree(myTree)
    myTree.printInorder(root)
    print()
    myTree,root = Manche(root, myTree, 2, random_games = False)
    myTree.printInorder(root)

def Test_Jeu(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop):
    myTree,root = Jeu_Avant_Finalistes(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop )
    Jeu_Finalistes(root, myTree,nb_joueur_par_game)

if __name__ == "__main__":
    myTree = AVL_Tree()
    root = Creation_Blank_Dummy_Tree(myTree)
    #Test_Delete(root,myTree)
    #Test_Update(root,myTree)
    #Test_Distribution_Random_Games(root,myTree,2)
    #Test_Distribution_Ranked_Games(root,myTree,2)
    #Test_Manche()
    nb_joueur_par_game = 4
    taille_top = 4
    nb_worst_players_to_drop = 4
    Test_Jeu(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop)
    