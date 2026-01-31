class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        max = target
        for i in letters:
            if i > max:
                max = i
                return max
        if max == target:
            return letters[0]
        # Time Complexity: O(N)
        # Space Compexity: O(1)