def solution(arr, divisor):
    answer = []
    count = 0
    for i in arr:
        if not i % divisor:
            answer.append(i)
            count += 1
            
    if not count:
        answer.append(-1)
        
    answer.sort()
    return answer