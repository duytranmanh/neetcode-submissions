# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #dfs for all:
        def dfs(root, target, path):
            if not root:
                return None

            if root.val == target.val:
                path.append(target)
                return path
            
            l_path = dfs(root.left, target, path + [root])
            if l_path != None:
                return l_path
            r_path = dfs(root.right, target, path + [root])
            if r_path != None:
                return r_path

        p_path = dfs(root, p, [])
        q_path = dfs(root, q, [])

        print([i.val for i in p_path])
        print([i.val for i in q_path])

        for i in range(max(len(p_path), len(q_path))):
            if i >= len(p_path):
                return q_path[i - 1]
            if i >= len(q_path):
                return p_path[i - 1]

            if p_path[i] != q_path[i]:
                return p_path[i -1]
        
