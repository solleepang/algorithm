def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in baby:
        babbling = [x for x in babbling if b*2 not in x]
        print(babbling)
        
    for b in baby:
        babbling = [word.replace(b, ' ') for word in babbling]
        print(babbling)
        
    for i in babbling:
        if i.isspace():
            answer += 1
    
    return answer