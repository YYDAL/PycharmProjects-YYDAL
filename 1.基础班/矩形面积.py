class Mianji:
    def __init__(self, gao, kuan):
        self.gao = gao
        self.kuan = kuan

    def Mianji0(self):
        jisuan = self.gao * self.kuan
        return '面积为%sm'%jisuan            #不能直接打印

al = Mianji(2,5)
# print(al.Mianji0())           #注意调用
q = al.Mianji0()         #两种方法都可以
print(q)