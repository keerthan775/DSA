from linked_list import Node

def insert_rear(l):
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
            temp.next = node
            temp = temp.next
        return linked_list
