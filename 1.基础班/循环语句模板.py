def chengji(shuzi):
    if shuzi > 1:
        qqq = shuzi*chengji(shuzi-1)
        # 循环调用后面的必须进行必要的变化否则会形成死循环
        return qqq
    else:
        return 1
a = chengji(8)
# 输入数据

print(a)