def solution(angle):
    answer = 0
    degrees = {180:4, 91:3, 90:2, 0:1}
    for degree, num in degrees.items():
        if angle >= degree:
            return num