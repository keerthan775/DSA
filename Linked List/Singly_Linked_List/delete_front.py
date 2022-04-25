def delete_front(linked_list):
    if not linked_list:
        print('There is no element to delete')
    elif not linked_list.next:
        print("deleted element is ", linked_list.data)
        linked_list = None
    else:
        temp1 = linked_list
        temp2 = linked_list.next
        print("deleted element is ", temp1.data)
        linked_list = temp2
    linked_list = linked_list
    return linked_list
