# def chengji(shuzi):
#     if shuzi > 1:
#         qqq = shuzi*chengji(shuzi-1)
#         return qqq
#     else:
#         return 1
#
# a = chengji(8)
# #
# print(a)


# def hhh():
#     print('哈哈哈')
#
# def qita():
#     print('你是谁？')
#
# def fuwu(qqq,eee):
#     if eee == 1:
#         return qqq()
#     elif eee == 2:
#         print('阿狸')
#     elif eee == 3:
#         print('hhhh')
#     else:
#         print('永远')
#
# fuwu(hhh,3)
# fuwu(qita,1)


# def shuzi(mubiao):
#     if mubiao > 2:
#         return shuzi(mubiao-1) + shuzi(mubiao-2)
#     elif mubiao == 1:
#         return 0                                   #因为数列的前两项无关联 需要手动添加
#     elif mubiao == 2:
#         return 1
#
# def shuru(i):
#     for cishu in range(1,i+1):                     #注意range中应该从1开始而不是0（若以0开始则会出现none）
#         print(shuzi(cishu))
#
# shuru(7)                                           #输入所要获取的数列的个数


# def HHH(a,b):
#     c = a['name']
#     b,c = c,b
#     a['name'] = c                               #貌似是暴力换值法
#     print(a)
#     print(b)
#
#
# HHH({'name':222},(1, 2, 3, 4))                  #分别输入字典和元组


# def HHH(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     q = list(kwargs.values())               #不太了解tuple（应该是强行转化为元组的方法吧），我用的是list
#     print(q)
#     b = dict(zip(kwargs.keys(),args))       #这个是看完讲解后的代码，原来那个偏的太离谱了
#     print(b)
#
# HHH(1,3,4,2,z=32,x=43,c=75,v=30)

# li = []
# for i in range(5):
#     def qqq():
#         return i
#     li.append(qqq())
#
# print(li)


# class Mianji:
#     def __init__(self, gao, kuan):
#         self.gao = gao
#         self.kuan = kuan
#
#     def Mianji(self):
#         jisuan = self.gao * self.kuan
#         return '面积为%sm'%jisuan            #不能直接打印
#
# al = Mianji(2,5)
# print(al.Mianji())           #注意调用
# q = al.Mianji()         #两种方法都可以
# print(q)


# a = {q:w for q,w in [(1, 'z'),(2, 'x'),(4, 'c')]}
# print(a)


# li = [1,2,3,4,5]
# # print(dir(li))
# b = iter(li)
# print(b)
#
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# q = [i for i in range(10)]
# print(q)
#
# w = (a for a in range(10))
# print(w)


# import time as hhh
# hhh.sleep(0.2)

#
# print('111')


# import re
#
# a = 'hhhhhhhwwue'
# wo = re.match(r'hhh', a)
# print(wo)


# aa = '<img style="-webkit-user-select: none;margin: auto;" src="https://img.alicdn.com/imgextra/i4/352469034/O1CN01XUpDCe2GbcZVsbsLd_!!352469034.jpg">'


# import re
#
#
# ret = re.match(r'\d|[1-9]\d|1\d{2}')


# def fun():
#     li = []
#     for i in range(5):
#         li.append(lambda x: i ** x)
#     return li
#
#
# gun = fun()
#
# print(gun[0](2))
# print(gun[1](2))
# print(gun[2](2))




# a = int(input('输入你的路程'))
# way = a
# if a < 3:
#     print('10')
# elif 3 <= a < 20:
#     print(str((a-3)*3+10))
# else:
#     print(float(a-20)*3.6+61)


# class Mianji:
#     def __init__(self,long,height):
#         self.long = long
#         self.height = height
#
#     def Zhengfangxing(self):
#         mianji = self.long * self.height
#         return "面积是%sm"%mianji
#
# class tiji(Mianji):
#     def __init__(self, long, height):
#         if long == height:
#             Mianji.__init__(self,long,height)
#         else:
#             pass
#
# shuju = tiji(12, 12)
# print(shuju.Zhengfangxing())

# class Dog:
#     def __init__(self):
#         print("汪汪汪")
# class Mydog(Dog):
#     def __init__(self):
#         Dog.__init__(self)                 #调用自己
#         print("哈哈哈")                     #实现对父级的调用
#
# kaishi = Mydog()

