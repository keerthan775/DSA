from .linked_list import Node

def insert_front(l):
    if not l:
        print("No data")
        return []
    elif len(l) == 1:
        return Node(l[0])
    else:
        linked_list = Node(l[0])
        temp = linked_list
        for i in l[1:]:
            node = Node(i)
            node.next = temp
            temp = node
        linked_list = temp
        return linked_list

