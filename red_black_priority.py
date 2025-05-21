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

    def fix_insert(self, node):
        while node.parent and node.parent.color == "RED":
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                uncle = grandparent.right
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    grandparent.color = "RED"
                    node = grandparent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotare_left(node)
                    node.parent.color = "BLACK"
                    grandparent.color = "RED"
                    self.rotare_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    grandparent.color = "RED"
                    node = grandparent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotare_right(node)
                    node.parent.color = "BLACK"
                    grandparent.color = "RED"
                    self.rotare_left(grandparent)
        self.root.color = "BLACK"

    def rotare_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotare_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def extract_max(self):
        if not self.root:
            return None

        max_node = self.root
        while max_node.left:
            max_node = max_node.left

        result = self.del_node(max_node)

        return result

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

    def fix_del(self, node):
        while node != self.root and self.get_color(node) == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right
                if self.get_color(sibling) == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.rotare_left(node.parent)
                    sibling = node.parent.right
                if (self.get_color(sibling.left) == "BLACK" and self.get_color(sibling.right) == "BLACK"):
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if self.get_color(sibling.right) == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.rotare_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.rotare_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if self.get_color(sibling) == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.rotare_right(node.parent)
                    sibling = node.parent.left
                if (self.get_color(sibling.left) == "BLACK" and self.get_color(sibling.right) == "BLACK"):
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if self.get_color(sibling.left) == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.rotare_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.rotare_right(node.parent)
                    node = self.root

        node.color = "BLACK"

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
