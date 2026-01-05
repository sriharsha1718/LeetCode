class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            sum = 0
            count = 0
            for i in range(1, int(num**0.5)+1):
                if num % i == 0:
                    count = count + 1
                    sum = sum + i 
                    # Handling the perfect square case 
                    # Number which is a perfect square but still have 4 divisors
                    if i*i != num:
                        count = count + 1
                        sum = sum + int(num / i)

                if count > 4:
                    break
            if count == 4:
                total_sum = total_sum + sum
        return total_sum
                
# Time complexity of O(n √m)
# Space complexity of O(1)
