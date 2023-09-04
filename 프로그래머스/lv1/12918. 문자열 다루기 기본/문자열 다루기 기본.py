def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    else:
        if s.isdigit():
            return True
        else:
            return False