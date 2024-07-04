# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()

        curr = head  # traversal pointer
        res_curr = res_head  # resulting pointer
        while curr.next:
            # `curr.val == 0` marks the beginning of a sub-list
            if curr.val == 0:
                # `res_curr.val != 0` means
                # we've done summing nodes in the previous sub-list
                # and res_curr.val holds that sum
                # now we initilize and move to the next resulting pointer
                if res_curr.val != 0:
                    res_curr.next = ListNode()
                    res_curr = res_curr.next
            else:
                # we are inside a sub-list
                # just add the value of the current node
                # to the sum held by `res_curr.val`
                res_curr.val += curr.val
            curr = curr.next

        return res_head
