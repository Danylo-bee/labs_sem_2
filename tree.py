from tree_balance import is_tree_balanced

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

rot = BinaryTree(3)
rot.left = BinaryTree(9)
rot.right = BinaryTree(20)

balanced_root = BinaryTree(1)
balanced_root.left = BinaryTree(2)
balanced_root.right = BinaryTree(3)
balanced_root.left.left = BinaryTree(4)
balanced_root.left.right = BinaryTree(5)
balanced_root.right.left = BinaryTree(6)
balanced_root.right.right = BinaryTree(7)

unbalanced_root = BinaryTree(1)
unbalanced_root.left = BinaryTree(2)
unbalanced_root.left.left = BinaryTree(3)
unbalanced_root.left.left.left = BinaryTree(4)


print("Balanced:",is_tree_balanced(rot))
print("Balanced:", is_tree_balanced(balanced_root))
print("Unbalanced:", is_tree_balanced(unbalanced_root))
