def HHH(chuanru):
    def dakai():
        hhh = chuanru()
        return hhh + "哈哈哈哈"
    return dakai()

def qqq():
    return "我"

www = HHH(qqq)
print(www)