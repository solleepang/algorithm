def solution(spell, dic):
    for word in dic:
        is_word = all(s in word for s in spell)
        if is_word:
            return 1
    return 2