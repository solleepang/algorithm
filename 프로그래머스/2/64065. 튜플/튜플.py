def solution(s):
    answer = []
    check_string = []
    s_list = sorted(s[2:-2].split('},{'), key=len)
    
    for i, snum in enumerate(s_list):
        if i == 0:
            num = snum
        else:
            split_snum = snum.split(',')
            for j in check_string:
                split_snum.remove(j)           
            num = split_snum[0]
        answer.append(int(num))
        check_string.append(num)
    return answer