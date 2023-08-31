def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        array_num = sorted(arr, reverse=True)[-1]
        arr.remove(array_num)
        return arr