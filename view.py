from red_black_priority_queue import RedBlackTreePriorityQueue

posts = RedBlackTreePriorityQueue()

while True:
    command = input("Введіть команду (add, search, update, quit): ")

    if command == "add":
        res_1 = str(input("Введіть пост: "))
        res_2 = int(input("Введіть кількість переглядів: "))
        posts.insert(res_1, res_2)
        print("Пост додано. Поточна черга:")
        print(posts.view_queue())

    elif command == "search":
        search_priority = int(input("Введіть кількість переглядів для пошуку: "))
        found = False
        for value, priority in posts.view_queue():
            if priority == search_priority:
                print(f"Знайдено пост: '{value}', перегляди: {priority}")
                found = True
                break
        if not found:
            print("Пост з таким пріоритетом (переглядами) не знайдено.")

    elif command == "update":
        old_priority = int(input("Введіть стару кількість переглядів: "))
        new_priority = int(input("Введіть нову кількість переглядів: "))

        def find_node_by_priority(node):
            if not node:
                return None
            if node.priority == old_priority:
                return node
            elif old_priority < node.priority:
                return find_node_by_priority(node.left)
            else:
                return find_node_by_priority(node.right)

        node_to_update = find_node_by_priority(posts.root)
        if node_to_update:
            value = node_to_update.value
            posts.insert(value, new_priority)
            posts.del_node(node_to_update)
            print("Оновлено. Поточна черга:")
            print(posts.view_queue())
        else:
            print("Пост з таким пріоритетом не знайдено для оновлення.")

    elif command == "quit":
        break
