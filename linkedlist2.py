class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def buildList(seq):
    f = ListNode(None)
    c=f
    for obj in seq:
        c.next = ListNode(obj)
        c= c.next
    h = f.next
    f.next = None
    return h

#Iterative solution to reversing a linked list

# def reverse(head):
#     prev = None
#     curr = head
#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev


#Recursive solution to reversing a linked list

def reverseList(head):
    if not head or not head.next:
        return head
    h =reverseList(head.next)
    head.next.next = head
    head.next = None
    return h

h=buildList([1,2,3,4])
h=reverseList(h)
while h:
    print (h.val)
    h = h.next

