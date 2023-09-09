from itertools import *

def solution(numbers):
    comb = list(combinations(numbers,2))
    answer = sorted(set([sum(i) for i in comb]))
    return answer