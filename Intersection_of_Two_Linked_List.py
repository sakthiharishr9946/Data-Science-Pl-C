class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lena = self.length(headA)
        lenb = self.length(headB)

        while lena > lenb:
            headA = headA.next
            lena -= 1

        while lenb > lena:
            headB = headB.next
            lenb -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def length(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l


common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

obj = Solution()
intersection = obj.getIntersectionNode(headA, headB)

if intersection:
    print(intersection.val)
else:
    print(None)