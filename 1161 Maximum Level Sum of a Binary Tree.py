class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # We will use Breadth First Search (BFS) to solve this problem
        # We need to find the maximum sum and there can be neg node values so we take -inf
        q = deque()
        q.append(root)

        max_sum = float('-inf')
        max_sum_level = 0
        current_level = 0

        while q:
            current_level += 1
            curr_total_sum = 0
            for i in range(len(q)):
                node = q.popleft() 
                curr_total_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < curr_total_sum:
                max_sum = curr_total_sum
                max_sum_level = current_level

        return max_sum_level

        # Time Complexity O(n)
        # Space Complexity O(n) The deque can hold up to max width of tree approx (N/2)