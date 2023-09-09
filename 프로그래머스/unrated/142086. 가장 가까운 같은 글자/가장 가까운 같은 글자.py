def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        string = s[:i]
        index = [j for j, c in enumerate(string) if c == s[i]]
        if index == []:
            answer.append(-1)
        else:
            answer.append(i - max(index))    
        
    return answer
        