# Single Loop Leet Code Daily
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        print(arr)
        min_diff = float('inf')
        result = []
        for i in range(len(arr) - 1):
            curr_diff = (arr[i+1] - arr[i])

            if curr_diff < min_diff:
                min_diff = curr_diff
                result = [[arr[i], arr[i+1]]]
            
            elif curr_diff == min_diff:
                result.append([arr[i], arr[i+1]])

        return result
        # Time Complexity: O(N Log N) because of sort()
        # Space Complexity: O(N) because of auxilary space of sort()        

        

# My Approach on basis of yest sliding window problem
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        print(arr)
        min_diff = float('inf')
        for i in range(len(arr) - 2 + 1):
            if (arr[i+1] - arr[i]) < min_diff:
                min_diff = (arr[i+1] - arr[i])

        print(min_diff)
        result = []
        for i in range(len(arr) - 2 + 1):
            if (arr[i+1] - arr[i]) == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
        # Time Complexity: O(N Log N) because of sort()
        # Space Complexity: O(N) because of auxilary space of sort()        