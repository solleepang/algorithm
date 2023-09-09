def solution(cards1, cards2, goal):
    
    c1 = 0
    c2 = 0
    for i in goal:
        if c1 < len(cards1):
            if i == cards1[c1]:
                c1 += 1
                continue
        if c2 < len(cards2):
            if i == cards2[c2]:
                c2 += 1
                continue
            
    return 'Yes' if c1+c2 == len(goal) else 'No'