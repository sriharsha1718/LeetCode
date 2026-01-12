class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Chebyshev distance (or L∞ metric) measures the distance between two points as the maximum absolute difference along any single coordinate dimension
        ans = 0
        for i in range(len(points)-1):
            cur_x, cur_y = points[i]
            next_x, next_y = points[i+1]
            dist = max(abs(cur_x - next_x), abs(cur_y - next_y))
            ans += dist
        return ans
        # Time Complexity: O(N)
          # We iterate thru the List of size N
        # Space Complexity: O(1)
          # We only use variable ans and no additional data structure