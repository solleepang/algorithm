def solution(s):
    s = s.split(" ")
    
    answer = []
    for j in s:
        word = [letter.upper() if i % 2==0 else letter.lower() for i,letter in enumerate(list(j))]
        answer.append(''.join(word))
    
    return ' '.join(answer)
            
            
            