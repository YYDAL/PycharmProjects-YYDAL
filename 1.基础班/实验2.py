import time
print("你好，欢迎使用本程序")
print("本程序暂时只能输入数字,每个数字之间请用英文逗号隔开")
print("现在仅作测试使用，未使用高级函数优化")
# time.sleep(1)
print('现在请先输入你的数据，方便我来帮助你')
try:
    shuju = input('请输入数据：')                #ValueError
    shuju = shuju.split(',')
    qqq = shuju.count(',')
    for i in range(qqq):
        shuju.remove(',')
    shuju = list(map(int, shuju))
except ValueError as buhuo:
    shuju = []
    print('输入错误,数据已清除,请选择2重新输入数据')
else:
    print('输入成功')
print('看看我可以干些什么')
while 1:
    xuanze = input('1，查看当前数据  2，添加其他数据  3，查找数据  4，删除数据  5，修改数据  6，统计数据  7，排序  8，退出    请选择你的指令')
    if xuanze == '1':
        print(shuju)
        continue
    elif xuanze == '2':
        try:
            tianji = input('请输入数据：')
            tianji = tianji.split(',')
            www = tianji.count(',')
            for i in range(www):
                tianji.remove(',')
            tianji = list(map(int, tianji))
        except ValueError as buhuo:
            print('输入错误,本次操作已撤销,请重新输入数据')
            tianji = []
        else:
            print('添加成功成功')
        shuju = shuju + tianji
        continue
    elif xuanze == '3':
        try:
            chazhao = int(input('请输入要查找的数据：'))
            eee = str(shuju.count(chazhao))
            print('一共有' + eee + '个')
        except ValueError as buhuo:
            print('输入错误，请重新输入')
        continue
    elif xuanze == '4':
        try:
            shanchu = int(input('请输入你要删除的数据：'))
            geshu = int(input('请输入删除的数量：'))
            # rrr = shuju.count(shanchu)
            for i in range(0, geshu):
                shuju.remove(shanchu)
        except ValueError as buhuo:
            print('未找到该数据或已将该数据全部删除')
        else:
            print('删除成功')
        continue
    elif xuanze == '5':
        try:
            xiugai = int(input('请输入你要修改的数据：'))
            xiugai2 = int(input('你要改为：'))
            geshu2 = int(input('请输入修改的数量：'))
            for i in range(geshu2):
                shuju.remove(xiugai)
                shuju.append(xiugai2)
        except ValueError as buhuo:
            print('未找到该数据或已将该数据全部修改')
        else:
            print('修改成功')
        continue
    elif xuanze == '6':
        jihe = list(set(shuju))
        for i in range(len(jihe)):
            tongji = str(shuju.count(jihe[i]))
            q1 = str(jihe[i])
            print(q1 + '有' + tongji + '个')
        continue
    elif xuanze == '7':
        w1 = int(input('1，正序  2，倒序'))
        if w1 == 1:
            shuju = sorted(shuju)
            print(shuju)
        elif w1 == 2:
            shuju = sorted(shuju)[::-1]
            print(shuju)
        else:
            print('输入错误请重新输入')
        continue
    elif xuanze == '8':
        break
    else:
        print('输入错误，请重新输入')
        continue
print('程序结束')




