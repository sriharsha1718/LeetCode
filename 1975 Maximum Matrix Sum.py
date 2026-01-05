class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # If even negative elements we can make all positive
        # If odd negative elements we ca n make all positive but one so we take min element
        # Calculate the sum of absolute values of all elements
        # Count the total number of negative elements
        # Track the minimum absolute value in the grid
        # Adjust the sum if the count of negative value is odd
        total_sum = 0
        negative = 0
        min_value = float('inf')
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative += 1
                min_value = min(min_value, abs(val))
        if negative % 2 != 0:
            total_sum = total_sum - (2*abs(min_value))
        return total_sum

        # Time Complexirt O(n * m)
        # Space Complexity O(1)