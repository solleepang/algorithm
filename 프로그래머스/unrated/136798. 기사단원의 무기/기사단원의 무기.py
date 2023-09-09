def solution(number, limit, power):
    # 5, 3, 2
    k = [1 for _ in range(number+1)] # [1,1,1,1,1,1]
    c = [0 for _ in range(number+1)] # [0,0,0,0,0,0]

    for i in range(len(k)):
        if i == 0:
            continue
        for j in range(i,len(k),i):
            # j=2 (2,5,2) j=2,4 k=[1,1,2,1,2,1] c=[0,1,2,1,2,1]
            # j=3 (3,5,3) j=3 k=[1,1,2,3,2,1] c=[0,1,2,2,2,1]
            # j=4 (4,5,4) j=4 k=[1,1,2,3,8,1] c=[0,1,2,2,3,1] ...
            k[j] *= i
            c[j] += 1
    c = c[1:] # [1,2,2,3,2]

    answer = 0
    for i in c:
        if i <= limit:
            answer += i
        else:
            answer += power

    return answer
