from datetime import date

def solution(a, b):
    dateDict = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    date_wd = date(2016, a, b).weekday()
    return  dateDict[date_wd]