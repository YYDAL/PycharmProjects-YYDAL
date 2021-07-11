class HHH:
    def __init__(self, gao, kuan):
        self.gao = gao                             #加入一个数据
        self.kuan = kuan

    def __add__(self, other):
        gaoo = self.gao + other.gao                #加入别的数据
        kuann = self.kuan + other.kuan
        return gaoo, kuann

a = HHH(12, 4)
b = HHH(1, 5)                                     #输入数据
print(a + b)                                     #打印计算结果