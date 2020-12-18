from Node_Class import Node
import random

class AVL_Tree:

    '''
    #* Class used as AVL Tree

    #? liste_joueurs_score : List containing for each player, another list composed of his name and his score
    '''
    def __init__(self):
        self.liste_joueurs_score = []

    '''
    #* Function allowing the insertion of a new node in the AVL, indeed it is the root variable which will really contain the data
    #* The AVL class guarantees the AVL nature of root via the various functions defined in it

    #? root : Root of the AVL containing all its child nodes
    #? score : player score
    #? joueur : the name of the player to insert
    '''
    def insert(self, root, score, joueur): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            self.liste_joueurs_score.append([joueur,score])
            return Node([joueur],score) 
        elif score < root.score: 
            root.left = self.insert(root.left, score, joueur) 
        elif score > root.score: 
            root.right = self.insert(root.right, score, joueur) 
        else:
            # Same score
            self.liste_joueurs_score.append([joueur,score])
            root.liste_joueurs_node.append(joueur)
            return root
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
         
        if balance > 1 and score < root.left.score: 
            return self.rightRotate(root) 
  
         
        if balance < -1 and score > root.right.score: 
            return self.leftRotate(root) 
  
         
        if balance > 1 and score > root.left.score: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
         
        if balance < -1 and score < root.right.score: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 


    '''
    #* Function allowing the deletion of a node in the AVL
    #* The data is actually in root, we will delete a node in root
    #* We are also removing the player in question from the AVL Tree player list.

    #! This function is not recursive and is surely not optimized because here we make a copy of our AVL Tree without adding the element to remove
    #! We had to do this because we were having issues with the basic recursive function to delete a node
    #! As a matter of fact, by integrating a list for each node (essential for players with the same score), many problems were generated
    #! when we wanted to recursively delete

    #? nom_joueur : the name of the player to insert
    '''
    def delete(self, nom_joueur): #don't need the score because we already have it in the list of players
        #Creation of the copies
        root_after_deletion = None
        myTree_after_deletion = AVL_Tree()
        for joueur_score in self.liste_joueurs_score:
            if (joueur_score[0] != nom_joueur): #If the player we are currently looking at is the same as the one we want to delete, we don't insert him in the copy
                root_after_deletion = myTree_after_deletion.insert(root_after_deletion,joueur_score[1],joueur_score[0])
        return (myTree_after_deletion,root_after_deletion)
        
        
    '''
    #* Function allowing to update the player score
    #* We will update the value in root to have an up-to-date node but also in the list of players of the AVL Tree

    #? root: Root of the AVL containing all its child nodes
    #? nom_joueur: the name of the player we want to update
    #? new_score: new score to assign to the player we have put in parameter
    '''
    def update(self, root, nom_joueur, new_score):
        self,root = self.delete(nom_joueur)
        root = self.insert(root, new_score, nom_joueur)
        return self,root


    '''
    #* Function allowing to get the node with the smallest value from the node we are in
    #* Used in some cases when we want to delete a node

    #? root: node of the AVL Tree containing all of its child nodes
    '''
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 


    '''
    #* Function allowing to make a left rotation for the AVL Tree (root)

    #? z: AVL Tree node (root) with all its child nodes
    '''
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    
    '''
    #* Function allowing to make a right rotation for the AVL Tree (root)

    #? z: AVL Tree node (root) with all its child nodes
    '''
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  

    '''
    #* Function allowing to get the height of a node of the AVL Tree (root)

    #? root: node of the AVL Tree with all its child nodes
    '''
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  

    '''
    #* Function allowing to obtain the balance of a node from a node of the AVL Tree (root)
    #* To know if we should perform a rotation and if so, know which one to perform

    #? root: node of the AVL Tree with all its child nodes
    '''
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  

    '''
    #* Function allowing to print nodes with the 'In Order' method

    #? root: Root of the AVL containing all its child nodes
    '''
    def printInorder(self,root): 
        if root: 
    
            # First recur on left child 
            self.printInorder(root.left) 
    
            # then print the data of node 
            print("Score : {} ; Player List : {}".format(root.score, root.liste_joueurs_node)) 
    
            # now recur on right child 
            self.printInorder(root.right)
            

    '''
    #* Function allowing to fill a list with the 'In Order' method
    #* This list will therefore contain all the players of the AVL Tree (root) ranked from worst to best
    #* Each index of this list will be a list composed of the name of the player and his score

    #? root: Root of the AVL containing all its child nodes
    #? list: list of players (to be declared empty before using this function)
    '''
    def ListInorder(self,root, liste_joueurs_inOrder): 
        if root: 
    
            # First recur on left child 
            self.ListInorder(root.left, liste_joueurs_inOrder) 
    
            #This for loop is necessary because if some players have the same score, we have to append all of them in the list 
            for player in root.liste_joueurs_node:
                liste_joueurs_inOrder.append([player,root.score])
    
            # now recur on right child 
            self.ListInorder(root.right, liste_joueurs_inOrder)

    
    '''
    #* Function allowing to fill a list with the 'In Order' 
    #* This list will therefore contain all the players of the AVL Tree (root) ranked from worst to best
    #* Each index of this list will be a list composed of a list of players name and a score

    #? root: Root of the AVL containing all its child nodes
    #? list: list of players (to be declared empty before using this function)
    '''
    def ListInorder_For_Ties(self,root, liste_joueurs_inOrder): 
        if root: 
    
            # First recur on left child 
            self.ListInorder_For_Ties(root.left, liste_joueurs_inOrder) 
    
            #Here we append the list of all the players having the same score and their score to deal with the case where some players are tied when dropping players or doing the podium
            liste_joueurs_inOrder.append([root.liste_joueurs_node,root.score])
    
            # now recur on right child 
            self.ListInorder_For_Ties(root.right, liste_joueurs_inOrder)