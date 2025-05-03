def is_tree_balanced(root):
    if root is None:
        return True

    q = [(root, False)]
    heights = {}

    while q:
        node, procesed = q.pop()

        if not node:
            continue

        if procesed:
            left_h = heights.get(node.left, 0)
            right_h = heights.get(node.right, 0)


            if abs(left_h - right_h) > 1:
                return False

            heights[node] = max(left_h, right_h) + 1
        else:
            q.append((node, True))
            q.append((node.right, False))
            q.append((node.left, False))
    return True
