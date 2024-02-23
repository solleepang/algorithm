def solution(dots):
    dots_list = sorted(dots)
    w = abs(dots_list[1][0] - dots_list[3][0])
    h = abs(dots_list[1][1] - dots_list[0][1])
    answer = w*h
    return answer