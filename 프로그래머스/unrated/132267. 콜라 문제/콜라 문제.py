def solution(a, b, n):
    answer = 0

    while n >= a:    
        r, c = divmod(n, a)
        result = r * b
        answer += result
        n = c + result
        
    return answer