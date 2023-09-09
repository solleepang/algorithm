from itertools import *

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    
    for i in arr:
        num = sum(i)
        if is_prime(num):
            answer += 1

    return answer