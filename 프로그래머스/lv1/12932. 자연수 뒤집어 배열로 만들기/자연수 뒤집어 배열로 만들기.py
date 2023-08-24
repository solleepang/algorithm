def solution(n):
    answer = []
    
    for i in range(1,len(str(n))+1):
        num = n % 10
        n = n // 10
        answer.append(num)
                   
    return answer