def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    list_len1 = int(10000/len(one))
    list_len2 = int(10000/len(two))
    list_len3 = int(10000/len(three))
    
    one = one * list_len1
    two = two * list_len2
    three = three * list_len3
    
    a1 = 0
    a2 = 0
    a3 = 0
    
    for i, ans in enumerate(answers):
            if one[i] == ans:
                a1 += 1
            if two[i] == ans:
                a2 += 1
            if three[i] == ans:
                a3 += 1
            
    rank = {1:a1, 2:a2, 3:a3}
    all_rank_values = rank.values()
    max_rank_values = max(all_rank_values)
    
    for i in range(1, len(rank)+1):
        if rank[i] == max_rank_values:
            answer.append(i)

    return answer
