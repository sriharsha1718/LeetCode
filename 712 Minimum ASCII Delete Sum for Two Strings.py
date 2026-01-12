class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Dynamic programming
        m, n = len(s1), len(s2)
        print(m, n)

        dp = [[0] * (n+1) for i in range(m+1)]
        print(dp)

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        # for row in dp:
        #     print(" ".join(map(str, row)))

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        # print()
        # for row in dp:
        #     print(" ".join(map(str, row)))

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),
                                   dp[i][j-1] + ord(s2[j-1])
                    )
        # print()
        # for row in dp:
        #     print(" ".join(map(str, row)))

        return dp[m][n]
        # Time Complexity: O(MN)
        # Space Compexity: O(MN)
        