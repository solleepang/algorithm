def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        else:
            # 65-90 97-122
            num = ord(i)
            if num > 64 and num < 91:
                if num+n > 90:
                    answer += chr(num+n - 26)
                else:
                    answer += chr(num+n)
            if num > 96 and num < 123:
                if num+n > 122:
                    answer += chr(num+n - 26)
                else:
                    answer += chr(num+n)
                    
    return answer

