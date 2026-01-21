class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums
        # Time Complexity: O(N Log M)
        # The algorithm runs in O(N log M) time because it processes N numbers and checks up to log M bits for each number, where M is the maximum value in the array.
        # Space Complexity: O(1)
        