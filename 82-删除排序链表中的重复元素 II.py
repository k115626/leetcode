# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            # head 是第一个节点，定义一个虚拟节点，让其的next指向head节点
            # 定义虚拟节点
            dummy = ListNode(0, head)
            if dummy.next is None:
                return head
            # 循环开始时，当前的节点是虚拟节点
            curr = dummy
            while curr.next and curr.next.next:
                if curr.next.val == curr.next.next.val:
                    val = curr.next.val
                    # 每次判断.next指向的这个值是不是重复值
                    while curr.next and curr.next.val == val:
                        curr.next = curr.next.next
                else:
                    curr = curr.next
            return dummy.next
            
