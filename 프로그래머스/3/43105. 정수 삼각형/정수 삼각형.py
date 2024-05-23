def solution(triangle):
    answer = 0
    h = len(triangle)
    dp = [[0 for i in range(h)] for i in range(h)]
    dp[0][0] = triangle[0][0]
    for i in range(1,h):
        nums = len(triangle[i])
        for j in range(nums):
            if i ==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else :
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    answer = max(dp[h-1])
    return answer