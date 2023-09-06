from itertools import *

def solution(t, p):
    answer = 0
    num = len(p)
    for i in range(len(t)-num+1):
        if t[i:i+num] <= p:
            answer += 1
    return answer


#     for j in t_list:
#         t = ''.join(j)
        
#         if t <= p:
#             answer += 1
#     return answer