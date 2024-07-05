# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # start from the second node
        prev_val = head.val
        curr = head.next
        curr_idx, first_crit_idx, prev_crit_idx = 1, None, None

        # initalize resulting values
        # set `minDistance = float("inf")` to facilitate calculations
        minDistance, maxDistance = float("inf"), -1

        # traverse up to the second last node only
        while curr.next:
            # check critical point
            if (
                prev_val < curr.val > curr.next.val  # local maxima
                or prev_val > curr.val < curr.next.val  # local minima
            ):
                if first_crit_idx is None:
                    # first critical point
                    # keep track and do nothing
                    first_crit_idx = curr_idx
                else:
                    # second critical point onwards
                    # update the resulting values
                    minDistance = min(curr_idx - prev_crit_idx, minDistance)
                    maxDistance = curr_idx - first_crit_idx
                # update index of the previous critical point for later calculation
                prev_crit_idx = curr_idx
            # move to the next node
            prev_val = curr.val
            curr = curr.next
            curr_idx += 1
        return [-1 if minDistance == float("inf") else minDistance, maxDistance]
