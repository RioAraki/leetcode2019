class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# loop through the ll to get length
# let k < length of ll
# function to turn right ll by 1, execute k times
def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return []
    if not head.next:
        return head

    def getLen(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    count = k % getLen(head)

    def rotateOne(head):
        tmp = dum = head
        while dum.next.next:
            dum = dum.next
        head = dum.next
        dum.next = None
        head.next = tmp
        return head

    for i in range(count):
        head = rotateOne(head)

    return head

def betterRotateRight(self, head, k):

    # similar idea here, get length and decrement k

    if not head:
        return None

    if head.next == None:
        return head

    pointer = head
    length = 1

    while pointer.next:
        pointer = pointer.next
        length += 1

    rotateTimes = k % length

    if k == 0 or rotateTimes == 0:
        return head

    # use two pointers, fast one would go through to the end while slow one would go forward len - k times

    fastPointer = head
    slowPointer = head

    for a in range(rotateTimes):
        fastPointer = fastPointer.next

    while fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next

    temp = slowPointer.next

    slowPointer.next = None
    fastPointer.next = head
    head = temp

    return head


#2019-09-03 redo:
# one loop to count the length of linked list, at the end of the ll, link it to the head
# find the tail since we know the length, set the tail's next to none. tail's next is the new head.

def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    
    
    
    # corner case
    if not head:
        return head
    
    start = head
    length = 1
    while head.next:
        length += 1
        head = head.next
        
    if k % length == 0:
        return start
    
    head.next = start
    
    
    
    tail = (length - k) % length
    cur = 1
    while cur < tail:
        start = start.next
        cur += 1
    ret = start.next
    start.next = None
    
    return ret
    
    
        