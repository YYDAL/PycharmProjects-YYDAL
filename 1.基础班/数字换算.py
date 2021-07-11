import time
print('欢迎使用本应用')
time.sleep(1)
print('看看我可以干些啥')
time.sleep(1)
while 1:
    xuanze = input('请输入几进制转几进制，例：二进制转十进制，请输入')
    if xuanze == '二进制转十进制':
        hhh = int(input('请输入数据：'))
        qqq = int(str(hhh), 2)
        print(qqq)
    elif xuanze == '八进制转十进制':
        hhh = int(input('请输入数据：'))
        qqq = int(str(hhh), 8)
        print(qqq)
    elif xuanze == '十六进制转十进制':
        hhh = int(input('请输入数据：'))  # 10
        qqq = int(str(hhh), 16)
        print(qqq)
    elif xuanze == '十进制转十六进制':
        hhh = int(input('请输入数据：'))
        qqq = hex(hhh)
        print(qqq)
    elif xuanze == '二进制转十六进制':
        hhh = int(input('请输入数据：'))
        qqq = hex(int(str(hhh), 2))
        print(qqq)
    elif xuanze == '八进制转十六进制':
        hhh = int(input('请输入数据：'))  # 16
        qqq = hex(int(str(hhh), 8))
        print(qqq)
    elif xuanze == '十进制转二进制':
        hhh = int(input('请输入数据：'))
        qqq = bin(hhh)
        print(qqq)
    elif xuanze == '八进制转二进制':
        hhh = int(input('请输入数据：'))
        qqq = bin(int(str(hhh), 8))
        print(qqq)
    elif xuanze == '十六进制转二进制':
        hhh = int(input('请输入数据：'))  # 2
        qqq = bin(int(str(hhh), 16))
        print(qqq)
    elif xuanze == '十进制转八进制':
        hhh = int(input('请输入数据：'))
        qqq = oct(hhh)
        print(qqq)
    elif xuanze == '二进制转八进制':
        hhh = int(input('请输入数据：'))
        qqq = oct(int(str(hhh), 2))
        print(qqq)
    elif xuanze == '十六进制转八进制':
        hhh = int(input('请输入数据：'))  # 8
        qqq = oct(int(str(hhh), 16))
        print(qqq)
    elif xuanze =='退出':
        break
    else:
        print('小朋友，建议你看看你是不是哪里输错了，如果想退出程序请输入 退出 ')
        continue








