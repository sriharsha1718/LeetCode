class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        new_nums = sorted(nums[1:])
        cost += new_nums[0] + new_nums[1]
        return cost
        # Time Complexity: O(NlogN)
        # Space Complecity: O(N)
        