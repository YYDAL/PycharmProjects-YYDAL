class Zuzong:                             #基类
    def play(self):
        print("我是老大")

class A(Zuzong):
    def play1(self):
        print("我是老二")

class B(Zuzong):
    def play(self):
        print("我是老三")

    def play3(self):
        print("我是哈哈哈")            #允许有多个方法

class C(B,A):                         #让C继承一下父级，优先继承第一个，然后依次类推
    pass                              #占位置

HHH = C()                            #必须转化一下
HHH.play1()                          #如果继承的第一个不具备调用的函数，则顺次寻找可继承者
HHH.play3()                             #若括号内没有则继承基类，如都没有则报错
       #可以使用  super.方法  把所有的方法都调出来