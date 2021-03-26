"""

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     """
    #     当前节点的值和下一个节点的值相等时，
    #     则当前节点的next指向next.next
    #     """
    #     dummy = ListNode(0, head)
    #     if dummy.next is None:
    #         return head
    #     curr = dummy.next
    #     while curr.next:
    #         if curr.val == curr.next.val:
    #             val = curr.val
    #             while curr.next and curr.next.val == val:
    #                 curr.next = curr.next.next
    #         else:
    #             curr = curr.next
    #     return dummy.next


