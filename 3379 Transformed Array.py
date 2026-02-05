class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            index = (i + nums[i]) % n
            result.append(nums[index])
        return result
        # Time Complexity: O(N)
        # Space Complexity: O(N) 