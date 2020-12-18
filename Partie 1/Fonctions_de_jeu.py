from AVL_Class import *
import random

'''
#* Function allowing to create an AVL Tree with some arbitrary data

#? myTree : AVL Tree just created
'''
def Creation_Dummy_Tree(myTree):
    root = None
    root = myTree.insert(root, 30, "Bob") 
    root = myTree.insert(root, 20, "Markus") 
    root = myTree.insert(root, 15, "Vadim") 
    root = myTree.insert(root, 50, "Yao") 
    root = myTree.insert(root, 50, "Henry") 
    root = myTree.insert(root, 10, "Samuel") 
    root = myTree.insert(root, 10, "Vinhed") 
    root = myTree.insert(root, 25, "Pierre")
    root = myTree.insert(root, 30, "Raphael")
    return root


'''
#* Function allowing to create an AVL Tree to begin the competition (the score of each player is 0)

#? myTree : AVL Tree just created
'''
def Creation_Tree_Beggining_Competition(myTree):
    root = None
    root = myTree.insert(root, 0, "Bob") 
    root = myTree.insert(root, 0, "Markus") 
    root = myTree.insert(root, 0, "Vadim") 
    root = myTree.insert(root, 0, "Yao") 
    root = myTree.insert(root, 0, "Henry") 
    root = myTree.insert(root, 0, "Samuel") 
    root = myTree.insert(root, 0, "Vinhed") 
    root = myTree.insert(root, 0, "Pierre")
    root = myTree.insert(root, 0, "Raphael")
    root = myTree.insert(root, 0, "Patrick")
    root = myTree.insert(root, 0, "Carlos")
    root = myTree.insert(root, 0, "Alex")
    return root


'''
#* Function allowing to create random games (each player in a game has been picked randomly regardless his score)

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
'''
def Random_Games(root,myTree, nb_joueur_par_game):
    #As we will remove players from this list, we make a copy of it so that the original is not altered
    liste_joueurs_score = myTree.liste_joueurs_score.copy()
    nb_games = int(len(liste_joueurs_score)/nb_joueur_par_game)
    
    liste_all_games = [] #List in which we will have all the game 
    for i in range(nb_games):
        liste_current_game = [] #List in which we will have all the players for the game we are currently creating
        for j in range (nb_joueur_par_game):
            #We select a player randomly
            joueur_score_random = random.choice(liste_joueurs_score)
            #We add him in the game
            liste_current_game.append(joueur_score_random)
            #We remove him from the list containing all the players so that we don't pick him again 
            liste_joueurs_score.remove(joueur_score_random)
        #We append this game in the list of games
        liste_all_games.append(liste_current_game) 
    return liste_all_games


'''
#* Function allowing to create ranked games (each player in a game has been picked in function of his score)

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
'''
def Ranked_Games(root,myTree, nb_joueur_par_game):
    liste_joueurs_score_ranked = [] #Will be modified in the function used below
    myTree.ListInorder(root, liste_joueurs_score_ranked)
    nb_games = int(len(myTree.liste_joueurs_score)/nb_joueur_par_game)

    liste_all_games = [] #List in which we will have all the game 
    for i in range(nb_games):
        liste_current_game = [] #List in which we will have all the players for the game we are currently creating
        for j in range (nb_joueur_par_game):
            #We add him in the game
            liste_current_game.append(liste_joueurs_score_ranked[0])
            #We remove him from the list containing all the players so that we don't pick him again 
            liste_joueurs_score_ranked.remove(liste_joueurs_score_ranked[0])
        #We append this game in the list of games
        liste_all_games.append(liste_current_game)

    return liste_all_games


'''
#* Function allowing to return a random number between 0 and 12
#* We use it to define the score of a player 
'''
def Random_Score():
    return random.choice(range(13))


'''
#* Function allowing to attribute a random score to each player in each game

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? liste_all_games : list containing all the games for which each index is a list containing of all the players in this game (all the players are represented by their name and their score)
'''
def Random_Score_Distribution(root, myTree, liste_all_games):
    for game in liste_all_games: #We go through the list of games 
        for joueur_score in game: #We go through all the players in the game we are looking at in order to update their score
            old_score = joueur_score[1]
            new_score = Random_Score() + old_score
            player_name = joueur_score[0]
            myTree,root = myTree.update(root,player_name,new_score)
    return myTree,root


'''
#* Function allowing to create a round

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
#? random_games : boolean that inform if we want to have a random game (True) or ranked games (False)
'''
def Round(root, myTree, nb_joueur_par_game,random_games= False):
    if(random_games):
        liste_all_games = Random_Games(root,myTree, nb_joueur_par_game)
    else:
        liste_all_games = Ranked_Games(root,myTree, nb_joueur_par_game)
    #We update the tree and the root with the values we will modify in Ramdom_Score_Distribution
    myTree,root = Random_Score_Distribution(root, myTree, liste_all_games)
    return myTree,root


