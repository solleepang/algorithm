# def solution(x, n):

#     if x == 0:
#         return [0]*n
#     else:
#         return [i for i in range(x,(n*x-1 if x < 0 else n*x+1),x)]
    
def solution(x, n):
    if x == 0:
        answer = [0]*n
    else:
        answer = list(range(x, (n+1)*x, x))
    return answer