"""
I did not write the code in this solution
It was copied from DeadPrince's
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solutions/5493561/beats-99-of-python-code

What's added: Explanation as comment
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def dfs(node):
            # the null base case
            if not node:
                return []
            
            # the useful base case
            # node is a leaf
            if not node.left and not node.right:
                # distance from the node
                # to its direct parent is 1
                return [1]

            # node is the LCA of all leaves below it
            # `left` holds the distances from each leaf
            #   on the left subtree to node
            # `right` holds the distances from each leaf
            #   on the right subtree to node
            left = dfs(node.left)
            right = dfs(node.right)

            # so, distance between two leaves, l1 and l2,
            # is the sum of
            # distance from l1 to node, and
            # distance from l2 to node
            for i in left:
                for j in right:
                    # we found a "good pair"
                    # when the sum satisfies the condition
                    # "less than or equal to distance"
                    if i + j <= distance:
                        self.ans += 1
            
            # we've done working with this node
            # combine the distances in `left` and `right`
            # and return it to the node's parent
            # the condition `i + 1 < distance` means
            # the leaf corresponding to that `i`
            # is still available for pairing
            # with a certain leaf on the other subtree of the parent
            return [i + 1 for i in left + right if i + 1 < distance]

        dfs(root)
        return self.ans