'''
#* Function allowing to drop the X worst players

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_worst_players_to_drop : number of players that we want to drop
'''
def Drop_Worst(root, myTree, nb_worst_players_to_drop):
    classement = [] #Will be modified in the function used below
    myTree.ListInorder_For_Ties(root, classement)
    players_to_be_deleted = []
    for liste_players_score in classement: #We will drop the X first players
        while(len(liste_players_score[0]) > 0 and nb_worst_players_to_drop > 0): # there is no more players that have this score or no more players to drop so we can go out of the loop
            index_player_to_delete = random.choice(range(len(liste_players_score[0]))) #If some players have the same score, we select one of them randomly
            players_to_be_deleted.append(liste_players_score[0][index_player_to_delete])
            liste_players_score[0].remove(liste_players_score[0][index_player_to_delete])
            nb_worst_players_to_drop-=1

        if (nb_worst_players_to_drop == 0): # Break again as there are no more players to drop
            break

    for player_name in players_to_be_deleted: #We go through this list and we delete each player in the AVL Tree
        myTree,root = myTree.delete(player_name)
    return myTree,root


'''
#* Function allowing to play until the desired number of players remains

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
#? nb_worst_players_to_drop : number of worst players that we want to drop after each game
'''
def Jeu_Avant_Finalistes(root, myTree,nb_joueur_par_game, taille_top, nb_worst_players_to_drop):
    nb_de_manches_ranked = int((len(myTree.liste_joueurs_score) - taille_top) / nb_worst_players_to_drop)
    print("Debut de competition !")
    print()
    #We do the first 3 ramdom games
    for i in range(3):
        myTree,root = Round(root, myTree, nb_joueur_par_game, random_games = True)
        print("Resultats game random n{}:".format(i+1))
        myTree.printInorder(root)
        print()
    #We do the needed number a ranked games
    for j in range(nb_de_manches_ranked):
        myTree,root = Round(root, myTree, nb_joueur_par_game)
        print("Resultats game ranked n{}:".format(j+1))
        myTree.printInorder(root)
        myTree,root = Drop_Worst(root, myTree, nb_worst_players_to_drop)
        print()
        print("Joueurs restants:".format(j+1))
        liste_joueurs_score_restants = myTree.liste_joueurs_score
        msg = ""
        for joueur_score in liste_joueurs_score_restants:
            msg += " {} ".format(joueur_score[0])
        print(msg)
        print()
    return myTree,root


'''
#* Function allowing to play the finals

#? root : Root of the AVL containing all its child nodes
#? myTree : AVL Tree declared before
#? nb_joueur_par_game : number of players in a game
'''
def Jeu_Finalistes(root, myTree,nb_joueur_par_game):
    print("TOP {} PLAYERS".format(nb_joueur_par_game))
    liste_finalistes = myTree.liste_joueurs_score.copy() #As we will update players from this list, we make a copy of it so that the original is not altered
    for joueur_score in liste_finalistes:
        print(joueur_score[0])
        # Reset score of each player
        myTree,root = myTree.update(root,joueur_score[0],0)
    print()
    # We do the 5 ranked games
    for i in range(5):
        myTree,root = Round(root, myTree, nb_joueur_par_game)
        print("Resultats game finalistes n{}:".format(i+1))
        myTree.printInorder(root)
        print()
    # We select the players for the podium
    classement = [] #Will be modified in the function used below
    myTree.ListInorder_For_Ties(root, classement)
    classement = classement[::-1] # We inverse the list as it's an InOrder list, the best players are at the end and we want them at the beginning to be easier to go through
    winners = []
    nb_winners = 3
    for liste_players_score in classement: #We will add the top 3 players (podium) the winners list
        while(len(liste_players_score[0]) > 0 and nb_winners > 0): # there is no more players that have this score or no more players to add to the podium
            index_winner = random.choice(range(len(liste_players_score[0]))) #If some players have the same score, we select one of them randomly
            winners.append([liste_players_score[0][index_winner],liste_players_score[1]])
            liste_players_score[0].remove(liste_players_score[0][index_winner])
            nb_winners-=1

        if (nb_winners == 0): # Break again as there are no more players to add to the podium
            break
    print("PODIUM")
    print("TOP 3 : {} avec {} points".format(winners[2][0],winners[2][1]))
    print("TOP 2 : {} avec {} points".format(winners[1][0],winners[1][1]))
    print("TOP 1 : {} avec {} points".format(winners[0][0],winners[0][1]))
