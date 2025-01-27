"""Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]

Example 2:
Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Example 3:
Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]"""
class Solution(object):
    def sufficientSubset(self, root, limit):
        def reduce_tree(root, limit, curr_sum):
            if not root:
                return None
            
            l_sum = [curr_sum[0] + root.val]
            r_sum = [l_sum[0]]
            
            root.left = reduce_tree(root.left, limit, l_sum)
            root.right = reduce_tree(root.right, limit, r_sum)
            
            curr_sum[0] = max(l_sum[0], r_sum[0])
            if curr_sum[0] < limit:
                root = None
            return root
        curr_sum = [0]
        return reduce_tree(root, limit, curr_sum)
 
