class Solution(object):
    def addNumber(self, l1, l2, l_res, cb):
        l_res.val = l1.val + l2.val + cb
        if l_res.val >= 10:
            cb = 1
            l_res.val = l_res.val % 10
        else:
            cb = 0
        return cb

    def addTwoNumbers(self, l1, l2):
        l_head = ListNode(0)
        return self.addTwoNumbersRecursion(l1, l2 ,l_head, l_head, 0)

    def addTwoNumbersRecursion(self, l1, l2, l_head, l_node, cb):
        cb = self.addNumber(l1, l2, l_node, cb)
        
        if (l1.next == None and l2.next == None):
            if cb == 1:
                l_next = addNextListNode(l_node, 1)
            return l_head

        l_next = addNextListNode(l_node, 0)
        if l1.next == None:
            addNextListNode(l1, 0)
        if l2.next == None:
            addNextListNode(l2, 0)
        return self.addTwoNumbersRecursion(l1.next, l2.next, l_head, l_next, cb)

def addNextListNode(l_node, x):
    l_next = ListNode(x)
    l_node.next = l_next
    return l_next