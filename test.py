from AVL_Class import AVL_Tree

# Driver program to test above function 
myTree = AVL_Tree() 
root = None
  
root = myTree.insert(root, 30, ["Bob"]) 
root = myTree.insert(root, 20, ["Markus"]) 
root = myTree.insert(root, 15, ["Vadim"]) 
root = myTree.insert(root, 50, ["Henry"]) 
root = myTree.insert(root, 10, ["Samuel"]) 
root = myTree.insert(root, 10, ["Vinhed"]) 
root = myTree.insert(root, 25, ["Pierre"])
root = myTree.insert(root, 30, ["Raphaël"])
root = myTree.delete(root, 30, ["Bob"])
root = myTree.delete(root, 30, ["Raphaël"])
myTree.printInorder(root)