def solution(arr1, arr2):
    answer = arr1
    count = 0
    for i,j in zip(arr1, arr2):
        for k in range(len(i)):
            a = i[k] + j[k]
            answer[count][k] = a
        count += 1
    return answer
