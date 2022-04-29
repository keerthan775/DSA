class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_list(linked_list):
    temp = linked_list
    l = []
    while temp:
        l.append(temp.data)
        temp = temp.right
    return l
