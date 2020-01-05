class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return 'ListNode({})'.format(str(self.val))


def buildList(seq):
    # seq is a list of objects.
    f = ListNode(None)
    c = f
    for obj in seq:
        c.next = ListNode(obj)
        c = c.next
    h, f.next = f.next, None
    return h


def search_by_index(head, index):
    if head is None or index < 0:
        return None
    for move_times in range(index):
        head = head.next
        if head is None:
            return None
    return head


def add_to_index(head, index, value):
    if index == 0:
        new_head = ListNode(value)
        new_head.next = head
        return new_head
    else:
        preNode = search_by_index(head, index - 1)
        if preNode is None:
            return head
        new_node = ListNode(value)
        new_node.next = preNode.next
        preNode.next = new_node
        return head


h = buildList([1, 2, 3])
print(add_to_index(h, 2, 4))

head = h
for i in range(3):
    if i == 2:
        print(head.val)
    else:
        head = head.next

