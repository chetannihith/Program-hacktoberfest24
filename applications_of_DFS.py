# Applications of Depth-First Search (DFS)

"""
Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as deeply as possible along each branch before backtracking. Here are some key applications of DFS:

1. **Topological Sorting**: Determines the order of tasks in a directed acyclic graph (DAG).
2. **Strongly Connected Components**: Identifies strongly connected components in directed graphs.
3. **Cycle Detection**: Detects cycles within a graph.
4. **Maze Solving**: Finds paths through mazes or labyrinths.
5. **Game Theory**: Explores game trees to find optimal strategies.
6. **Search Algorithms**: Used in AI for solving puzzles or planning routes.
7. **Decision Trees**: Assists in building classification models.
8. **Network Analysis**: Explores networks to identify connected components.
9. **Web Crawling**: Used to crawl websites and index pages.
10. **Robotics**: Plans paths for robots in complex environments.

Now, let's look at the implementation of DFS through a binary tree with pre-order, in-order, and post-order traversals.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    root = TreeNode(1)
    nodeA = TreeNode(2)
    nodeB = TreeNode(3)
    nodeC = TreeNode(4)
    nodeD = TreeNode(5)
    nodeE = TreeNode(6)
    nodeF = TreeNode(7)

    root.left = nodeA
    root.right = nodeB
    nodeA.left = nodeC
    nodeA.right = nodeD
    nodeB.left = nodeE
    nodeB.right = nodeF

    return root

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

# Create the tree and demonstrate DFS traversals
if __name__ == "__main__":
    root = create_tree()
    
    print("Pre-order Traversal:")
    preorder(root)
    print("\nIn-order Traversal:")
    inorder(root)
    print("\nPost-order Traversal:")
    postorder(root)
