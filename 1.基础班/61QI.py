# bianchang = input('请输入第一条边长：')
# bianchang2 = input('请输入第二条边长：')
# bianchang3 = input('请输入第三条边长：')
# if bianchang!=bianchang2 and bianchang2!=bianchang3:
#     print('这不是一个矩形')
# elif bianchang==bianchang2 and bianchang2==bianchang3:
#     a = int(bianchang)**2
#     print('面积为%s'%a)
# elif bianchang!=bianchang2:
#     b = int(bianchang) * int(bianchang3)
#     print('面积为%s' %b)
# elif bianchang!=bianchang3:
#     c = int(bianchang) * int(bianchang2)
#     print('面积为%s' %c)




# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5, 6}
# c = a & b
# d = (a | b) - (a - b) - (b - a)
# print(c)
# print(d)
#
# # 可变： 集合{}   列表[]   字典{}
# #不可变；  字符串''   数值    元组（）
#


# a = {'name': 'hhh', 'age': 17}
# a.setdefault('性别', '男')
# print(a)
# a.pop('name')
# print(a)
# a.setdefault('性别')
# print(a.setdefault('性别'))
# print(a.keys())
# b = {'name': 'hhh2', 'age': 172}
# a.update(b)
# print(a.keys())
# print(a)


#
# i = 0
# ii = 0
# while i <= 100:
#     print('次数：', i)
#     ii = ii + i
#     print('总和:', ii)
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(str(i)+'*'+str(j)+'='+str(i*j)+'\t', end=' ')
#         j +=1
#     print()
#     i +=1

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, '*', j, '=', i*j, end='  ')
#     print()

# def hhh():
#     print('11111')
#
#
# hhh()



#
# def hhh(a):
#     print(a+1)
#
# hhh(111)

# def hhh(*args,**kwargs):
#     print(args)
#     print(*args)
#     print(kwargs)
#
# hhh(1,2,3,4,hh=11,de=35)


# print(dict(a=1))





# wo = 111
# eval('print(wo)')        #将本来是字符串的语句继续执行
#
# qqq = ['name', 'age', '性别']
# www = ['yydal', 20, 'nan']
# xinxi = zip(qqq, www)
# # print(list(xinxi))              #需要用list接收一下
# print(tuple(xinxi))
# print(dir(xinxi))               #查看xinxi的所有方法
# print(dict(xinxi))


###################################################################12.28

# if hhh != 66612121:
#     ku.append(hhh)
# else:
#     print(ku)
# ku = []
# hhh = int(input('输入任意值后开始运行：'))
# while hhh != '你猜不到':
#     hhh = int(input('请输入数据，输入‘666’后开始计算：'))
#     if hhh == 666:
#         break
#     else:
#         ku.append(hhh)
# panduan = int(input('选1正序运算，选2逆序运算：'))
# if panduan == 1:
#     print(sorted(ku))
# elif panduan == 2:
#     print(sorted(ku)[::-1])
# else:
#     print('我怀疑你在搞我')

# def hhh(a, b, c = '哈哈哈', *args):
#     qqq = '%s对着%s说%s'%(a, b, c)
#     print(qqq)
#
# hhh(1,3,4)
################################################################12.30
# def hhh (*args):
#     aa = list(args[0])
#     bb = list(args[1])
#     cc = dict(zip(bb, aa))
#     dd = dict(args[1])
#     zz = tuple(dd.values())
#     print(zz)
#     print(cc)
#     return (zz,cc)
# # a = (1, 2, 3, 4)
# # b = {'q': 111, 'w': 222, 'e': 333, 'r': 444}
# a = eval(input('请输入元组：'))
# b = eval(input('请输入字典：'))
# # a = input('请输入元组：')
# # b = input('请输入字典：')
# www = hhh(a, b)

##########################################################################1.1
# class Juxing:
#     def __init__(self, chang, kuan):
#         self.chang = chang
#         self.kuan = kuan
#     # def mianji(self):
#     def mianji(self):
#         jisuan = self.kuan * self.chang
#         return '面积为%s平方米'%jisuan
# hhh = Juxing(2,3)
# q = hhh.mianji()
# print(q)

##########################################################################1.3

# class hhh:
#     chushi = 0
#     eee = 12345
#     def fangfa(self):
#         self.chushi += 1
#     def __del__(self):
#         hhh()
# www = hhh()
# print(www.eee)
# www.fangfa()
# www.fangfa()
# print(www.chushi)
# www.__del__()
# print(www.chushi)
# print(www.chushi)

# class DDD:
#     def hhh(self):
#         print('哈哈哈哈')
#
# class qqq(DDD):
#     def hhh2(self):
#         print('1111')
# class www(DDD):
#     pass
# class eee(qqq):
#     print('2222')
#
# aaa = eee()
# aaa.hhh2()

