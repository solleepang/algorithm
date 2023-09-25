def solution(X, Y):
    arr = []
    
    num_list = ["0","1","2","3","4","5","6","7","8","9"]
    Xl = len(X)
    Yl = len(Y)
    for i in num_list:
        Xnum = X.replace(i, "")
        Ynum = Y.replace(i, "")
        xl = len(Xnum)
        yl = len(Ynum)
        if xl != Xl and yl != Yl:
            num1 = Xl-xl
            num2 = Yl-yl
            arr.append(i*min(num1,num2))

        if not Xnum or not Ynum:
            break
    
    if not arr:
        return "-1"
    else:
        res = ''.join(sorted(arr, reverse=True))
        res_check = res.replace("0", "")
        if not res_check:
            return "0"
        else:
            return res
    
    