# class Zuzong:                             #基类
#     def play(self):
#         print("我是老大")
#
# class A(Zuzong):
#     def play1(self):
#         print("我是老二")
#
# class B(Zuzong):
#     def play(self):
#         print("我是老三")
#
#     def play3(self):
#         print("我是哈哈哈")            #允许有多个方法
#
# class C(B,A):                         #让C继承一下父级，优先继承第一个，然后依次类推
#     pass                              #占位置
#
# HHH = C()                            #必须转化一下
# HHH.play1()                          #如果继承的第一个不具备调用的函数，则顺次寻找可继承者
# HHH.play3()                             #若括号内没有则继承基类，如都没有则报错


# class HHH:
# #     def __init__(self, gao, kuan):
# #         self.gao = gao                             #加入一个数据
# #         self.kuan = kuan
# #
# #     def __add__(self, other):
# #         gaoo = self.gao + other.gao                #加入别的数据
# #         kuann = self.kuan + other.kuan
# #         return gaoo, kuann
# #
# # a = HHH(1, 4)
# # b = HHH(1, 5)                                     #输入数据
# # print(a + b)                                     #打印计算结果




# class HHH:
#     def __init__(self, chang):
#         self.chang = chang
#
#     def Zfx(self):                                    正方形
#         mianji = self.chang**2
#         return mianji
#
# shuru = HHH(4)
# print(shuru.Zfx())



# class HHH:
#     def __init__(self, chang, kuan):
#         self.kuan = kuan
#         self.chang = chang
#     def jisuan(self):
#         mianji = self.chang * self.kuan
#         return "面积是%s平方米"%(mianji)
#
# a = HHH(2,3)
# print(a.jisuan())





# class Jilei:
#     def hhh(self):
#         print("111")
#     def hhh2(self):
#         print("1112")
# class A(Jilei):
#     def hhh(self):
#         print("222")
#     def hhh3(self):
#         print("2223")
# class B(Jilei):
#     def hhh(self):
#         print("333")
#     def hhh4(self):
#         print("3334")
# class C(A,B):
#     pass
#
# aaa = C()                 实例化
# aaa.hhh()






# class HHH:
#     _weizhi = None
#     def __new__(cls, *args, **kwargs):
#         if cls._weizhi == None:
#             cls._weizhi = object.__new__(cls)
#             return cls._weizhi                     #标准单例模式，需要记住
#         else:
#             return cls._weizhi
#
# A = HHH()
# B = HHH()
# print(id(A))                                      #此时的A,B同属于一个单例
# print(id(B))                                     #后者后把前者覆盖

# class Hzz:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "hhh"):
#             cls.hhh = object.__new__(cls)
#         return cls.hhh
# A = Hzz("qq")
# B = Hzz("aaa")
# print(id(A))
# print(id(B))



# class HHH:
#     def __init__(self, name):
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         return object.__new__(cls)
#
#
#     def run(self):
#         print("跑")
# qqq = HHH("hhh")
# qqq.run()

# class HHH:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "hhh"):
#             cls.hhh = object.__new__(cls)
#         return cls.hhh
#
# xiaoming = HHH("小明")
# xiaohong = HHH("小号")
# print(id(xiaoming))
# print(id(xiaohong))


# class HHH:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return "错误"
#
# wo = HHH("YYDAL")
# print(hasattr(wo, "name"))
# print(wo.nam)
# print(getattr(wo, "name"))


# class HHH:
#     def __get__(self, instance, owner):
#         #获取属性
#     def __set__(self, instance, value):
#         #修改属性
#     def __delete__(self, instance):
#         #删除属性

# def HHH(chuanru):
#     def dakai():
#         hhh = chuanru()
#         return hhh + "哈哈哈哈"
#     return dakai()
#
# def qqq():
#     return "我"
#
# www = HHH(qqq)
# print(www)
#

a = [1, 2, 3, 4, 5]
print(a)
a.pop()
print(a)
b = (1, 2, 3, 4, 5)
a.append(1)
print(a)
a.sort()
print(a)
a.reverse()
print(a)


































