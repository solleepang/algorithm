def solution(lottos, win_nums):
    answer = []
    min_n = 7
    zero = 0
    # 최저순위: 아는것만 맞았을 때, 최고순위: 아는거 + 0 까지 다 맞았을 때
    for i in lottos:
        if i != 0:
            if i in win_nums:
                min_n -= 1
        else:
            zero += 1
            
    max_num = min(min_n - zero, 6)
    min_num = min(6, min_n)
                
    return [max_num, min_num]