#####################################################################1.4
# class Juxing:
#     def __init__(self, chang, kuan):
#         self.chang = chang
#         self.kuan = kuan
#     def mianji(self):
#         jisuan = self.kuan * self.chang
#         return '面积为%s平方米'%jisuan
# class Zhengfang(Juxing):
#         pass
# chang = int(input('请输入一边长'))
# kuan = int(input('请输入另一边长'))
# if chang != kuan:
#         print('你好像输错数据了,这不是一个正方形')
# else:
#     pass
# hhh = Zhengfang(chang, kuan)
# q = hhh.mianji()
# print(q)


# class DDD:
#     def hhh(self):
#         print('哈哈哈')
#
# class A(DDD):
#     def hh1(self):
#         print('a')
# class B(DDD):
#     def hh2(self):
#         print('b')
# class C(A):
#     def ww(self):
#         print('结束')
# hhh = C()
# hhh.hh1()
# hhh.ww()
# print(C.mro())


#############################################################################1.10
# print('开始')
# try:
#     print(aaa)
#     a2 = 'aa' + 1
#     print(aa+1)
# except NameError as aa:
#     print(aa)
#     print('第一处问题')
# except Exception as a1:
#     print(a1)
#     print('第二处问题')
# finally:
#     print('最终问题')
# print('结束')
#
# shu = int(input('请输入获取列表的长度：'))
# # a = [1, 1]
# a = list(iter([1, 1]))
# for i in a:
#     a.append(a[len(a)-1] + a[len(a)-2])
#     # print(len(a))
#     if len(a) > shu:
#         break
#     else:
#         pass
# print(a)


# import time
# a = 0
# b = 1
# while True:
#     a, b = b, a + b
#     time.sleep(1)
#     print(a)

#########################################################################1.11


# class hhh:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             #hasattr(类名，属性名)若没有该属性则创建一个，         #初始化基本格式
#             cls.instance = super().__new__(cls)
#             return cls.instance
#
#     def __init__(self):
#         self.shuxin = 11111
#
# aaa = hhh()
# print(aaa.shuxin)              #第一次正常调用
# bbb = hhh()
# print(bbb.shuxin)              #第二次被调用时则会无法获取该属性

#############################################################################1.13

# f = open('text.txt', 'w',encoding='utf-8')
# f.write('哈哈哈哈')
# f.close()
# import time
# def time_time(func):
#     def jisuan():
#         print('开始计时：')
#         kaishi_time = time.time()
#         func()
#         jieshu_time = time.time()
#         print('计时完成')
#         print('运行时间：%s'%(jieshu_time - kaishi_time))
#     return jisuan
# a = [1, 2, 3, 4, 5]
# @time_time
# def type_time():
#     for i in range(1000000):
#         type(a)
# @time_time
# def isinstance_time():
#     for i in range(1000000):
#         isinstance(a, list)
# type_time()
# isinstance_time()

#########################################################################1.15

#########################第一题
# a = [1, 2, 9, 2, 1, 4, 4]
# w = list(set(a))
# q = w + w
# for z in range(len(a)):
#     q.remove(a[z])
# print(q[0])

##########################第二题

# a = 1234321
# q = list(str(a))
# w = q[::-1]
# if q == w:
#     print('ture')
# else:
#     print('flase')

#########################第三题
# a = []
# q = 0
# for i in range(101):
#     if q % 3 == 0 and q % 5 == 0:
#         a.append('BiLi')
#     elif q % 3 == 0:
#         a.append('Bi')
#     elif q % 5 == 0:
#         a.append('Li')
#     else:
#         a.append(q)
#     q += 1
# print(a)

#############################第六题
# class House:
#     mianji = 100
#     name = '我的房子'
#     jiage = 1000000
#     def goumai():
#         print('你需要向House主人支付足够的钱')
#     def chushou():
#        print('House主人将获得钱')
# class Furniture(House):
#     def goumai():
#         print('你需要向Furniture主人支付足够的钱')
# wo = House
# wo.goumai()
# wo.chushou()
# ni = Furniture
# ni.goumai()

#############################第七题
# ransom = 'qerty'
# magazine = 'qwertyu'
# a = list(str(ransom))
# w = list(str(magazine))
# for z in range(len(a)):
#     if a[z] in w:
#         pass
#     else:
#         print('false')
#         break
#     if z == len(a)-1:
#         print('ture')
#     else:
#         pass

# a = int(input())
# b = int(input())
# print(a + b)


# year = '2020'
# name = 'happy new year' + ' ' + year
# print(name)


# a = [1, 2, 3, 4, 5]
# b = a
# print(b)
# b.append(0)
# print(b)
# print(a)

# hhh = '我最优秀'
# qqq = hhh.encode(encoding='UTF-8')
# print(qqq)
# www = qqq.decode(encoding='utf-8')
# print(www)






print('111')









