class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # We will use two pass Depth First Search (DFS) one to caculate the total sum of all elements
        # Another to calcuate the sum of elements in the subtree
        # We will use the Recursion technique
        all_sums = []
        def tree_sum(node):
            if node is None:
                return 0
            s = node.val + tree_sum(node.left) + tree_sum(node.right)
            all_sums.append(s)
            return s

        total_sum = tree_sum(root)
        best = 0
        for s in all_sums:
            best = max(best, s * (total_sum-s))
        return best % (10**9 + 7)
        # Time Complexity: O(n)
          # We visit every node once to calculate sums
          # We iterate thru the list of sums once
          # Recursive stack depth
        # Space Complexity: O(n)
          # List storing N sums