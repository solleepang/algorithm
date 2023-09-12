def solution(food):
    answer_l = ''
    for i in range(len(food)):
        if food[i] <= 1:
            continue
        else:
            num = food[i] // 2
            answer_l +=  str(i) * num
    answer_r = answer_l[::-1]
    return answer_l + '0' + answer_r