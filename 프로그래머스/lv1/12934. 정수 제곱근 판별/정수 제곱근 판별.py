def solution(n):
    num = n ** 0.5
    return (num+1)**2 if not num % 1 else -1