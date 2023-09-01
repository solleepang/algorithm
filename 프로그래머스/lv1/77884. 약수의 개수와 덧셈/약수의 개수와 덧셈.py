def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        count = 0
        for i in range(1,num+1):
            if not num % i:
                count += 1
        if count % 2:
            answer -= num
        else:
            answer += num
    return answer