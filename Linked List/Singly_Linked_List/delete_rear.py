def delete_rear(linked_list):
    if not linked_list:
        print('There is no element to delete')
    elif not linked_list.next:
        print("deleted element is ", linked_list.data)
        linked_list = None
    else:
        temp = linked_list
        while(temp):
            if not temp.next.next:
                print("deleted element is ", temp.next.data, temp.next)
                temp.next = None
                break
            temp = temp.next
    linked_list = linked_list
    return linked_list