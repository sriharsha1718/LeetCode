class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            val = -1
            for i in range(1, num):
                if (i | (i+1)) == num:
                    val = i
                    break
            ans.append(val)
            
        return ans
        # Time Compexity O(nm)
        # Space Complexity O(n)