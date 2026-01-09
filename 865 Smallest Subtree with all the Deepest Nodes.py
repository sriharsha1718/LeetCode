class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using DFS to get the Level of each Node
        depth = { None : -1 }
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        # for i in depth:
        #     if i != None:
        #         print(i.val, 'Level:' , depth[i])
        max_depth = max(depth.values())

        def answer(node):
            if not node or depth.get(node) == max_depth:
                return node
            L = answer(node.left)
            R = answer(node.right)
            if L and R: return node
            if L: return L
            if R: return R
            return None
        return answer(root)
        # Time Complexity O(N)
        # Space Compexity O(N)