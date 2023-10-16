def s_letter(fl, s):
    count_fl = 1
    count_nl = 0 
    count = 0
    while count_fl != count_nl: 
        count += 1
        if count == len(s):
            break
        if s[count] == fl:
            count_fl += 1
        else:
            count_nl += 1
    s = s[count+1:]
    return s

def solution(s):
    answer = 0
    while len(s) > 0:
        if len(s) == 1:
            answer += 1
            break
        else:
            s = s_letter(s[0],s)
            answer += 1
    return answer