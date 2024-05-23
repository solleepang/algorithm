def solution(operations):
    arr = []
    for i in operations:
        if i[0] == 'I':
            arr.append(int(i[2:]))
        elif i[0] == 'D':
            num = int(i[2:])
            if not arr:
                continue
            elif num > 0:
                arr.remove(max(arr))
            else:
                arr.remove(min(arr))
    
    return [max(arr), min(arr)] if arr else [0,0]