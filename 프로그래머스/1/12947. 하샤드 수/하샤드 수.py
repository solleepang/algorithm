def solution(x):
    
    num = 0
    num_str = str(x)
    for i in num_str:
        num += int(i)
    
    return False if x%num else True