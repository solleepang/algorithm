def solution(phone_number):
    letter = phone_number[:-4]
    return phone_number.replace(letter,'*'*len(letter))