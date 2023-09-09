def solution(k, m, score):
    m_left = len(score) - (len(score) % m)
    scores = sum(sorted(score, reverse=True)[m-1:m_left:m])*m
    return scores