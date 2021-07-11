def shuzi(mubiao):
    if mubiao > 2:
        return shuzi(mubiao-1) + shuzi(mubiao-2)
    elif mubiao == 1:
        return 0                                   #因为数列的前两项无关联 需要手动添加
    elif mubiao == 2:
        return 1

def shuru(i):
    for cishu in range(1, i+1):                     #注意range中应该从1开始而不是0（若以0开始则会出现none）
        print(shuzi(cishu))

shuru(50)                                           #输入所要获取的数列的个数