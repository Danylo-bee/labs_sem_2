from math import sqrt

def max_wire_length(w, heights):
    n = len(heights)
    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        dist_00 = w
        dist_01 = sqrt(w**2 + (heights[i] - 1)**2)
        dist_10 = sqrt(w**2 + (1 - heights[i-1])**2)
        dist_11 = sqrt(w**2 + (heights[i] - heights[i-1])**2)

        dp[i][0] = max(
            dp[i-1][0] + dist_00,
            dp[i-1][1] + dist_10
        )

        dp[i][1] = max(
            dp[i-1][0] + dist_01,
            dp[i-1][1] + dist_11
        )

    return round(max(dp[n-1][0], dp[n-1][1]), 2)
