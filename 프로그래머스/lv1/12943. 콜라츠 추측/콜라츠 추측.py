def solution(num):
    answer = 0
    count = 0
    while count < 500:
        if num == 1:
            return count
        count += 1        
        if not num % 2:
            num = num / 2
        else:
            num = num * 3 +1 
    count = -1
    return count