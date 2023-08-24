def solution(n):
    answer = 0
    count = 0
    
    while True:
        count += 1
        if n % count == 1:
            return count