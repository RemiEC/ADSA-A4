from AVL_Class import *
from Fonctions_de_jeu import *

def Test_Delete():
    myTree = AVL_Tree()
    root = Creation_Dummy_Tree(myTree)
    print(myTree.liste_joueurs)
    myTree.printInorder(root)
    myTree.delete(root, 30, ["Raphael"])
    myTree.delete(root, 20, ["Markus"])
    print()
    print ("Nouvelle version apres Delete")
    print()
    print(myTree.liste_joueurs)
    myTree.printInorder(root)
    

def Test_Update():
    myTree = AVL_Tree()
    root = Creation_Dummy_Tree(myTree)
    myTree.printInorder(root)
    myTree.update(root, 30, ["Raphael"], 15)
    myTree.update(root, 30, ["Bob"], 5)
    print()
    print ("Nouvelle version apres Update")
    print()
    myTree.printInorder(root)

def Test_Distribution_Game():
    myTree = AVL_Tree()
    distribution_game = Random_Games(myTree,2)
    
    i=1
    for game in distribution_game:
        print("Poule {} : ".format(i))
        print(game)
        print()
        i+=1

if __name__ == "__main__":
    #Test_Delete()
    #print()
    #Test_Update()
    Test_Distribution_Game()