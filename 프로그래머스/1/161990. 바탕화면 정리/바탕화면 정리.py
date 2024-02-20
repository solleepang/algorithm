def find_index(string):
    for i, c in enumerate(string):
        if c == "#":
            yield i

def solution(wallpaper):
    answer = [-1, -1, -1, -1]
    
    for i, string in enumerate(wallpaper):
        indices = list(find_index(string))
        if not indices:
            continue
        else:
            if answer[0] == -1:
                answer[0] = i
            answer[2] = i+1
            min_x = min(indices)
            min_y = max(indices)
            if answer[1] < 0 or answer[1] > min_x:
                answer[1] = min_x
            if answer[3] <= min_y:
                answer[3] = min_y +1
            
                
    return answer