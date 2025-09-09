# Structure of a Binary Tree Node
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Function to print preorder traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
    
printPreorder(root)