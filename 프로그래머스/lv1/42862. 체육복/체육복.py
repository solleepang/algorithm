def solution(n, lost, reserve):
    answer = n - len(lost)
    res_len = sorted(reserve)
    lost_len = sorted(lost)
    
    for i in lost:
        if i in res_len and i in lost_len:
            lost_len.remove(i)
            res_len.remove(i)
            answer += 1
            
    for i in lost_len:
        if not res_len:
            break
        if i-1 in res_len:
            res_len.remove(i-1) 
            answer += 1
        elif i+1 in res_len:
            res_len.remove(i+1) 
            answer += 1
            
    return answer