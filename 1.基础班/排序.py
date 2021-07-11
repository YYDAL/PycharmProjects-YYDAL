ku = []
hhh = int(input('输入任意值后开始运行：'))
while hhh != '你猜不到':
    hhh = int(input('请输入数据，输入‘666’后开始计算：'))
    if hhh == 666:
        break
    else:
        ku.append(hhh)
panduan = int(input('选1正序运算，选2逆序运算：'))
if panduan == 1:
    print(sorted(ku))
elif panduan == 2:
    print(sorted(ku)[::-1])
else:
    print('我怀疑你在搞我')
jieshu = input('计算完成，输入任意值退出')