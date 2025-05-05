class Node:
    def __init__(self, value = None, priority = None):
        self.value = value
        self.priority = priority
        self.color = "RED"
        self.right = None
        self.left = None
        self.parent = None
    def __repr__(self):
        return f"Node(value={self.value}, priority={self.priority})"

class RedBlackTreePriorityQueue:
    def __init__(self,):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
            self.root.color = "BLACK"
            return

        parent = None
        current = self.root

        while current:
            parent = current
            if new_node.priority < current.priority:
                current = current.right
            else:
                current = current.left

        new_node.parent = parent
        if new_node.priority < parent.priority:
            parent.right = new_node
        else:
            parent.left = new_node

        self.fix_insert(new_node)

    def del_node(self, node):
        if node.left and node.right:
            sucsesor = self.min_value_node(node.right)
            node.value, node.priority = sucsesor.value, sucsesor.priority
            node = sucsesor
        child = node.left if node.left else node.right
        if child:
            child.parent = node.parent
            if not node.parent:
                self.root = child
            elif node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child

            if node.color == "BLACK":
                self.fix_del(child)
        else:
            if node.color == "BLACK":
                self.fix_del(node)
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None

        return (node.value, node.priority)

    def get_color(self, node):
        return node.color if node else "BLACK"

    def min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def view_queue(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append((node.value, node.priority))
            self.inorder_traversal(node.right, result)
