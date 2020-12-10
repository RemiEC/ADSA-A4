from Node_Class import Node
import random
class AVL_Tree:


    def __init__(self):
        self.liste_joueurs = []

    def insert(self, root, score, player): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            self.liste_joueurs.append(player[0])
            return Node(player,score) 
        elif score < root.score: 
            root.left = self.insert(root.left, score, player) 
        elif score > root.score: 
            root.right = self.insert(root.right, score, player) 
        else:
            # Same score
            self.liste_joueurs.append(player[0])
            root.list_player.append(player[0])
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
  
    def delete(self, root, score, player): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif score < root.score: 
            root.left = self.delete(root.left, score, player) 
  
        elif score > root.score: 
            root.right = self.delete(root.right, score, player) 
  
        else: 
            if(len(root.list_player) == 1):
                if root.left is None: 
                    temp = root.right 
                    root = None
                    return temp 

                elif root.right is None: 
                    temp = root.left 
                    root = None
                    return temp 

                self.liste_joueurs.remove(root.list_player[0])
                temp = self.getMinValueNode(root.right) 
                root.score = temp.score
                root.list_player = temp.list_player 
                root.right = self.delete(root.right, 
                                        temp.score, temp.list_player) 
            else : 
                self.liste_joueurs.remove(player[0])
                root.list_player.remove(player[0])

        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 

        
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root
    
    def update(self, root, old_score, player_name, new_score):
        root = self.delete(root, old_score, player_name)
        root = self.insert(root, new_score, player_name)
        return root

    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 

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
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def printInorder(self,root): 
        if root: 
    
            # First recur on left child 
            self.printInorder(root.left) 
    
            # then print the data of node 
            print("Score : {} ; Player List : {}".format(root.score, root.list_player)) 
    
            # now recur on right child 
            self.printInorder(root.right)
    def ListInorder(self,root, liste): 
        if root: 
    
            # First recur on left child 
            self.ListInorder(root.left, liste) 
    
            # then print the data of node 
            for player in root.list_player:
                liste.append(player)
    
            # now recur on right child 
            self.ListInorder(root.right, liste)

          