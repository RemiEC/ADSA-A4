from AVL_Class import *
from Fonctions_de_jeu import *

'''
#* Function allowing to test the delete function

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
'''
def Test_Delete(root,myTree):
    print(myTree.liste_joueurs_score)
    myTree.printInorder(root)
    myTree,root = myTree.delete("Vadim")
    myTree,root = myTree.delete("Bob")
    myTree,root = myTree.delete("Yao")
    print()
    print ("Nouvelle version apres Delete")
    print()
    print(myTree.liste_joueurs_score)
    myTree.printInorder(root)


'''
#* Function allowing to test the update function

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
'''
def Test_Update(root,myTree):
    myTree.printInorder(root)
    myTree,root = myTree.update(root, "Bob", 5)
    myTree,root = myTree.update(root, "Raphael", 15)
    print()
    print ("Nouvelle version apres Update")
    print()
    myTree.printInorder(root)


'''
#* Function allowing to test the creation of random games

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
'''
def Test_Random_Games(root,myTree, nb_joueur_par_game):
    liste_all_games = Random_Games(root,myTree, nb_joueur_par_game)
    i=1
    for game in liste_all_games:
        print("Poule {} : ".format(i))
        print(game)
        print()
        i+=1


'''
#* Function allowing to test the creation of ranked games

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
'''
def Test_Ranked_Games(root,myTree, nb_joueur_par_game):
    liste_all_games = Ranked_Games(root,myTree, nb_joueur_par_game)
    i=1
    for game in liste_all_games:
        print("Poule {} : ".format(i))
        print(game)
        print()
        i+=1


'''
#* Function allowing to test a round
'''
def Test_Manche():
    myTree = AVL_Tree()
    root = Creation_Dummy_Tree(myTree)
    myTree.printInorder(root)
    print()
    myTree,root = Round(root, myTree, 2, random_games = False)
    myTree.printInorder(root)


'''
#* Function allowing to test the game itself

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
#? taille_top : number of finalists players that we want
#? nb_worst_players_to_drop : number of players that we want to drop at the end of each game
'''
def Test_Jeu(root, myTree, nb_joueur_par_game, taille_top, nb_worst_players_to_drop):
    myTree,root = Jeu_Avant_Finalistes(root,myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop )
    Jeu_Finalistes(root,myTree,nb_joueur_par_game)


if __name__ == "__main__":
    # Declaration of the needed variables
    nb_joueur_par_game = 4
    taille_top = 4
    nb_worst_players_to_drop = 4
    myTree = AVL_Tree()
    root = Creation_Tree_Beggining_Competition(myTree)

    # Functions to test
    #Test_Delete(root,myTree)
    #Test_Update(root,myTree)
    #Test_Random_Games(root,myTree,2)
    #Test_Ranked_Games(root,myTree,2)
    #Test_Manche()
    Test_Jeu(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop)
    